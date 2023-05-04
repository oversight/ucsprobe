import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeSdr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeSdr")

	@staticmethod
	def ClassId():
		return "apeSdr"

	DN = "Dn"
	ENTITY_TYPE = "EntityType"
	EVENT_READING_TYPE = "EventReadingType"
	HYSTERISIS_DOWN = "HysterisisDown"
	HYSTERISIS_UP = "HysterisisUp"
	ID = "Id"
	INSTANCE = "Instance"
	NAME = "Name"
	RN = "Rn"
	SENSOR_ID = "SensorId"
	SENSOR_TYPE = "SensorType"
	STATUS = "Status"
	THRESHOLD_LC = "ThresholdLc"
	THRESHOLD_LNC = "ThresholdLnc"
	THRESHOLD_LNR = "ThresholdLnr"
	THRESHOLD_UC = "ThresholdUc"
	THRESHOLD_UNC = "ThresholdUnc"
	THRESHOLD_UNR = "ThresholdUnr"
	TYPE = "Type"
	UNITS = "Units"

	CONST_ENTITY_TYPE_ADD_IN_CARD = "ADD_IN_CARD"
	CONST_ENTITY_TYPE_BACK_PANEL_BOARD = "BACK_PANEL_BOARD"
	CONST_ENTITY_TYPE_BATTERY = "BATTERY"
	CONST_ENTITY_TYPE_BIOS = "BIOS"
	CONST_ENTITY_TYPE_CABLE_INTERCONNECT = "CABLE_INTERCONNECT"
	CONST_ENTITY_TYPE_CHASSIS_BACK_PANEL_BOARD = "CHASSIS_BACK_PANEL_BOARD"
	CONST_ENTITY_TYPE_CMC = "CMC"
	CONST_ENTITY_TYPE_CONNECTIVITY_SWITCH = "CONNECTIVITY_SWITCH"
	CONST_ENTITY_TYPE_COOLING_UNIT = "COOLING_UNIT"
	CONST_ENTITY_TYPE_DEVICE_BAY = "DEVICE_BAY"
	CONST_ENTITY_TYPE_DISK = "DISK"
	CONST_ENTITY_TYPE_DISK_DRIVE_BAY = "DISK_DRIVE_BAY"
	CONST_ENTITY_TYPE_DRIVE_BACKPLANE = "DRIVE_BACKPLANE"
	CONST_ENTITY_TYPE_EXTERNAL_ENVIRONMENT = "EXTERNAL_ENVIRONMENT"
	CONST_ENTITY_TYPE_FAN_COOLING = "FAN_COOLING"
	CONST_ENTITY_TYPE_FRONT_PANEL_BOARD = "FRONT_PANEL_BOARD"
	CONST_ENTITY_TYPE_GROUP = "GROUP"
	CONST_ENTITY_TYPE_IBMC = "IBMC"
	CONST_ENTITY_TYPE_IO_MODULE = "IO_MODULE"
	CONST_ENTITY_TYPE_IPMI_CHANNEL = "IPMI_CHANNEL"
	CONST_ENTITY_TYPE_MEMORY_DEVICE = "MEMORY_DEVICE"
	CONST_ENTITY_TYPE_MEMORY_MODULE = "MEMORY_MODULE"
	CONST_ENTITY_TYPE_MGMT_CONTROLLER_FIRMWARE = "MGMT_CONTROLLER_FIRMWARE"
	CONST_ENTITY_TYPE_OPERATING_SYSTEM = "OPERATING_SYSTEM"
	CONST_ENTITY_TYPE_OTHER = "OTHER"
	CONST_ENTITY_TYPE_OTHER_CHASSIS_BOARD = "OTHER_CHASSIS_BOARD"
	CONST_ENTITY_TYPE_OTHER_SYSTEM_BOARD = "OTHER_SYSTEM_BOARD"
	CONST_ENTITY_TYPE_PCI_BUS = "PCI_BUS"
	CONST_ENTITY_TYPE_PCI_EXPRESS_BUS = "PCI_EXPRESS_BUS"
	CONST_ENTITY_TYPE_PERIPHERAL = "PERIPHERAL"
	CONST_ENTITY_TYPE_PERIPHERAL_BAY = "PERIPHERAL_BAY"
	CONST_ENTITY_TYPE_POWER_MANAGEMENT_BOARD = "POWER_MANAGEMENT_BOARD"
	CONST_ENTITY_TYPE_POWER_MODULE = "POWER_MODULE"
	CONST_ENTITY_TYPE_POWER_SUPPLY = "POWER_SUPPLY"
	CONST_ENTITY_TYPE_POWER_SYSTEM_BOARD = "POWER_SYSTEM_BOARD"
	CONST_ENTITY_TYPE_POWER_UNIT = "POWER_UNIT"
	CONST_ENTITY_TYPE_PROCESSING_BLADE = "PROCESSING_BLADE"
	CONST_ENTITY_TYPE_PROCESSOR = "PROCESSOR"
	CONST_ENTITY_TYPE_PROCESSOR_BOARD = "PROCESSOR_BOARD"
	CONST_ENTITY_TYPE_PROCESSOR_FRONT_SIDE_BUS = "PROCESSOR_FRONT_SIDE_BUS"
	CONST_ENTITY_TYPE_PROCESSOR_IO_MODULE = "PROCESSOR_IO_MODULE"
	CONST_ENTITY_TYPE_PROCESSOR_MEMORY_MODULE = "PROCESSOR_MEMORY_MODULE"
	CONST_ENTITY_TYPE_PROCESSOR_MODULE = "PROCESSOR_MODULE"
	CONST_ENTITY_TYPE_REMOTE_MGMT_COMM_DEVICE = "REMOTE_MGMT_COMM_DEVICE"
	CONST_ENTITY_TYPE_SATA_SAS_BUS = "SATA_SAS_BUS"
	CONST_ENTITY_TYPE_SCSI_BUS = "SCSI_BUS"
	CONST_ENTITY_TYPE_SUB_CHASSIS = "SUB_CHASSIS"
	CONST_ENTITY_TYPE_SYSTEM_BOARD = "SYSTEM_BOARD"
	CONST_ENTITY_TYPE_SYSTEM_BUS = "SYSTEM_BUS"
	CONST_ENTITY_TYPE_SYSTEM_CHASSIS = "SYSTEM_CHASSIS"
	CONST_ENTITY_TYPE_SYSTEM_INTERNAL_EXPANSION_BOARD = "SYSTEM_INTERNAL_EXPANSION_BOARD"
	CONST_ENTITY_TYPE_SYSTEM_MANAGEMENT_MODULE = "SYSTEM_MANAGEMENT_MODULE"
	CONST_ENTITY_TYPE_SYSTEM_MANAGEMENT_SOFTWARE = "SYSTEM_MANAGEMENT_SOFTWARE"
	CONST_ENTITY_TYPE_UNKNOWN = "UNKNOWN"
	CONST_ENTITY_TYPE_UNSPECIFIED = "UNSPECIFIED"
	CONST_EVENT_READING_TYPE_DISCRETE_ACPI_POWER = "DISCRETE_ACPI_POWER"
	CONST_EVENT_READING_TYPE_DISCRETE_AVAILABILITY = "DISCRETE_AVAILABILITY"
	CONST_EVENT_READING_TYPE_DISCRETE_DEVICE_ENABLE = "DISCRETE_DEVICE_ENABLE"
	CONST_EVENT_READING_TYPE_DISCRETE_DEVICE_PRESENCE = "DISCRETE_DEVICE_PRESENCE"
	CONST_EVENT_READING_TYPE_DISCRETE_LIMIT_EXCEEDED = "DISCRETE_LIMIT_EXCEEDED"
	CONST_EVENT_READING_TYPE_DISCRETE_PERFORMANCE_MET = "DISCRETE_PERFORMANCE_MET"
	CONST_EVENT_READING_TYPE_DISCRETE_PREDICTIVE_FAILURE = "DISCRETE_PREDICTIVE_FAILURE"
	CONST_EVENT_READING_TYPE_DISCRETE_REDUNDANCY = "DISCRETE_REDUNDANCY"
	CONST_EVENT_READING_TYPE_DISCRETE_SEVERITY = "DISCRETE_SEVERITY"
	CONST_EVENT_READING_TYPE_DISCRETE_STATE = "DISCRETE_STATE"
	CONST_EVENT_READING_TYPE_DISCRETE_USAGE = "DISCRETE_USAGE"
	CONST_EVENT_READING_TYPE_OEM1 = "OEM1"
	CONST_EVENT_READING_TYPE_SENSOR_SPECIFIC = "SENSOR_SPECIFIC"
	CONST_EVENT_READING_TYPE_THRESHOLD = "THRESHOLD"
	CONST_EVENT_READING_TYPE_UNKNOWN = "UNKNOWN"
	CONST_SENSOR_TYPE_ADD_IN_CARD = "ADD_IN_CARD"
	CONST_SENSOR_TYPE_BATTERY = "BATTERY"
	CONST_SENSOR_TYPE_BOOT_ERROR = "BOOT_ERROR"
	CONST_SENSOR_TYPE_BUTTON = "BUTTON"
	CONST_SENSOR_TYPE_CABLE_INTERCONNECT = "CABLE_INTERCONNECT"
	CONST_SENSOR_TYPE_CHASSIS = "CHASSIS"
	CONST_SENSOR_TYPE_CHIP_SET = "CHIP_SET"
	CONST_SENSOR_TYPE_COOLING_DEVICE = "COOLING_DEVICE"
	CONST_SENSOR_TYPE_CRITICAL_INTERRUPT = "CRITICAL_INTERRUPT"
	CONST_SENSOR_TYPE_CURRENT = "CURRENT"
	CONST_SENSOR_TYPE_DRIVE_SLOT = "DRIVE_SLOT"
	CONST_SENSOR_TYPE_ENTITY_PRESENCE = "ENTITY_PRESENCE"
	CONST_SENSOR_TYPE_EVENT_LOGGING_DISABLED = "EVENT_LOGGING_DISABLED"
	CONST_SENSOR_TYPE_FAN = "FAN"
	CONST_SENSOR_TYPE_FRU_STATE = "FRU_STATE"
	CONST_SENSOR_TYPE_LAN = "LAN"
	CONST_SENSOR_TYPE_MANAGEMENT_SUBSYSTEM_HEALTH = "MANAGEMENT_SUBSYSTEM_HEALTH"
	CONST_SENSOR_TYPE_MEMORY = "MEMORY"
	CONST_SENSOR_TYPE_MICROCONTROLLER_COPROCESSOR = "MICROCONTROLLER_COPROCESSOR"
	CONST_SENSOR_TYPE_MODULE_BOARD = "MODULE_BOARD"
	CONST_SENSOR_TYPE_MONITOR_ASIC_IC = "MONITOR_ASIC_IC"
	CONST_SENSOR_TYPE_OEM1 = "OEM1"
	CONST_SENSOR_TYPE_OEM2 = "OEM2"
	CONST_SENSOR_TYPE_OEM3 = "OEM3"
	CONST_SENSOR_TYPE_OEM4 = "OEM4"
	CONST_SENSOR_TYPE_OEM5 = "OEM5"
	CONST_SENSOR_TYPE_OEM7 = "OEM7"
	CONST_SENSOR_TYPE_OS_BOOT = "OS_BOOT"
	CONST_SENSOR_TYPE_OS_CRITICAL_STOP = "OS_CRITICAL_STOP"
	CONST_SENSOR_TYPE_OTHER_FRU = "OTHER_FRU"
	CONST_SENSOR_TYPE_OTHER_UNITS_BASED_SENSOR = "OTHER_UNITS_BASED_SENSOR"
	CONST_SENSOR_TYPE_PHYSICAL_SECURITY = "PHYSICAL_SECURITY"
	CONST_SENSOR_TYPE_PLATFORM_ALERT = "PLATFORM_ALERT"
	CONST_SENSOR_TYPE_PLATFORM_SECURITY = "PLATFORM_SECURITY"
	CONST_SENSOR_TYPE_POWER_MEMORY_RESIZE = "POWER_MEMORY_RESIZE"
	CONST_SENSOR_TYPE_POWER_SUPPLY = "POWER_SUPPLY"
	CONST_SENSOR_TYPE_POWER_UNIT = "POWER_UNIT"
	CONST_SENSOR_TYPE_PROCESSOR = "PROCESSOR"
	CONST_SENSOR_TYPE_SESSION_AUDIT = "SESSION_AUDIT"
	CONST_SENSOR_TYPE_SLOT_CONNECTOR = "SLOT_CONNECTOR"
	CONST_SENSOR_TYPE_SYSTEM_ACPI_POWER_STATE = "SYSTEM_ACPI_POWER_STATE"
	CONST_SENSOR_TYPE_SYSTEM_BOOT_INITIATED = "SYSTEM_BOOT_INITIATED"
	CONST_SENSOR_TYPE_SYSTEM_EVENT = "SYSTEM_EVENT"
	CONST_SENSOR_TYPE_SYSTEM_FIRMWARE_PROGRESS = "SYSTEM_FIRMWARE_PROGRESS"
	CONST_SENSOR_TYPE_TEMPERATURE = "TEMPERATURE"
	CONST_SENSOR_TYPE_TERMINATOR = "TERMINATOR"
	CONST_SENSOR_TYPE_UNKNOWN = "UNKNOWN"
	CONST_SENSOR_TYPE_VERSION_CHANGE = "VERSION_CHANGE"
	CONST_SENSOR_TYPE_VOLTAGE = "VOLTAGE"
	CONST_SENSOR_TYPE_WATCHDOG_1 = "WATCHDOG_1"
	CONST_SENSOR_TYPE_WATCHDOG_2 = "WATCHDOG_2"
	CONST_TYPE_COMPACT_SENSOR_RECORD = "COMPACT_SENSOR_RECORD"
	CONST_TYPE_FULL_SENSOR_RECORD = "FULL_SENSOR_RECORD"
	CONST_TYPE_UNKNOWN_RECORD = "UNKNOWN_RECORD"
	CONST_UNITS_AMPS = "AMPS"
	CONST_UNITS_BECQUERELS = "BECQUERELS"
	CONST_UNITS_BITS = "BITS"
	CONST_UNITS_BYTES = "BYTES"
	CONST_UNITS_CANDELA = "CANDELA"
	CONST_UNITS_CENTIMETERS = "CENTIMETERS"
	CONST_UNITS_CFM = "CFM"
	CONST_UNITS_CHARACTERS = "CHARACTERS"
	CONST_UNITS_COLLISIONS = "COLLISIONS"
	CONST_UNITS_COLOR_TEMP_DEG_K = "COLOR_TEMP_DEG_K"
	CONST_UNITS_CORRECTABLE_ERRORS = "CORRECTABLE_ERRORS"
	CONST_UNITS_COULOMBS = "COULOMBS"
	CONST_UNITS_CUBIC_CENTIMETERS = "CUBIC_CENTIMETERS"
	CONST_UNITS_CUBIC_FEET = "CUBIC_FEET"
	CONST_UNITS_CUBIC_INCHS = "CUBIC_INCHS"
	CONST_UNITS_CUBIC_METERS = "CUBIC_METERS"
	CONST_UNITS_CYCLES = "CYCLES"
	CONST_UNITS_DAY = "DAY"
	CONST_UNITS_DECIBELS = "DECIBELS"
	CONST_UNITS_DEGREES_C = "DEGREES_C"
	CONST_UNITS_DEGREES_F = "DEGREES_F"
	CONST_UNITS_DEGREES_K = "DEGREES_K"
	CONST_UNITS_DWORDS = "DWORDS"
	CONST_UNITS_DB_A = "DbA"
	CONST_UNITS_DB_C = "DbC"
	CONST_UNITS_ERRORS = "ERRORS"
	CONST_UNITS_FARADS = "FARADS"
	CONST_UNITS_FATAL_ERRORS = "FATAL_ERRORS"
	CONST_UNITS_FEET = "FEET"
	CONST_UNITS_FL_OZ = "FL_OZ"
	CONST_UNITS_FOOT_POUNDS = "FOOT_POUNDS"
	CONST_UNITS_GAUSS = "GAUSS"
	CONST_UNITS_GBITS = "GBITS"
	CONST_UNITS_GBYTES = "GBYTES"
	CONST_UNITS_GILBERTS = "GILBERTS"
	CONST_UNITS_GRAMS = "GRAMS"
	CONST_UNITS_GRAVITIES = "GRAVITIES"
	CONST_UNITS_GRAYS = "GRAYS"
	CONST_UNITS_HENRIES = "HENRIES"
	CONST_UNITS_HITS = "HITS"
	CONST_UNITS_HOUR = "HOUR"
	CONST_UNITS_HZ = "HZ"
	CONST_UNITS_INCHES = "INCHES"
	CONST_UNITS_JOULES = "JOULES"
	CONST_UNITS_KBITS = "KBITS"
	CONST_UNITS_KBYTES = "KBYTES"
	CONST_UNITS_KPA = "KPA"
	CONST_UNITS_LINES = "LINES"
	CONST_UNITS_LITERS = "LITERS"
	CONST_UNITS_LUMENS = "LUMENS"
	CONST_UNITS_LUX = "LUX"
	CONST_UNITS_MBITS = "MBITS"
	CONST_UNITS_MBYTES = "MBYTES"
	CONST_UNITS_MESSAGES = "MESSAGES"
	CONST_UNITS_METERS = "METERS"
	CONST_UNITS_MHENRIES = "MHENRIES"
	CONST_UNITS_MIL = "MIL"
	CONST_UNITS_MILLIMETERS = "MILLIMETERS"
	CONST_UNITS_MINUTE = "MINUTE"
	CONST_UNITS_MISSES = "MISSES"
	CONST_UNITS_MOLES = "MOLES"
	CONST_UNITS_MSECONDS = "MSECONDS"
	CONST_UNITS_NEWTONS = "NEWTONS"
	CONST_UNITS_NITS = "NITS"
	CONST_UNITS_OHMS = "OHMS"
	CONST_UNITS_OUNCES = "OUNCES"
	CONST_UNITS_OUNCE_INCHES = "OUNCE_INCHES"
	CONST_UNITS_OVERRUNS = "OVERRUNS"
	CONST_UNITS_PACKETS = "PACKETS"
	CONST_UNITS_POUNDS = "POUNDS"
	CONST_UNITS_PPM = "PPM"
	CONST_UNITS_PSI = "PSI"
	CONST_UNITS_QWORDS = "QWORDS"
	CONST_UNITS_RADIANS = "RADIANS"
	CONST_UNITS_RESETS = "RESETS"
	CONST_UNITS_RETRIES = "RETRIES"
	CONST_UNITS_REVOLUTIONS = "REVOLUTIONS"
	CONST_UNITS_RPM = "RPM"
	CONST_UNITS_SECONDS = "SECONDS"
	CONST_UNITS_SERADIANS = "SERADIANS"
	CONST_UNITS_SIEMENS = "SIEMENS"
	CONST_UNITS_SIEVERTS = "SIEVERTS"
	CONST_UNITS_UFARADS = "UFARADS"
	CONST_UNITS_UNCORRECTABLE_ERRORS = "UNCORRECTABLE_ERRORS"
	CONST_UNITS_UNDERRUNS = "UNDERRUNS"
	CONST_UNITS_UNSPECIFIED = "UNSPECIFIED"
	CONST_UNITS_USECONDS = "USECONDS"
	CONST_UNITS_VA = "VA"
	CONST_UNITS_VOLTS = "VOLTS"
	CONST_UNITS_WATTS = "WATTS"
	CONST_UNITS_WEEK = "WEEK"
	CONST_UNITS_WORDS = "WORDS"
	CONST_UNITS_RESERVED1 = "reserved1"