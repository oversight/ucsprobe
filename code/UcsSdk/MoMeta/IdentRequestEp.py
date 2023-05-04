import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IdentRequestEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IdentRequestEp")

	@staticmethod
	def ClassId():
		return "identRequestEp"

	DN = "Dn"
	REQ_DN = "ReqDn"
	REQ_ID = "ReqId"
	RN = "Rn"
	STATUS = "Status"

