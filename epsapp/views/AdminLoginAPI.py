from rest_framework import status
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from epsapp.models.Trails.AuthTrails import AuthTrails
from epsapp.serializers.Trails.AuthTrails import AuthTrails as AuthTrailSerial
from rest_framework.views import APIView
from rest_framework.response import Response
from epsapp.serializers.UserLogin import UserLoginSerializer
from epsapp.views.Authenticate import Authenticate
from epsapp.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from epsapp.models.UserAuthentication import UserAuthentication
from epsapp.models.Role.RoleAndAction import RoleAndAction
from epsapp.models.FeatureTable import FeatureTable
from epsapp.models.Admin import Admin

count = 0


# Generate Token Manually
dictionary = {
    1: {
        "id": 'wijungle',
        "title": 'Wijungle',
        "messageId": 'sidebar.app.wi',
        "type": 'group',
        "children": [],
    },
    2: {
        "id": 'UserManagement',
        "title": 'UserManagement',
        "messageId": 'sidebar.app.dashboard.UserManagement',
        "icon": '<AiOutlineTeam />',
        # // type:'collapse',
        # path: '/wijungle/UserManagement/USer_Folder',
        # // children:[
        # //   {
        # //     id: 'UserManagement',
        # //     title: 'UserManagement',
        # //     messageId: 'sidebar.app.dashboard.UserManagement',
        # //     icon: <BsCurrencyBitcoin />,
        # //     path: '/wijungle/UserManagement/USer_Folder',
        # //   },
        #    // ]
    },
    3: {
        "id": 'KeyManagement',
        "title": 'KeyManagement',
        "messageId": 'sidebar.app.dashboard.KeyManagement',
        "icon": '<AiOutlineKey />',
        "path": '/wijungle/KeyManagement/Key_Foder',
    },
    4: {
        "id": 'PolicyManagement',
        "title": 'PolicyManagement',
        "messageId": 'sidebar.app.dashboard.PolicyManagement',
        "icon": '<AiOutlineForm />',
        "path": '/wijungle/PolicyManagement/Policy_Folders',
    },
    5: {
        "id": 'Hardware',
        "title": 'Hardware',
        "messageId": 'sidebar.app.dashboard.Hardware',
        "icon": '<AiOutlineSetting />',
        "path": '/wijungle/Hardware/Hardware_TAb',
    },
    6: {
        "id": 'Classification',
        "title": 'Classification',
        "messageId": 'sidebar.classification',
        "icon": '<AiOutlineApartment />',
        "path": '/wijungle/Classification/ClassFolder',
    },
    7: {
        "id": 'AppConrol',
        "title": 'AppControl',
        "messageId": 'sidebar.appcontrol',
        "icon": '<AiOutlineAppstore />',
        "path": '/wijungle/AppConrol/ACFoler',
    },
    8: {
        "id": 'DeviceControl',
        "title": 'DeviceControl',
        "messageId": 'sidebar.devicecontrol',
        "icon": '<AiTwotoneUsb />',
        "path": '/wijungle/DeviceControl/DCFolder',
    },
    9: {  # Have Children
        "id": 'dataleakpolicy',
        "title": 'Data Leak Policy',
        "messageId": 'sidebar.dataleakpolicy',
        "icon": '<AiOutlineDatabase />',
        "type": 'collapse',
        "children": [],
    },
    10: {
        "id": 'localprinter',
        "title": 'Local Printer',
        "messageId": 'sidebar.locprinter',
        "path": '/wijungle/DataLeakPolicy/Local-Printer',
    },
    11: {
        "id": 'webProtection',
        "title": 'Web Protection',
        "messageId": 'sidebar.WebProtectionpolicy',
        "path": '/wijungle/DataLeakPolicy/Web-Protection',
    },
    12: {
        "id": 'networkCare',
        "title": 'Network Care',
        "messageId": 'sidebar.dnetwcarey',
        "path": '/wijungle/DataLeakPolicy/Network-Care',
    },
    13: {
        "id": 'clip-board',
        "title": 'Clip Board Policy',
        "messageId": 'sidebar.clpboard',
        "path": '/wijungle/DataLeakPolicy/Clip-board',
    },
    14: {
        "id": 'screen-shots',
        "title": 'Screen-Shots Policy',
        "messageId": 'sidebar.scsh',
        "path": '/wijungle/DataLeakPolicy/Screen-shots',
    },
    15: {
        "id": 'afs',
        "title": 'App File Access',
        "messageId": 'sidebar.afs',
        "path": '/wijungle/DataLeakPolicy/App-fil-Access',
    },
    16: {  # have children
        "id": 'history',
        "title": 'History',
        "messageId": 'sidebar.history',
        "icon": '<AiFillClockCircle />',
        "type": 'collapse',
        "children": [],
    },
    17: {
        "id": 'UserHistory',
        "title": 'UserHistory',
        "messageId": 'sidebar.app.dashboard.UserHistory',
        "icon": '<BsCurrencyBitcoin />',
        "path": '/wijungle/History/UserHistory',
    },
    18: {
        "id": 'KeyHistory',
        "title": 'KeyHistory',
        "messageId": 'sidebar.app.dashboard.KeyHistory',
        "icon": '<BsCurrencyBitcoin />',
        "path": '/wijungle/History/KeyHistory',
    },
    19: {
        "id": 'History_tab',
        "title": 'History_tab',
        "messageId": 'sidebar.app.dashboard.HardwareHistory',
        "icon": '<BsCurrencyBitcoin />',
        "path": '/wijungle/History/HardwareHistory',
    },
    20: {
        "id": 'trail',
        "title": 'Trails',
        "messageId": 'sidebar.trails',
        "icon": '<InteractionOutlined />',
        "path": '/wijungle/Trails/TrailFolder',
    }
}


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }


