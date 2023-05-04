import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class QosclassFc(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"QosclassFc")

	@staticmethod
	def ClassId():
		return "qosclassFc"

	ADMIN_STATE = "AdminState"
	BW_PERCENT = "BwPercent"
	COS = "Cos"
	DN = "Dn"
	DROP = "Drop"
	MTU = "Mtu"
	NAME = "Name"
	PRIORITY = "Priority"
	RN = "Rn"
	STATUS = "Status"
	WEIGHT = "Weight"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_BW_PERCENT_NOT_APPLICABLE = "not-applicable"
	CONST_COS_ANY = "any"
	CONST_DROP_DROP = "drop"
	CONST_DROP_NO_DROP = "no-drop"
	CONST_MTU_FC = "fc"
	CONST_MTU_NORMAL = "normal"
	CONST_PRIORITY_BEST_EFFORT = "best-effort"
	CONST_PRIORITY_BRONZE = "bronze"
	CONST_PRIORITY_FC = "fc"
	CONST_PRIORITY_GOLD = "gold"
	CONST_PRIORITY_PLATINUM = "platinum"
	CONST_PRIORITY_SILVER = "silver"
	CONST_WEIGHT_BEST_EFFORT = "best-effort"
	CONST_WEIGHT_NONE = "none"
