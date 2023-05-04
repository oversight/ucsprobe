import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIpV4History(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIpV4History")

	@staticmethod
	def ClassId():
		return "vnicIpV4History"

	DN = "Dn"
	OLD_IP_V4_ADDR = "OldIpV4Addr"
	RN = "Rn"
	STATUS = "Status"

