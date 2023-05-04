import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class UuidpoolUniverse(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"UuidpoolUniverse")

	@staticmethod
	def ClassId():
		return "uuidpoolUniverse"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

