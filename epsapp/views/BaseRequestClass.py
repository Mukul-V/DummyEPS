from datetime import datetime

from rest_framework_simplejwt.tokens import RefreshToken
from epsapp.ENUM_File import audit_type, audit_action
from epsapp.serializers.AuditTrailsSerializer import AuditTrails


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }


# Auto Loader for Reflex
def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


# Dictionary of request params, models, serializers
dictionary = {
    "antivirus": ['Antivirus', 'AntivirusSerializer'],
    "antivirus-negative-path": ['AntivirusNegativePath', 'AntivirusNegativePathSerializer'],

    "app-class": ['AppClassification', 'AppClassificationSerializer'],
    "app-class-data": ['AppClassificationData', 'AppClassificationDataSerializer'],

    "app-policy": ['AppControlPolicy', 'AppControlPolicySerializer'],
    "app-policy-data": ['AppControlPolicy.AppControlPolicyData', 'AppControlPolicy.AppControlPolicyData'],

    "app-file-dlp": ['AppFileAccessDlp', 'AppFileAccessDlpSerializer'],
    "app-file-dlp-data": ['AppFileAccessDlpData', 'AppFileAccessDlpDataSerializer'],

    "base-class-grp": ['BaseClassificationGroup', 'BaseClassificationGroupSerializer'],
    "class-grp": ['ClassificationGroupMapping', 'ClassificationGroupMappingSerializer'],

    "clipboard-dlp": ['ClipboardDlp', 'ClipboardDlpSerializer'],
    "clipboard-dlp-data": ['ClipboardDlpData', 'ClipboardDlpDataSerializer'],

    "device-policy": ['DeviceControlPolicy', 'DeviceControlPolicySerializer'],
    "exception": ['DeviceException', 'DeviceExceptionSerializer'],

    "file-class": ['FileClassification', 'FileClassificationSerializer'],
    "file-upload": ['', 'FileUploadSerializer'],
    "file-data": ['FileData', 'FileDataSerializer'],

    "user-history": ['UserHistory', 'UserHistorySerializer'],

    "printer-dlp": ['LocalPrinterDlp', 'LocalPrinterDlpSerializer'],
    "printer-dlp-data": ['LocalPrinterDlpData', 'LocalPrinterDlpDataSerializer'],

    "network-dlp": ['NetworkDlp', 'NetworkDlpSerializer'],
    "network-dlp-data": ['NetworkDlpData', 'NetworkDlpDataSerializer'],

    "role": ['Role', 'RoleSerializer'],
    "role-action": ['RoleAndAction', 'RoleAndActionSerializer'],

    "rules": ['Rules', 'RulesSerializer'],
    "rules-action": ['RuleUserMapping', 'RuleUserMappingSerializer'],

    "schedule-class": ['ScheduleClassification', 'ScheduleClassificationSerializer'],
    "schedule-days": ['ScheduleDays', 'ScheduleDaysSerializer'],

    "screenshot-dlp": ['ScreenshotDlp', 'ScreenshotDlpSerializer'],
    "screenshot-dlp-data": ['ScreenshotDlpData', 'ScreenshotDlpDataSerializer'],

    "settings": ['Settings', 'SettingsSerializer'],
    "settings-negative-path": ['SettingsNegativePathModel', 'SettingsNegativePathModelSerializer'],

    "audit-trails": ['AuditTrails', 'AuditTrailsSerializer'],
    "auth-trails": ['AuthTrails', 'AuthTrailsSerializer'],

    "user-group": ['UserGroup', 'UserGroupSerializer'],
    "user-group-mapping": ['Users_User_Group_Mapping', 'Users_User_Group_Mapping_Serializer'],

    "domain": ['Domain', "DomainSerializer"],
    "web-class": ['WebClassification', 'WebClassificationSerializer'],

    "web-dlp": ['WebDlp', 'WebDlpSerializer'],
    "web-dlp-data": ['WebDlpData', 'WebDlpDataSerializer'],

    "web-filtering": ['WebFiltering', 'WebFilteringSerializer'],
    "web-filtering-mapping": ['WebFilteringMapping', 'WebFilteringMappingSerializer'],

    "admin": ['Admin', 'AdminSerializer'],

    "app-version": ['AppVersion', 'AppVersionSerializer'],

    "super-class": ['ClassificationSuperClass', 'ClassificationSuperClassSerializer'],

    "content-class": ['ContentClassification', 'ContentClassificationSerializer'],

    "device-class": ['DeviceClassification', 'DeviceClassificationSerializer'],

    "feature-table": ['FeatureTable', 'FeatureTableSerializer'],

    "hardware": ['Hardware', 'HardwareSerializer'],

    "ip-class": ['IpClassification', 'IpClassificationSerializer'],

    "keys": ['KeysTable', 'KeysTableSerializer'],

    "organization": ['Organization', 'OrganizationSerializer'],

    "os-table": ['OsTable', 'OsTableSerializer'],

    "reporting": ['Reporting', 'ReportingSerializer'],

    "token-auth": ['TokenAuth', 'TokenAuthSerializer'],

    "user-auth": ['UserAuthentication', 'UserAuthenticationSerializer'],

    "user-hardware-restrict": ['UserHardwareRestrict', 'UserHardwareRestrictSerializer'],

    "users": ["Users", "UsersSerializer"]
}

