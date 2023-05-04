import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfUCSMBootOrderRuleControl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfUCSMBootOrderRuleControl")

	@staticmethod
	def ClassId():
		return "biosVfUCSMBootOrderRuleControl"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_UCSMBOOT_ORDER_RULE = "VpUCSMBootOrderRule"

	CONST_VP_UCSMBOOT_ORDER_RULE_LOOSE = "loose"
	CONST_VP_UCSMBOOT_ORDER_RULE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_UCSMBOOT_ORDER_RULE_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_UCSMBOOT_ORDER_RULE_STRICT = "strict"
