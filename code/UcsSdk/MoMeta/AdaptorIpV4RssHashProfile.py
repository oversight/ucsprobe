import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorIpV4RssHashProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorIpV4RssHashProfile")

	@staticmethod
	def ClassId():
		return "adaptorIpV4RssHashProfile"

	DN = "Dn"
	IP_HASH = "IpHash"
	RN = "Rn"
	STATUS = "Status"
	TCP_HASH = "TcpHash"

	CONST_IP_HASH_DISABLED = "disabled"
	CONST_IP_HASH_ENABLED = "enabled"
	CONST_TCP_HASH_DISABLED = "disabled"
	CONST_TCP_HASH_ENABLED = "enabled"
