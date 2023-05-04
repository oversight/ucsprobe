import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeKvmMgmtPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeKvmMgmtPolicy")

	@staticmethod
	def ClassId():
		return "computeKvmMgmtPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	VMEDIA_ENCRYPTION = "VmediaEncryption"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_VMEDIA_ENCRYPTION_DISABLE = "disable"
	CONST_VMEDIA_ENCRYPTION_ENABLE = "enable"
