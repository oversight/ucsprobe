import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyCentraleSync(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyCentraleSync")

	@staticmethod
	def ClassId():
		return "policyCentraleSync"

	DN = "Dn"
	LEFT_DATA = "LeftData"
	RIGHT_DATA = "RightData"
	RN = "Rn"
	STATUS = "Status"

