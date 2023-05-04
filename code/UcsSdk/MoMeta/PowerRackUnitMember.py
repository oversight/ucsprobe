import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerRackUnitMember(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerRackUnitMember")

	@staticmethod
	def ClassId():
		return "powerRackUnitMember"

	DN = "Dn"
	ID = "Id"
	OPER_STATE = "OperState"
	RN = "Rn"
	STATUS = "Status"

	CONST_OPER_STATE_CAP_INSUFFICIENT = "cap-insufficient"
	CONST_OPER_STATE_CAP_OK = "cap-ok"
	CONST_OPER_STATE_FW_MISMATCH = "fw-mismatch"
	CONST_OPER_STATE_PSU_INSUFFICIENT = "psu-insufficient"
	CONST_OPER_STATE_PSU_REDUNDANCY_FAILED = "psu-redundancy-failed"
	CONST_OPER_STATE_UNINITIALIZED = "uninitialized"
