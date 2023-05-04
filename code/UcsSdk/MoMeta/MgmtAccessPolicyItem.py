import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtAccessPolicyItem(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtAccessPolicyItem")

	@staticmethod
	def ClassId():
		return "mgmtAccessPolicyItem"

	DESCR = "Descr"
	DN = "Dn"
	IP_POOL_NAME = "IpPoolName"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SUBJECT = "Subject"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SUBJECT_ADAPTOR = "adaptor"
	CONST_SUBJECT_BLADE = "blade"
	CONST_SUBJECT_BOARD_CONTROLLER = "board-controller"
	CONST_SUBJECT_CHASSIS = "chassis"
	CONST_SUBJECT_IOCARD = "iocard"
	CONST_SUBJECT_SWITCH = "switch"
	CONST_SUBJECT_SYSTEM = "system"
	CONST_SUBJECT_UNKNOWN = "unknown"
