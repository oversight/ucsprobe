import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FcpoolBlock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FcpoolBlock")

	@staticmethod
	def ClassId():
		return "fcpoolBlock"

	DN = "Dn"
	FROM = "From"
	RN = "Rn"
	STATUS = "Status"
	TO = "To"

