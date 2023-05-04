import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareBlade(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareBlade")

	@staticmethod
	def ClassId():
		return "firmwareBlade"

	DN = "Dn"
	OPER_VERSION = "OperVersion"
	RN = "Rn"
	STATUS = "Status"

