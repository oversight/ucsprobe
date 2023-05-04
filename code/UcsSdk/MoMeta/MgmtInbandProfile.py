import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtInbandProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtInbandProfile")

	@staticmethod
	def ClassId():
		return "mgmtInbandProfile"

	DEFAULT_VLAN_NAME = "DefaultVlanName"
	DN = "Dn"
	NAME = "Name"
	POOL_NAME = "PoolName"
	RN = "Rn"
	STATUS = "Status"

