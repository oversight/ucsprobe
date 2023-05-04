import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIqnHistory(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIqnHistory")

	@staticmethod
	def ClassId():
		return "vnicIqnHistory"

	DN = "Dn"
	OLD_INITIATOR_NAME = "OldInitiatorName"
	RN = "Rn"
	STATUS = "Status"

