import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IqnpoolBlock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IqnpoolBlock")

	@staticmethod
	def ClassId():
		return "iqnpoolBlock"

	DN = "Dn"
	FROM = "From"
	RN = "Rn"
	STATUS = "Status"
	SUFFIX = "Suffix"
	TO = "To"

