import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class UuidpoolBlock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"UuidpoolBlock")

	@staticmethod
	def ClassId():
		return "uuidpoolBlock"

	DN = "Dn"
	FROM = "From"
	RN = "Rn"
	STATUS = "Status"
	TO = "To"

