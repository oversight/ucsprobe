import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DhcpAcquired(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DhcpAcquired")

	@staticmethod
	def ClassId():
		return "dhcpAcquired"

	ACQTS = "Acqts"
	COOKIE = "Cookie"
	DN = "Dn"
	ENDS = "Ends"
	IP = "Ip"
	MAC = "Mac"
	RN = "Rn"
	STATUS = "Status"
	SYS_ID = "SysId"

