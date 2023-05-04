import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentXcvr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentXcvr")

	@staticmethod
	def ClassId():
		return "equipmentXcvr"

	DN = "Dn"
	ID = "Id"
	MODEL = "Model"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	TS = "Ts"
	TYPE = "Type"
	VENDOR = "Vendor"

	CONST_TYPE_10GBASEER = "10gbaseer"
	CONST_TYPE_10GBASELR = "10gbaselr"
	CONST_TYPE_10GBASELRM = "10gbaselrm"
	CONST_TYPE_10GBASESR = "10gbasesr"
	CONST_TYPE_CWDM1471 = "cwdm1471"
	CONST_TYPE_CWDM1531 = "cwdm1531"
	CONST_TYPE_CWDM1551 = "cwdm1551"
	CONST_TYPE_FET = "fet"
	CONST_TYPE_H10GCU1M = "h10gcu1m"
	CONST_TYPE_H10GCU3M = "h10gcu3m"
	CONST_TYPE_H10GCU5M = "h10gcu5m"
	CONST_TYPE_H10GCU7M = "h10gcu7m"
	CONST_TYPE_H10GLRMSM = "h10glrmsm"
	CONST_TYPE_H10GUSR = "h10gusr"
	CONST_TYPE_SFP = "sfp"
	CONST_TYPE_UNKNOWN = "unknown"
	CONST_TYPE_X2 = "x2"
