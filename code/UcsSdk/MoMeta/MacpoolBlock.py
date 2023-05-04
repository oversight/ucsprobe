import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MacpoolBlock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MacpoolBlock")

	@staticmethod
	def ClassId():
		return "macpoolBlock"

	DN = "Dn"
	FROM = "From"
	RN = "Rn"
	STATUS = "Status"
	TO = "To"

