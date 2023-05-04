import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfPSTATECoordination(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfPSTATECoordination")

	@staticmethod
	def ClassId():
		return "biosVfPSTATECoordination"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PSTATECOORDINATION = "VpPSTATECoordination"

	CONST_VP_PSTATECOORDINATION_HW_ALL = "hw-all"
	CONST_VP_PSTATECOORDINATION_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PSTATECOORDINATION_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_PSTATECOORDINATION_SW_ALL = "sw-all"
	CONST_VP_PSTATECOORDINATION_SW_ANY = "sw-any"
