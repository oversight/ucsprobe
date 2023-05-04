import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosRef")

	@staticmethod
	def ClassId():
		return "biosRef"

	DN = "Dn"
	IS_SUPPORTED = "IsSupported"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_YES = "yes"
