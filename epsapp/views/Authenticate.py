from django.db.models import Q
from epsapp.models.UserAuthentication import UserAuthentication
from epsapp.serializers.AuthTrailsSerializer import AuthTrails
from epsapp.models.Users import Users
from datetime import datetime
from epsapp.views.RetryAttemptLimiter import RetryAttemptLimiter


class Authenticate(object):
    def authenticate(username=None, password=None, **kwargs):  # (username, password)
        try:
            if kwargs['user_type'] == 2:  # Client User
                user = UserAuthentication.objects.get(Q(username=username) & Q(user_type=kwargs['user_type']))
                if user.check_password(password):
                    qry = list(UserAuthentication.objects.filter(username=username, user_type=kwargs['user_type']).values("key"))
                    qry1 = list(Users.objects.filter(user_auth=qry[0]["key"]).values('organization', 'os', 'mac_address', 'key'))
                    data = {
                        "user": user,
                        "organization": qry1[0]["organization"],
                        'user_key': qry1[0]["key"],
                        'os': qry1[0]["os"],
                        'mac_address': qry1[0]["mac_address"],
                    }
                    return data
                else:
                    return None

            if kwargs['user_type'] == 1:  # Admin User
                request = kwargs['request']
                user_agent = request.META.get('HTTP_USER_AGENT', '')
                if "Windows" in user_agent:
                    origin_os = "Windows"
                elif "Macintosh" in user_agent:
                    origin_os = "macOS"
                elif "Linux" in user_agent:
                    origin_os = "Linux"
                else:
                    origin_os = "Unknown"
                origin_ip = request.META['REMOTE_ADDR']

                user = UserAuthentication.objects.get(Q(username=username) & Q(user_type=kwargs['user_type']))
                qry = list(UserAuthentication.objects.filter(username=username, user_type=kwargs['user_type']).values("id", "invalid_attempt", "holding_datetime"))
                attempts = qry[0]["invalid_attempt"]
                holding_time = qry[0]["holding_datetime"]
                key = qry[0]["id"]
                retry = RetryAttemptLimiter(username, attempts, holding_time)
                val = retry.checkUnderTimeout()  # Checked the Checkout Time

                if val:  # Too Many Attempts
                    current_dateTime = datetime.now().astimezone()
                    auth_data = {
                        "type": "AUTH FAILED",
                        "reason": "Too Many Attempts",
                        "user_login": current_dateTime,
                        "user_agent": user_agent + "," + origin_ip + "," + origin_os,
                    }
                    serial = AuthTrails(data=auth_data)
                    if serial.is_valid(raise_exception=True):
                        serial.save()
                    return 0
                else:
                    if user.check_password(password):
                        retry.clearTimeout()  # Successfully
                        return user  # Password is Valid and returned User
                    else:
                        retry.invalidAttempted()  # Found Invalid Attempts
                        now = datetime.now()
                        current_time = now.astimezone()
                        auth_data = {  # Invalid Credentials pushed data in auth trails
                            "type": "AUTH FAILED",
                            "reason": "Invalid Credentials",
                            "user_login": current_time,
                            "user_agent": user_agent + "," + origin_ip + "," + origin_os,
                        }
                        serial = AuthTrails(data=auth_data)
                        if serial.is_valid(raise_exception=True):
                            serial.save()
                        return None
        except UserAuthentication.DoesNotExist:
            UserAuthentication().set_password(password)


