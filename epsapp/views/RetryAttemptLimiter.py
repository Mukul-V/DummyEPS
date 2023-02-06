from datetime import datetime
from django.db.models import Q
from epsapp.models.UserAuthentication import UserAuthentication
from epsapp.serializers.UserAuthentication import UserAuthentication as UserAuthSerial


class RetryAttemptLimiter:

    def __init__(self, username, attempts, holding_time):
        self.username = username
        self.attempts = attempts
        self.holding_time = holding_time

    def checkUnderTimeout(self):
        INVALID_PASSWORD_LIMIT = 3
        INVALID_PASSWORD_LIMIT_REACHED_TIMEOUT = 10

        if self.attempts >= INVALID_PASSWORD_LIMIT and self.holding_time is not None:
            now = datetime.now()
            current_time = now.astimezone()
            time_gap = current_time - self.holding_time
            minutes = time_gap.seconds / 60
            if minutes <= INVALID_PASSWORD_LIMIT_REACHED_TIMEOUT:  #
                return True
            else:
                self.clearTimeout()
        else:
            return False  # Time_Out Finished

    def invalidAttempted(self):
        current_time = datetime.now().astimezone()
        qry = list(UserAuthentication.objects.filter(username=self.username, user_type=1).values("key", "invalid_attempt", "holding_datetime"))
        attempts = qry[0]["invalid_attempt"]
        key = qry[0]["key"]

        # Login is invalid so set the timer accordingly
        data = {
            "invalid_attempt": attempts+1,
            "holding_datetime": current_time,
        }
        user_key = UserAuthentication.objects.get(key=key, user_type=1)
        serial = UserAuthSerial(user_key, data=data, partial=True)
        if serial.is_valid(raise_exception=True):
            serial.save()  # Updated the attempts in the User Authentication Table

    # Login is successful so clear the timeout
    def clearTimeout(self):
        user = UserAuthentication.objects.get(Q(username=self.username) & Q(user_type=1))
        data = {  # clearTimeout Finished
                    "invalid_attempt": 0,
                    "holding_datetime": None,
                }
        serial = UserAuthSerial(user, data=data, partial=True)
        if serial.is_valid(raise_exception=True):
            serial.save()
