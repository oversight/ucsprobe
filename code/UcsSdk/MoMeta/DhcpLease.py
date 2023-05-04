import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DhcpLease(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DhcpLease")

	@staticmethod
	def ClassId():
		return "dhcpLease"

	CLI_ID = "CliId"
	COOKIE = "Cookie"
	DN = "Dn"
	ENDS = "Ends"
	HOSTNAME = "Hostname"
	INTF = "Intf"
	IP = "Ip"
	MAC = "Mac"
	RN = "Rn"
	STARTS = "Starts"
	STATUS = "Status"

