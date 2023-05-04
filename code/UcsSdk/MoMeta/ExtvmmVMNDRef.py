import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtvmmVMNDRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtvmmVMNDRef")

	@staticmethod
	def ClassId():
		return "extvmmVMNDRef"

	CONFIG_QUALIFIER = "ConfigQualifier"
	DESCR = "Descr"
	DN = "Dn"
	FN_DEF_NAME = "FnDefName"
	FN_NAME = "FnName"
	NAME = "Name"
	OPER_VM_NETWORK_DEF_NAME = "OperVmNetworkDefName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	VM_NETWORK_DEF_NAME = "VmNetworkDefName"

	CONST_CONFIG_QUALIFIER_DUPLICATE_VMND_REFERENCE = "duplicate-vmnd-reference"
	CONST_CONFIG_QUALIFIER_NORMAL = "normal"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
