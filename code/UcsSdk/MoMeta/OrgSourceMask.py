import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class OrgSourceMask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"OrgSourceMask")

	@staticmethod
	def ClassId():
		return "orgSourceMask"

	DN = "Dn"
	MASK = "Mask"
	RN = "Rn"
	STATUS = "Status"

