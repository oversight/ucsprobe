import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeControllerChassis(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeControllerChassis")

	@staticmethod
	def ClassId():
		return "apeControllerChassis"

	DN = "Dn"
	INDEX = "Index"
	RN = "Rn"
	STATUS = "Status"

