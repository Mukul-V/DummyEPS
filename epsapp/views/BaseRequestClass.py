from rest_framework_simplejwt.tokens import RefreshToken


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
    print("in import")
    return mod


# Dictionary of request params, models, serializers
dictionary = {
    "antivirus": ['Antivirus', 'Antivirus'],
    "antivirus-negative-path": ['Antivirus.AntivirusNegativePath', 'Antivirus.AntivirusNegativePath'],

    "app-class": ['AppClassification.AppClassification', 'AppClassification.AppClassification'],
    "app-class-data": ['AppClassification.AppClassificationData', 'AppClassification.AppClassificationData'],

    "app-policy": ['AppControlPolicy.AppControlPolicy', 'AppControlPolicy.AppControlPolicy'],
    "app-policy-data": ['AppControlPolicy.AppControlPolicyData', 'AppControlPolicy.AppControlPolicyData'],

    "app-file-dlp": ['AppFileAccessDlp.AppFileAccessDlp', 'AppFileAccessDlp.AppFileAccessDlp'],
    "app-file-dlp-data": ['AppFileAccessDlp.AppFileAccessDlpData', 'AppFileAccessDlp.AppFileAccessDlpData'],

    "base-class-grp": ['ClassificationGroup.BaseClassificationGroup', 'ClassificationGroup.BaseClassificationGroup'],
    "class-grp": ['ClassificationGroup.ClassificationGroupMapping', 'ClassificationGroup.ClassificationGroupMapping'],

    "clipboard-dlp": ['ClipboardDlp.ClipboardDlp', 'ClipboardDlp.ClipboardDlp'],
    "clipboard-dlp-data": ['ClipboardDlp.ClipboardDlpData', 'ClipboardDlp.ClipboardDlpData'],

    "device-policy": ['DeviceControlPolicy.DeviceControlPolicy', 'DeviceControlPolicy.DeviceControlPolicy'],
    "exception": ['DeviceControlPolicy.DeviceException', 'DeviceControlPolicy.DeviceException'],

    "file-class": ['FileClassification.FileClassification', 'FileClassification.FileClassification'],
    "file-upload": ['', 'FileClassification.FileUploadSerializer'],
    "file-data": ['FileData', 'FileDataSerializer'],

    "user-history": ['History.UserHistory', 'History.UserHistory'],

    "printer-dlp": ['LocalPrinterDlp.LocalPrinterDlp', 'LocalPrinterDlp.LocalPrinterDlp'],
    "printer-dlp-data": ['LocalPrinterDlp.LocalPrinterDlpData', 'LocalPrinterDlp.LocalPrinterDlpData'],

    "network-dlp": ['NetworkDlp.NetworkDlp', 'NetworkDlp.NetworkDlp'],
    "network-dlp-data": ['NetworkDlp.NetworkDlpData', 'NetworkDlp.NetworkDlpData'],

    "role": ['Role.Role', 'Role.Role'],
    "role-action": ['Role.RoleAndAction', 'Role.RoleAndAction'],

    "rules": ['Rules.Rules', 'Rules.Rules'],
    "rules-action": ['Rules.RuleUserMapping', 'Rules.RuleUserMapping'],

    "schedule-class": ['ScheduleClassification.ScheduleClassification', 'ScheduleClassification.ScheduleClassification'],
    "schedule-days": ['ScheduleClassification.ScheduleDays', 'ScheduleClassification.ScheduleDays'],

    "screenshot-dlp": ['ScreenshotDlp.ScreenshotDlp', 'ScreenshotDlp.ScreenshotDlp'],
    "screenshot-dlp-data": ['ScreenshotDlp.ScreenshotDlpData', 'ScreenshotDlp.ScreenshotDlpData'],

    "settings": ['Settings.Settings', 'Settings.Settings'],
    "settings-negative-path": ['Settings.SettingsNegativePathModel', 'Settings.SettingsNegativePathModel'],

    "audit-trails": ['Trails.AuditTrails', 'Trails.AuditTrails'],
    "auth-trails": ['Trails.AuthTrails', 'Trails.AuthTrails'],

    "user-group": ['UserGroup.UserGroup', 'UserGroup.UserGroup'],
    "user-group-mapping": ['UserGroup.Users_User_Group_Mapping', 'UserGroup.Users_User_Group_Mapping'],

    "domain": ['WebClassification.Domain', "WebClassification.Domain"],
    "web-class": ['WebClassification.WebClassification', 'WebClassification.WebClassification'],

    "web-dlp": ['WebDlp.WebDlp', 'WebDlp.WebDlp'],
    "web-dlp-data": ['WebDlp.WebDlpData', 'WebDlp.WebDlpData'],

    "web-filtering": ['WebFiltering.WebFiltering', 'WebFiltering.WebFiltering'],
    "web-filtering-mapping": ['WebFiltering.WebFilteringMapping', 'WebFiltering.WebFilteringMapping'],

    "admin": ['Admin', 'Admin'],

    "app-version": ['AppVersion', 'AppVersion'],

    "super-class": ['ClassificationSuperClass', 'ClassificationSuperClass'],

    "content-class": ['ContentClassification', 'ContentClassification'],

    "device-class": ['DeviceClassification', 'DeviceClassification'],

    "feature-table": ['FeatureTable', 'FeatureTable'],

    "hardware": ['Hardware', 'Hardware'],

    "ip-class": ['IpClassification', 'IpClassification'],

    "keys": ['KeysTable', 'KeysTable'],

    "organization": ['Organization', 'Organization'],

    "os-table": ['OsTable', 'OsTable'],

    "reporting": ['Reporting', 'Reporting'],

    "token-auth": ['TokenAuth', 'TokenAuth'],

    "user-auth": ['UserAuthentication', 'UserAuthentication'],

    "user-hardware-restrict": ['UserHardwareRestrict', 'UserHardwareRestrictSerializer'],

    "users": ["Users", "Users"]
}

# Columns of the Table in UI

# USER COLUMN
user_column = [
    {"dataIndex": "name", "title": "Name", "align": "center"},
    {"dataIndex": "phone", "title": "Phone Number", "align": "center"},
    {"dataIndex": "email", "title": "Email Address", "align": "center"},
    {"dataIndex": "dob", "title": "Date of Birth", "align": "center"},
    {"dataIndex": "user_auth_username", "title": "Username", "align": "center"},
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


# GET API

def get_data(models, page, rows, org_id, user_id, auth_trail, field="key", order="1", column=None, val=None, types=None):

    # PAGINATION ROWS AND COLUMNS
    keys = org_id
    val1 = rows * (page - 1)
    val2 = (val1 + rows)

    # COLUMN ASSIGNING AS PER MODEL
    if models == "admin" and types == "admin_column":
        col = admin_column

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
        serializer = my_import('epsapp.serializers.' + dictionary[models][1])
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
