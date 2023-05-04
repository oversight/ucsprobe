import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwatTarget(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwatTarget")

	@staticmethod
	def ClassId():
		return "swatTarget"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VAR_NAME = "VarName"
	VAR_VALUE = "VarValue"

