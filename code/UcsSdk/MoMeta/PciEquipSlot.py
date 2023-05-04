import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PciEquipSlot(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PciEquipSlot")

	@staticmethod
	def ClassId():
		return "pciEquipSlot"

	CONTROLLER_REPORTED = "ControllerReported"
	DISCOVERY_STATE = "DiscoveryState"
	DN = "Dn"
	HOST_REPORTED = "HostReported"
	ID = "Id"
	MAC_LEFT = "MacLeft"
	MAC_RIGHT = "MacRight"
	MODEL = "Model"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	SMBIOS_ID = "SmbiosId"
	STATUS = "Status"
	VENDOR = "Vendor"

	CONST_DISCOVERY_STATE_AUTO_UPGRADING = "auto-upgrading"
	CONST_DISCOVERY_STATE_DISCOVERED = "discovered"
	CONST_DISCOVERY_STATE_OFFLINE = "offline"
	CONST_DISCOVERY_STATE_ONLINE = "online"
	CONST_DISCOVERY_STATE_UNKNOWN = "unknown"
	CONST_DISCOVERY_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
