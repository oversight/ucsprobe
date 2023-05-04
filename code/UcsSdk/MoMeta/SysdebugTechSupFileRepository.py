import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugTechSupFileRepository(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugTechSupFileRepository")

	@staticmethod
	def ClassId():
		return "sysdebugTechSupFileRepository"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

