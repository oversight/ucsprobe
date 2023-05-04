import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class QueryresultDependency(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"QueryresultDependency")

	@staticmethod
	def ClassId():
		return "queryresultDependency"

	CLASS_TYPE = "ClassType"
	DN = "Dn"
	IS_IMPORTABLE = "IsImportable"
	POLICY_OWNER = "PolicyOwner"
	REF_CONVERTED_DN = "RefConvertedDn"
	REF_DN = "RefDn"
	REF_NAME = "RefName"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_IMPORTABLE_FALSE = "false"
	CONST_IS_IMPORTABLE_NO = "no"
	CONST_IS_IMPORTABLE_TRUE = "true"
	CONST_IS_IMPORTABLE_YES = "yes"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
