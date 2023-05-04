import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwatCondition(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwatCondition")

	@staticmethod
	def ClassId():
		return "swatCondition"

	DN = "Dn"
	OPERATION = "Operation"
	RN = "Rn"
	STATUS = "Status"
	VAR_NAME = "VarName"
	VAR_VALUE = "VarValue"

	CONST_OPERATION_EQ = "EQ"
	CONST_OPERATION_GE = "GE"
	CONST_OPERATION_GT = "GT"
	CONST_OPERATION_LE = "LE"
	CONST_OPERATION_LT = "LT"
	CONST_OPERATION_NE = "NE"
