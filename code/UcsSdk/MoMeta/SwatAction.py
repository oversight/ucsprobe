import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwatAction(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwatAction")

	@staticmethod
	def ClassId():
		return "swatAction"

	DN = "Dn"
	EVALUATION_METHOD = "EvaluationMethod"
	INSTANCE_MOD = "InstanceMod"
	INTERVAL = "Interval"
	MAX_HITS = "MaxHits"
	NAME = "Name"
	RN = "Rn"
	SLEEP_DELAY = "SleepDelay"
	STATUS = "Status"
	TYPE = "Type"

	CONST_EVALUATION_METHOD_DETERMINISTIC = "Deterministic"
	CONST_EVALUATION_METHOD_RANDOM = "Random"
	CONST_INSTANCE_MOD_CREATE = "CREATE"
	CONST_INSTANCE_MOD_DELETE = "DELETE"
	CONST_TYPE_CRASH = "CRASH"
	CONST_TYPE_MOD = "MOD"
	CONST_TYPE_RETURN = "RETURN"
	CONST_TYPE_SLEEP = "SLEEP"
