import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaSessionInfoTable(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaSessionInfoTable")

	@staticmethod
	def ClassId():
		return "aaaSessionInfoTable"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

