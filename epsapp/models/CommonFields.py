custom_type = (
    (0, 0),  # Predefined
    (1, 1)  # Custom
)

action_type = (
    (1, 1),  # Block
    (2, 2),  # Allow
    (3, 3),  # ReadOnly
    (4, 4)  # AllowButReport
)

class_group_type = (
    (1, 1),  # 1 -> Device_Class
    (2, 2),  # 2 -> App_Class
    (3, 3),  # 3 -> Web_Class
    (4, 4),  # 4 -> File_Class
    (5, 5),  # 5 -> Ip Class
    (6, 6)  # 6 -> Schedule_Class
)

device_type = (
    (1, 1),  # USB Device
    (2, 2),  # Serial Port
    (3, 3),  # Portable Device
    (4, 4),  # Webcam
    (5, 5)  # Printer
)

feature_type = (
    (1, 1),  # GrandParent
    (2, 2),  # Parent
    (3, 3)  # Child
)

file_type = (
    (1, 1),  # TXT
    (2, 2),  # DOC
    (3, 3),  # PDF
    (4, 4),  # XLS
    (5, 5)   # PPT
)

tenure_type = (
    (0, 0),  # Fixed
    (1, 1),  # Days
    (2, 2),  # Weeks
    (3, 3),  # Months
    (4, 4),  # Years
)

key_state = (
    (1, 1),  # Active
    (2, 2),  # In-Active
    (3, 3),  # GracePeriod
    (4, 4),  # Unused
)
