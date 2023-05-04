import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeReading(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeReading")

	@staticmethod
	def ClassId():
		return "apeReading"

	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	STATE = "State"
	STATUS = "Status"
	VALUE = "Value"

