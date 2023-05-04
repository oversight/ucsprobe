import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorNwMgmtCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorNwMgmtCap")

	@staticmethod
	def ClassId():
		return "adaptorNwMgmtCap"

	API = "Api"
	DN = "Dn"
	MGMT_TRANSPORT = "MgmtTransport"
	MODE = "Mode"
	OPER_POWER_REQUIREMENT = "OperPowerRequirement"
	REBOOT_ACTION_ON_DESTRUCTIVE = "RebootActionOnDestructive"
	RN = "Rn"
	STATUS = "Status"

	CONST_API_MENLO = "menlo"
	CONST_API_NONE = "none"
	CONST_API_PALO = "palo"
	CONST_MGMT_TRANSPORT_L2 = "L2"
	CONST_MGMT_TRANSPORT_L3 = "L3"
	CONST_MODE_FULL = "full"
	CONST_MODE_PARTIAL = "partial"
	CONST_OPER_POWER_REQUIREMENT_FULL = "full"
	CONST_OPER_POWER_REQUIREMENT_NONE = "none"
	CONST_OPER_POWER_REQUIREMENT_STANDBY = "standby"
	CONST_REBOOT_ACTION_ON_DESTRUCTIVE_ADAPTOR = "adaptor"
	CONST_REBOOT_ACTION_ON_DESTRUCTIVE_HOST = "host"
	CONST_REBOOT_ACTION_ON_DESTRUCTIVE_NONE = "none"