# Columns of the Table in UI

# USER COLUMN
user_column = [
    {"dataIndex": "name", "title": "Name", "align": "center"},
    {"dataIndex": "phone", "title": "Phone Number", "align": "center"},
    {"dataIndex": "email", "title": "Email Address", "align": "center"},
    {"dataIndex": "dob", "title": "Date of Birth", "align": "center"},
    {"dataIndex": "user_auth_username", "title": "Username", "align": "center"},
    {"dataIndex": "user_auth_is_active", "title": "Status", "align": "center"},
]

# USER HISTORY COLUMN
user_history = [
    {"dataIndex": "user_id", "title": "User ID", "align": "center"},
    {"dataIndex": "hardware_id", "Hardware ID": "Phone Number", "align": "center"},
    {"dataIndex": "login", "title": "Login Time", "align": "center"},
    {"dataIndex": "logout", "title": "Logout Time", "align": "center"},
]

# ADMIN COLUMN
admin_column = [
    {"dataIndex": "name", "title": "Name", "align": "center"},
    {"dataIndex": "phone", "title": "Phone Number", "align": "center"},
    {"dataIndex": "email", "title": "Email Address", "align": "center"},
    {"dataIndex": "dob", "title": "Date of Birth", "align": "center"},
]

# KEY COLUMN
key_column = [
    {"dataIndex": "key_value", "title": "Key", "align": "center"},
    {"dataIndex": "issue_date", "title": "Date of Issue", "align": "center"},
    {"dataIndex": "tenure", "title": "Tenure", "align": "center"},
    {"dataIndex": "activate_date", "title": "Date of Activation", "align": "center"},
    {"dataIndex": "expiry_date", "title": "Date of Expiry", "align": "center"},
]

# CLASSIFICATION COLUMN TYPE 1
class_1 = [
    {"dataIndex": "name", "title": "Name"},
    {"dataIndex": "description", "title": "Description"}
]

# CLASSIFICATION DEVICE COLUMN TYPE 2
class_device = [
    {"dataIndex": "name", "title": "Name"},
    {"dataIndex": "description", "title": "Description"},
    {"dataIndex": "device_type", "title": "Device Type"},
    {"dataIndex": "device_name_regex", "title": "Name/Regex"},
    {"dataIndex": "vid_pid", "title": "VID/PID"},
    {"dataIndex": "serial_number", "title": "Device Serial No."},
    {"dataIndex": "brand", "title": "Brand"},
]

