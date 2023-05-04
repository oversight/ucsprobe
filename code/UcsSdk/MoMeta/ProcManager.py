import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcManager(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcManager")

	@staticmethod
	def ClassId():
		return "procManager"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

