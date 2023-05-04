import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmDC(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmDC")

	@staticmethod
	def ClassId():
		return "vmDC"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OWN = "Own"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	UUID = "Uuid"

	CONST_INT_ID_NONE = "none"
	CONST_OWN_DISCOVERED = "discovered"
	CONST_OWN_MANAGED = "managed"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
