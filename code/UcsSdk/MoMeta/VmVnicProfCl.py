import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmVnicProfCl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmVnicProfCl")

	@staticmethod
	def ClassId():
		return "vmVnicProfCl"

	DC_NAME = "DcName"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	ORG_PATH = "OrgPath"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SW_NAME = "SwName"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
