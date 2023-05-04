import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorLanCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorLanCap")

	@staticmethod
	def ClassId():
		return "adaptorLanCap"

	DEFAULT_VLAN = "DefaultVlan"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

	CONST_DEFAULT_VLAN_DEFAULT_VLAN = "default-vlan"
	CONST_DEFAULT_VLAN_NATIVE_VLAN = "native-vlan"
