import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FaultLocalTypedHolder(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FaultLocalTypedHolder")

	@staticmethod
	def ClassId():
		return "faultLocalTypedHolder"

	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TOTAL_FAULTS = "TotalFaults"
	TYPE = "Type"

	CONST_TYPE_ANY = "any"
	CONST_TYPE_CONFIGURATION = "configuration"
	CONST_TYPE_CONNECTIVITY = "connectivity"
	CONST_TYPE_ENVIRONMENTAL = "environmental"
	CONST_TYPE_EQUIPMENT = "equipment"
	CONST_TYPE_FSM = "fsm"
	CONST_TYPE_GENERIC = "generic"
	CONST_TYPE_MANAGEMENT = "management"
	CONST_TYPE_NETWORK = "network"
	CONST_TYPE_OPERATIONAL = "operational"
	CONST_TYPE_SECURITY = "security"
	CONST_TYPE_SERVER = "server"
	CONST_TYPE_SYSDEBUG = "sysdebug"
