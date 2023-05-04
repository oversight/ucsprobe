import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwatTrigger(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwatTrigger")

	@staticmethod
	def ClassId():
		return "swatTrigger"

	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_AND = "AND"
	CONST_TYPE_OR = "OR"
