import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TopSystem(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"TopSystem")

	@staticmethod
	def ClassId():
		return "topSystem"

	ADDRESS = "Address"
	CURRENT_TIME = "CurrentTime"
	DESCR = "Descr"
	DN = "Dn"
	IPV6_ADDR = "Ipv6Addr"
	MODE = "Mode"
	NAME = "Name"
	OWNER = "Owner"
	RN = "Rn"
	SITE = "Site"
	STATUS = "Status"
	SYSTEM_UP_TIME = "SystemUpTime"

	CONST_MODE_CLUSTER = "cluster"
	CONST_MODE_STAND_ALONE = "stand-alone"
	CONST_MODE_UNSPECIFIED = "unspecified"