# POLICY COLUMN
policy_1 = [
    {"dataIndex": "name", "title": "Name"},
    {"dataIndex": "description", "title": "Description"},
    {"dataIndex": "schedule_class_group", "title": "Schedule"},
]

# RULE COLUMN
rule_column = [
    {"dataIndex": "name", "title": "Name", "align": "center"},
    {"dataIndex": "description", "title": "Description", "align": "center"},
    {"dataIndex": "device_control_policy", "title": "Device Control Policy", "align": "center"},
    {"dataIndex": "app_control_policy", "title": "App Control Policy", "align": "center"},
    {"dataIndex": "app_file_access_dlp", "title": "App-File Access DLP", "align": "center"},
    {"dataIndex": "clipboard_dlp", "title": "Clipboard DLP", "align": "center"},
    {"dataIndex": "local_printer_dlp", "title": "Local Printer DLP", "align": "center"},
    {"dataIndex": "network_dlp", "title": "Network DLP", "align": "center"},
    {"dataIndex": "screenshot_dlp", "title": "Screenshot DLP", "align": "center"},
    {"dataIndex": "web_dlp", "title": "Web DLP", "align": "center"},
]

# REPORTING COLUMN
reporting_column = [
    {"dataIndex": "name", "title": "Name", "align": "center"},
    {"dataIndex": "incident_time", "title": "Incident Time", "align": "center"},
    {"dataIndex": "source", "title": "Source", "align": "center"},
    {"dataIndex": "endpoint", "title": "Endpoints", "align": "center"},
    {"dataIndex": "policy", "title": "Policy", "align": "center"},
    {"dataIndex": "channel", "title": "Channels", "align": "center"},
    {"dataIndex": "destination", "title": "Destinations", "align": "center"},
    {"dataIndex": "transaction_size", "title": "Transactions Size", "align": "center"},
    {"dataIndex": "action", "title": "Action", "align": "center"},
    {"dataIndex": "maximum_matches", "title": "Maximum Matches", "align": "center"},
    {"dataIndex": "status", "title": "Status", "align": "center"},
    {"dataIndex": "severity", "title": "Severity", "align": "center"},
    {"dataIndex": "created_by", "title": "Created By", "align": "center"},
    {"dataIndex": "updated_by", "title": "Updated By", "align": "center"},
    {"dataIndex": "detected_by", "title": "Detected By", "align": "center"},
    {"dataIndex": "files", "title": "Files", "align": "center"},
    {"dataIndex": "application_name", "title": "Application Name", "align": "center"},
    {"dataIndex": "direction", "title": "Direction", "align": "center"},
]

# HARDWARE COLUMN
hardware_column = [
    {"dataIndex": "hardware_value", "title": "Hardware ID", "align": "center"},
    {"dataIndex": "user", "title": "User ID", "align": "center"},
    {"dataIndex": "key_value", "title": "Key", "align": "center"},
    {"dataIndex": "bandwidth", "title": "Bandwidth", "align": "center"},
    {"dataIndex": "cpu", "title": "CPU", "align": "center"},
    {"dataIndex": "ram", "title": "RAM", "align": "center"},
    {"dataIndex": "hdd", "title": "HDD", "align": "center"},
    {"dataIndex": "current_wifi", "title": "Current WiFi", "align": "center"},
    {"dataIndex": "current_ip", "title": "Current IP", "align": "center"}
]

# ANTIVIRUS COLUMN
antivirus_column = [
    {"dataIndex": "max_file_size_scan", "title": "Max File Size", "align": "center"},
    {"dataIndex": "extension", "title": "Extension", "align": "center"},
    {"dataIndex": "custom", "title": "Custom", "align": "center"},
]


# GET API

