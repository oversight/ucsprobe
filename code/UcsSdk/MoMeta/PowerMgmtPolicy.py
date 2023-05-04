import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerMgmtPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerMgmtPolicy")

	@staticmethod
	def ClassId():
		return "powerMgmtPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	STYLE = "Style"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_STYLE_INTELLIGENT_POLICY_DRIVEN = "intelligent-policy-driven"
	CONST_STYLE_MANUAL_PER_BLADE = "manual-per-blade"
