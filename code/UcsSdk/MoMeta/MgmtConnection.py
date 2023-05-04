import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtConnection(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtConnection")

	@staticmethod
	def ClassId():
		return "mgmtConnection"

	ACK = "Ack"
	DN = "Dn"
	OPER_STATE = "OperState"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ACK_ACKNOWLEDGED = "acknowledged"
	CONST_ACK_UN_INITIALIZED = "un-initialized"
	CONST_ACK_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
	CONST_OPER_STATE_ACKNOWLEDGED = "acknowledged"
	CONST_OPER_STATE_UN_INITIALIZED = "un-initialized"
	CONST_OPER_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
	CONST_TYPE_SHARED_LOM = "shared-lom"
	CONST_TYPE_SIDEBAND = "sideband"
	CONST_TYPE_UNSPECIFIED = "unspecified"
