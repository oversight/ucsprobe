import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class OsAgent(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"OsAgent")

	@staticmethod
	def ClassId():
		return "osAgent"

	DN = "Dn"
	LAST_CMD = "LastCmd"
	LAST_EVT = "LastEvt"
	LAST_EVT_TS = "LastEvtTs"
	PREV_CMD = "PrevCmd"
	PREV_EVT = "PrevEvt"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VENDOR = "Vendor"
	VERSION = "Version"

	CONST_LAST_CMD_NONE = "none"
	CONST_LAST_EVT_NONE = "none"
	CONST_PREV_CMD_NONE = "none"
	CONST_PREV_EVT_NONE = "none"
	CONST_TYPE_HOST_AGENT = "hostAgent"
	CONST_TYPE_INDETERMINATE = "indeterminate"
	CONST_TYPE_PNUOS_AGENT = "pnuosAgent"
