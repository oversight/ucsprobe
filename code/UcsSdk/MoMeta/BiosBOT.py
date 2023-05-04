import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosBOT(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosBOT")

	@staticmethod
	def ClassId():
		return "biosBOT"

	DN = "Dn"
	LAST_UPDATE = "LastUpdate"
	RN = "Rn"
	STATUS = "Status"

	CONST_LAST_UPDATE_NEVER = "never"
