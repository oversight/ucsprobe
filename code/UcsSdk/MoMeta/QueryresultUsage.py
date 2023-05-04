import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class QueryresultUsage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"QueryresultUsage")

	@staticmethod
	def ClassId():
		return "queryresultUsage"

	CLASS_TYPE = "ClassType"
	DN = "Dn"
	IS_SERVICE_TEMPLATE = "IsServiceTemplate"
	POLICY_OWNER = "PolicyOwner"
	REF_CONVERTED_DN = "RefConvertedDn"
	REF_DN = "RefDn"
	REF_NAME = "RefName"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SERVICE_TEMPLATE_FALSE = "false"
	CONST_IS_SERVICE_TEMPLATE_NO = "no"
	CONST_IS_SERVICE_TEMPLATE_TRUE = "true"
	CONST_IS_SERVICE_TEMPLATE_YES = "yes"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
