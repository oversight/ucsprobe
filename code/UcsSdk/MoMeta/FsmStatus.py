import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FsmStatus(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FsmStatus")

	@staticmethod
	def ClassId():
		return "fsmStatus"

	CONVERTED_EP_REF = "ConvertedEpRef"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OBJECT_CLASS_NAME = "ObjectClassName"
	REMOTE_EP_REF = "RemoteEpRef"
	RN = "Rn"
	STATE = "State"
	STATUS = "Status"

	CONST_STATE_FAIL = "fail"
	CONST_STATE_IN_PROGRESS = "inProgress"
	CONST_STATE_NOP = "nop"
	CONST_STATE_PENDING = "pending"
	CONST_STATE_SKIP = "skip"
	CONST_STATE_SUCCESS = "success"
	CONST_STATE_THROTTLED = "throttled"
