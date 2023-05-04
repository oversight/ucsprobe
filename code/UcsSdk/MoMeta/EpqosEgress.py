import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EpqosEgress(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EpqosEgress")

	@staticmethod
	def ClassId():
		return "epqosEgress"

	BURST = "Burst"
	DN = "Dn"
	HOST_CONTROL = "HostControl"
	NAME = "Name"
	OPER_PRIO = "OperPrio"
	PRIO = "Prio"
	RATE = "Rate"
	RN = "Rn"
	STATUS = "Status"

	CONST_HOST_CONTROL_FULL = "full"
	CONST_HOST_CONTROL_FULL_WITH_EXCEPTION = "full-with-exception"
	CONST_HOST_CONTROL_NONE = "none"
	CONST_OPER_PRIO_BEST_EFFORT = "best-effort"
	CONST_OPER_PRIO_BRONZE = "bronze"
	CONST_OPER_PRIO_FC = "fc"
	CONST_OPER_PRIO_GOLD = "gold"
	CONST_OPER_PRIO_PLATINUM = "platinum"
	CONST_OPER_PRIO_SILVER = "silver"
	CONST_PRIO_BEST_EFFORT = "best-effort"
	CONST_PRIO_BRONZE = "bronze"
	CONST_PRIO_FC = "fc"
	CONST_PRIO_GOLD = "gold"
	CONST_PRIO_PLATINUM = "platinum"
	CONST_PRIO_SILVER = "silver"
	CONST_RATE_LINE_RATE = "line-rate"
