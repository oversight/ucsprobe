import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricVlanPermit(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricVlanPermit")

	@staticmethod
	def ClassId():
		return "fabricVlanPermit"

	CLOUD = "Cloud"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_SWITCH_ID_DUAL = "dual"