def get_data(models, page, rows, org_id, user_id, auth_trail, field="key", order="1", column=None, val=None, types=None, class_type=None):

    # PAGINATION ROWS AND COLUMNS
    keys = org_id
    val1 = rows * (page - 1)
    val2 = (val1 + rows)

    # COLUMN ASSIGNING AS PER MODEL
    if models == "admin" and types == "admin_column":
        col = admin_column

    elif models == "antivirus" and types == "antivirus_column":
        col = antivirus_column

    elif models == "reporting" and types == "reporting":
        col = reporting_column

    elif models == "users" and types == "user_column":
        col = user_column

    elif models == "keys" and types == "key_column":
        col = key_column

    elif models == "device-class" or models == "app-class" or models == "web-class" or models == "ip-class" or models == "file-class" or models == "schedule-class" and types == "class_1":
        col = class_1

    elif models == "device-class" and types == "class_device_2":
        col = class_device

    elif models == "device-policy" or models == "app-policy" or models == "printer-dlp" or models == "network-dlp" or models == "clipboard-dlp" or models == "screenshot-dlp" or models == "web-dlp" or models == "app-file-dlp" and types == "policy_1":
        col = policy_1

    elif models == "policy" and types == "rule_1":
        col = rule_column

    elif models == "base-class-grp" and types == "app" or types == "web" or types == "file" or types == "device" or types == "ip" or types == "schedule":
        col = class_1

    elif models == "hardware":
        col = hardware_column

    elif models == "user-history":
        col = user_history

    else:
        col = None

    # FETCHING DATA FROM DATABASE
    if models in dictionary:  # Common Get for all Models
        model = my_import('epsapp.models.' + dictionary[models][0])
        print(model)
        serializer = my_import('epsapp.serializers.' + dictionary[models][1])
        print(serializer)
        qry_len = 0
        detail = 0

        if column is not None and val is not None:  # COLUMN SEARCH
            detail = model.objects.all().order_by(field).filter(**{column + "__icontains": val}).filter(organization=keys)[val1:val2]
            qry_len = model.objects.all().order_by(field).filter(**{column + "__icontains": val}).count()  # NEED TO CHECK LATER ONCE

        elif order == "1":  # INCREASING ORDER {DEFAULT}
            if models == "base-class-grp" and types == "app" or types == "web" or types == "file" or types == "device" or types == "ip" or types == "schedule":  # CLASSIFICATION GROUP GET
                detail = model.objects.all().filter(type=types).order_by(field).filter(organization=keys)[val1:val2]
                qry_len = model.objects.all().filter(type=types).order_by(field).count()  # NEED TO CHECK LATER ONCE
            else:
                if models == "users":  # USERS GET API
                    detail = model.objects.values('key', 'name', 'phone', 'email', 'dob', 'user_auth__username', 'user_auth__is_active').order_by(field).filter(organization=keys)[val1:val2]
                    qry_len = model.objects.all().order_by(field).count()

                elif models == "organization":  # ORGANIZATION GET API
                    detail = model.objects.all().order_by(field)[val1:val2]
                    qry_len = model.objects.all().order_by(field).count()

                else:  # COMMON GET FOR ALL
                    detail = model.objects.all().order_by(field).filter(organization=keys)[val1:val2]
                    qry_len = model.objects.all().order_by(field).count()

        elif order == "0":  # DECREASING ORDER
            if models == "base-class-grp" and types == "app" or types == "web" or types == "file" or types == "device" or types == "ip" or types == "schedule":  # CLASSIFICATION GROUP GET
                detail = model.objects.all().filter(type=types).order_by("-" + field).filter(organization=keys)[val1:val2]
                qry_len = model.objects.all().filter(type=types).order_by("-" + field).count()

            elif models == "organization":  # ORGANIZATION GET
                detail = model.objects.all().order_by("-" + field)[val1:val2]
                qry_len = model.objects.all().order_by("-" + field).count()

            else:  # COMMON GET FOR ALL
                detail = model.objects.all().order_by("-" + field).filter(organization=keys)[val1:val2]
                qry_len = model.objects.all().order_by("-" + field).count()
        serial = serializer(detail, many=True).data
        data = {
            'count': qry_len,
            'column': col,
            'data': serial
        }
        return data

    else:
        return "Data Not Found"


