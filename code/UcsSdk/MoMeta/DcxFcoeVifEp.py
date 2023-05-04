import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DcxFcoeVifEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DcxFcoeVifEp")

	@staticmethod
	def ClassId():
		return "dcxFcoeVifEp"

	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"