class AdminLoginAPI(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')  # Checking User-Agent
        if "Windows" in user_agent:
            origin_os = "Windows"
        elif "Macintosh" in user_agent:
            origin_os = "macOS"
        elif "Linux" in user_agent:
            origin_os = "Linux"
        else:
            origin_os = "Unknown"
        origin_ip = request.META['REMOTE_ADDR']

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            if username is None and password is None and request.headers.get('Authorization'):  # Code for the Page Refresh
                token = request.headers.get('Authorization')
                permission_classes = [IsAuthenticated]
                return Response(token)

            extra = {"user_type": 1, "request": request}
            user = Authenticate.authenticate(username=username, password=password, **extra)

            if user == 0:  # Max Attempt Reached
                return Response("Max Login Limit Reached wait and Try Again Later")

            if user is not None:  # User is Valid and Authenticated
                qry = list(UserAuthentication.objects.filter(username=user).values_list('organization', 'id'))
                role_qry = list(Admin.objects.filter(user_auth=qry[0][1]).values('role_id'))
                print(role_qry)
                role = role_qry[0]["role_id"]
                if role is None:
                    return Response("Invalid Role of User")
                request.session['org_id'] = qry[0][0]  # Store the Organization ID in Session
                request.session["user_id"] = qry[0][1]  # Store the User/Admin ID in Session
                token = get_tokens_for_user(user)
                request.session["access_token"] = token["access"]
                request.session["refresh_token"] = token["refresh"]
                now = datetime.now()
                current_time = now.astimezone()
                auth_data = {  # Data of Auth Trail
                    "type": "AUTH SUCCESS",
                    "user": qry[0][1],
                    "user_login": current_time,
                    "user_logout": "ACTIVE",
                    "user_agent": user_agent,
                    "user_ip": origin_ip,
                    "user_os": origin_os,
                    "token": token["access"]
                }

                serial = AuthTrailSerial(data=auth_data)
                if serial.is_valid(raise_exception=True):
                    serial.save()
                key = AuthTrails.objects.latest()
                trail_key = list(AuthTrails.objects.filter(key=key).values("key"))
                request.session["auth_trail"] = trail_key[0]['key']
                role_permit = list(RoleAndAction.objects.filter(role=role).values("feature_id", "permission").filter(permission__gt=0))
                feature_id = []
                permission_grant = []
                permission = {}
                for val in role_permit:
                    feature_id.append(val['feature_id'])
                    permission[val['feature_id']] = val["permission"]
                    permission_grant.append(val["permission"])
                feature_data = list(FeatureTable.objects.all().filter(key__in=feature_id).values("self_type", "id_parent", "id_grand_parent"))
                request.session["features"] = feature_id
                request.session["permissions"] = permission_grant

                menu_data = {}
                for i in range(len(feature_id)):
                    if feature_data[i]["self_type"] == 1:
                        menu_data[feature_id[i]] = dictionary[feature_id[i]]
                    if feature_data[i]["self_type"] == 2:
                        parent = feature_data[i]["id_parent"]
                        menu_data[parent]['children'].append(dictionary[feature_id[i]])
                    # if feature_data[i]["self_type"] == 3:
                    #     grand_parent = feature_data[i]["id_grand_parent"]
                    #     parent = feature_data[i]["id_parent"]
                    #     menu_data[grand_parent]["children"][parent]["children"][feature_id[i]] = dictionary[feature_id[i]]
                session_id = request.session.session_key
                print(request.session['org_id'])
                print(request.session['user_id'])
                response_data = {
                    "token": token,
                    "msg": "Login Success",
                    "data": menu_data,
                    "permission": permission,
                    "session_id": session_id
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:  # User Pass Something Invalid in Credentials
                return Response({'errors': {'none_field_error': 'Username or Password is not Valid'}}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
