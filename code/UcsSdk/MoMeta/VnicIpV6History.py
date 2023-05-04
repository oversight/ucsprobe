import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIpV6History(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIpV6History")

	@staticmethod
	def ClassId():
		return "vnicIpV6History"

	DN = "Dn"
	OLD_IP_V6_ADDR = "OldIpV6Addr"
	RN = "Rn"
	STATUS = "Status"

