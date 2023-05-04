import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareBootDefinition(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareBootDefinition")

	@staticmethod
	def ClassId():
		return "firmwareBootDefinition"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_ADAPTOR = "adaptor"
	CONST_TYPE_BLADE_BIOS = "blade-bios"
	CONST_TYPE_BLADE_CONTROLLER = "blade-controller"
	CONST_TYPE_BOARD_CONTROLLER = "board-controller"
	CONST_TYPE_CATALOG = "catalog"
	CONST_TYPE_DEBUG_PLUG_IN = "debug-plug-in"
	CONST_TYPE_DIAG = "diag"
	CONST_TYPE_FEX = "fex"
	CONST_TYPE_FLEXFLASH_CONTROLLER = "flexflash-controller"
	CONST_TYPE_GRAPHICS_CARD = "graphics-card"
	CONST_TYPE_HOST_HBA = "host-hba"
	CONST_TYPE_HOST_HBA_OPTIONROM = "host-hba-optionrom"
	CONST_TYPE_HOST_NIC = "host-nic"
	CONST_TYPE_HOST_NIC_OPTIONROM = "host-nic-optionrom"
	CONST_TYPE_IOCARD = "iocard"
	CONST_TYPE_LOCAL_DISK = "local-disk"
	CONST_TYPE_MGMT_EXT = "mgmt-ext"
	CONST_TYPE_STORAGE_CONTROLLER = "storage-controller"
	CONST_TYPE_SWITCH = "switch"
	CONST_TYPE_SWITCH_KERNEL = "switch-kernel"
	CONST_TYPE_SWITCH_SOFTWARE = "switch-software"
	CONST_TYPE_SYSTEM = "system"
	CONST_TYPE_UNSPECIFIED = "unspecified"
