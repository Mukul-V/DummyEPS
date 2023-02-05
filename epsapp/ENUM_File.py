from enum import Enum


# Error Codes
class response_code(Enum):
    ERR_SUCCESS = 1  # "Login Successfully"
    ERR_KEY_GRACE = 2  # "Key is in Grace"
    ERR_GET_CONFIG = 3  # "Ask for the configuration"
    ERR_KEY_ALREADY_USED = 4  # "Key is Already in Use"
    ERR_KEY_EXPIRE = 5  # "Key is Expired"
    ERR_LOGIN_FAIL = 6  # "Login Failed due to invalid credentials"
    ERR_HARDWARE_INVALID = 7  # "hardware is invalid"
    ERR_HARDWARE_RESTRICTED = 8  # "Restricted Hardware Found"
    ERR_OS_RESTRICTED = 9  # "Restricted Operating System Found"
    ERR_MAC_ADDRESS_RESTRICTED = 10  # "Restricted Mac Address Found"
    ERR_KEY_INVALID = 11  # "Invalid Key"
    ERR_KEY_BLOCKED = 12  # "Key Blocked"
    ERR_KEY_REQUIRED = 13  # "Key needs to pass in request"
    ERR_USER_INVALID = 14  # "Username or Password is not Valid"
    ERR_OS_NOT_FOUND = 15  # OS not found in request
    ERR_MAC_NOT_FOUND = 16  # Mac Address not found in request
    ERR_HARDWARE_NOT_FOUND = 17  # Hardware not found in request


class created_by(Enum):
    PREDEFINED = 0  # Predefined configurations
    CUSTOM = 1  # Custom Configurations (created by admin)


class action(Enum):
    BLOCK = 1  # Predefined configurations
    ALLOW = 2  # Custom Configurations (created by admin)
    READONLY = 3  # Custom Configurations (created by admin)  # USB Storage in Device Control Policy
    ALLOWBUTREPORT = 4  #


class device_type(Enum):
    USB_STG = 1  # USB device type
    SERIAL_PORT = 2  # Serial Ports
    PORTABLE_DEVICE = 3  # Portable Devices
    WEBCAM = 4  # Webcam
    PRINTER = 5  # Printer


class file_type(Enum):
    TXT = 1
    DOC = 2
    PDF = 3
    XLS = 4
    PPT = 5


class file_data_part_match_relation(Enum):
    OR = 0
    AND = 1


class file_validation_type(Enum):
    REGEX = 1
    FILE = 2


class schedule_type(Enum):
    FOREVER = 1
    ON_TIME = 2


class audit_type(Enum):
    TASK_SUCCESS = "TASK SUCCESS"
    TASK_FAILED = "TASK FAILED"


class audit_action(Enum):
    CREATE_RECORD = "CREATE_RECORD"
    UPDATE_RECORD = "UPDATE_RECORD"
    DELETE_RECORD = "DELETE_RECORD"


class Rule_Position(Enum):
    TOP = 1
    BOTTOM = 0


class Days(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class Channel(Enum):
    WEB = 1,  # Web
    EMAIL = 2,  # Email
    APP = 3,  # App
    PRINTER = 4,  # Printer
    NETWORK = 5  # Network

