import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyPolicyScopeCont(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyPolicyScopeCont")

	@staticmethod
	def ClassId():
		return "policyPolicyScopeCont"

	APP_TYPE = "AppType"
	DN = "Dn"
	GEN_NUM = "GenNum"
	NEED_RECOVERY = "NeedRecovery"
	RN = "Rn"
	STATUS = "Status"

	CONST_NEED_RECOVERY_FALSE = "false"
	CONST_NEED_RECOVERY_NO = "no"
	CONST_NEED_RECOVERY_TRUE = "true"
	CONST_NEED_RECOVERY_YES = "yes"
