import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeFru(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeFru")

	@staticmethod
	def ClassId():
		return "apeFru"

	BOARD_MANUFACTURER = "BoardManufacturer"
	BOARD_MFG_TIME = "BoardMfgTime"
	BOARD_PART_NO = "BoardPartNo"
	BOARD_PRODUCT_NAME = "BoardProductName"
	BOARD_SERIAL_NO = "BoardSerialNo"
	BOARD_VID = "BoardVid"
	CHASSIS_PART_NO = "ChassisPartNo"
	CHASSIS_SERIAL_NO = "ChassisSerialNo"
	CONTROL_PLANE_MAC1 = "ControlPlaneMac1"
	CONTROL_PLANE_MAC2 = "ControlPlaneMac2"
	DATA_PLANE_MAC1 = "DataPlaneMac1"
	DATA_PLANE_MAC2 = "DataPlaneMac2"
	DATA_PLANE_WWN1 = "DataPlaneWwn1"
	DATA_PLANE_WWN2 = "DataPlaneWwn2"
	DN = "Dn"
	ENTITY_TYPE = "EntityType"
	ID = "Id"
	INSTANCE = "Instance"
	PRODUCT_ASSET_TAG = "ProductAssetTag"
	PRODUCT_MANUFACTURER = "ProductManufacturer"
	PRODUCT_NAME = "ProductName"
	PRODUCT_PART_NO = "ProductPartNo"
	PRODUCT_SERIAL_NO = "ProductSerialNo"
	PRODUCT_VERSION_NO = "ProductVersionNo"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

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