import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeMcTable(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeMcTable")

	@staticmethod
	def ClassId():
		return "apeMcTable"

	DN = "Dn"
	ID = "Id"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