# POST DATA
def post_data(org_id, user_id, auth_trail, models, data, action=None):
    print("Function called")
    # ANTIVIRUS POST
    print(models)
    if models in dictionary and models == "antivirus":
        # from epsapp.serializers.Antivirus.Antivirus
        serializer = my_import('epsapp.serializers.' + dictionary[models][1])
        print(serializer)
        data["organization"] = org_id
        serial = serializer(data=data)
        if serial.is_valid(raise_exception=True):
            print("Serializer is valid Good")
        # else:
        #     print("There is some mistake Check Again")
        return "Working on the Device Control Condition"


def post_user(org_id, user_id, auth_trail, models, data):  # Add New User  org_id, user_id, auth_trail, model, data
    user_auth_model = my_import('epsapp.models.' + dictionary["user-auth"][0])
    print(user_auth_model)
    model = my_import('epsapp.models.' + dictionary[models][0])
    print(model)
    serializer = my_import('epsapp.serializers.' + dictionary[models][1])
    print(serializer)
    user_auth_serial = my_import('epsapp.serializers.' + dictionary["user-auth"][1])
    print(user_auth_serial)
    if data.get("username") is None or data.get("password") is None or data.get("password2") is None or org_id is None:
        return "Required Fields are Empty"
    data["organization"] = org_id
    auth_data = {
        "organization": org_id,
        "username": data["username"],
        "password": data["password"],
        "password2": data["password2"],
        "user_type": 2,
    }
    print(auth_data)
    print(user_auth_serial)
    auth_serial = user_auth_serial(data=auth_data)
    if auth_serial.is_valid(raise_exception=True):  # Serializing the User Authentication Data
        auth_serial.save()  # Inserting details in Auth Table
        key = user_auth_model.objects.latest()  # (LATEST KEY OF USER AUTHENTICATION TABLE)

        data["user_auth"] = key  # Adding user_authentication key in the User Personal Detail Data
        serial = serializer(data=data)
        if serial.is_valid(raise_exception=True):  # Serializing the Data for User table with user_auth ID
            serial.save()  # Saved Data in The User Table

            key = model.objects.latest()  # (THE LATEST KEY OF USER TABLE)
            if data.get("hardware_value"):  # Inserting Data in USER_HARDWARE_RESTRICT
                hardware_value = data.get("hardware_value")
                hardware_user_model = my_import('epsapp.models.' + dictionary["user-hardware-restrict"][0])
                details = []
                for i in range(len(hardware_value)):
                    details.append(hardware_user_model(user=key, hardware_value=hardware_value[i]))
                hardware_user_model.objects.bulk_create(details)  # Domain Bulk Insertion

            # Code for the insertion in Audit Trail:
            current_dateTime = datetime.now()
            audit_data = {
                "auth_trail": auth_trail,
                "type": audit_type.TASK_SUCCESS.value,
                "date_time": current_dateTime,
                "action": audit_action.CREATE_RECORD.value + " Add New User"
            }
            serial = AuditTrails(data=audit_data)
            if serial.is_valid(raise_exception=True):
                serial.save()
            return 'User Registration Success'
        else:
            # Code for the insertion in Audit Trail:
            current_dateTime = datetime.now()
            audit_data = {
                "auth_trail": auth_trail,
                "type": audit_type.TASK_FAILED.value,
                "date_time": current_dateTime,
                "action": audit_action.CREATE_RECORD.value + " Classification Group"
            }
            serial = AuditTrails(data=audit_data)
            if serial.is_valid(raise_exception=True):
                serial.save()
            return "Record Not Saved Successfully"
    else:
        return serializer.errors
