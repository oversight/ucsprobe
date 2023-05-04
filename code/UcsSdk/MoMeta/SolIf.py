import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SolIf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SolIf")

	@staticmethod
	def ClassId():
		return "solIf"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SPEED = "Speed"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLE = "disable"
	CONST_ADMIN_STATE_ENABLE = "enable"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SPEED_115200 = "115200"
	CONST_SPEED_19200 = "19200"
	CONST_SPEED_38400 = "38400"
	CONST_SPEED_57600 = "57600"
	CONST_SPEED_9600 = "9600"
