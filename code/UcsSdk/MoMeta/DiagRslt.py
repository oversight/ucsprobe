import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DiagRslt(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DiagRslt")

	@staticmethod
	def ClassId():
		return "diagRslt"

	DESCR = "Descr"
	DN = "Dn"
	END_TS = "EndTs"
	ID = "Id"
	RESULT = "Result"
	RN = "Rn"
	RSLT_STATUS = "RsltStatus"
	START_TS = "StartTs"
	STATUS = "Status"

	CONST_RESULT_FAIL = "fail"
	CONST_RESULT_NA = "na"
	CONST_RESULT_PASS = "pass"
	CONST_RSLT_STATUS_CANCELLED = "cancelled"
	CONST_RSLT_STATUS_COMPLETE = "complete"
	CONST_RSLT_STATUS_FAILED = "failed"
	CONST_RSLT_STATUS_IN_PROGRESS = "in-progress"
	CONST_RSLT_STATUS_NOT_RUN = "not-run"
	CONST_RSLT_STATUS_SCHEDULED = "scheduled"
