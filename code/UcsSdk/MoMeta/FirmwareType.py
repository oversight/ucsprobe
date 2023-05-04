import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareType(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareType")

	@staticmethod
	def ClassId():
		return "firmwareType"

	DN = "Dn"
	EP = "Ep"
	INV_TAG = "InvTag"
	MAX_VER = "MaxVer"
	MIN_VER = "MinVer"
	RN = "Rn"
	STATUS = "Status"

	CONST_EP_ADAPTOR = "adaptor"
	CONST_EP_BLADE_BIOS = "blade-bios"
	CONST_EP_BLADE_CONTROLLER = "blade-controller"
	CONST_EP_BOARD_CONTROLLER = "board-controller"
	CONST_EP_CATALOG = "catalog"
	CONST_EP_DEBUG_PLUG_IN = "debug-plug-in"
	CONST_EP_DIAG = "diag"
	CONST_EP_FEX = "fex"
	CONST_EP_FLEXFLASH_CONTROLLER = "flexflash-controller"
	CONST_EP_GRAPHICS_CARD = "graphics-card"
	CONST_EP_HOST_HBA = "host-hba"
	CONST_EP_HOST_HBA_OPTIONROM = "host-hba-optionrom"
	CONST_EP_HOST_NIC = "host-nic"
	CONST_EP_HOST_NIC_OPTIONROM = "host-nic-optionrom"
	CONST_EP_IOCARD = "iocard"
	CONST_EP_LOCAL_DISK = "local-disk"
	CONST_EP_MGMT_EXT = "mgmt-ext"
	CONST_EP_STORAGE_CONTROLLER = "storage-controller"
	CONST_EP_SWITCH = "switch"
	CONST_EP_SWITCH_KERNEL = "switch-kernel"
	CONST_EP_SWITCH_SOFTWARE = "switch-software"
	CONST_EP_SYSTEM = "system"
	CONST_EP_UNSPECIFIED = "unspecified"
