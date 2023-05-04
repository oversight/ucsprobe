import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IqnpoolTransportBlock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IqnpoolTransportBlock")

	@staticmethod
	def ClassId():
		return "iqnpoolTransportBlock"

	DN = "Dn"
	FROM = "From"
	RN = "Rn"
	STATUS = "Status"
	SUFFIX = "Suffix"
	TO = "To"

