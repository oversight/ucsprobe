import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfAssertNMIOnSERR(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfAssertNMIOnSERR")

	@staticmethod
	def ClassId():
		return "biosVfAssertNMIOnSERR"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ASSERT_NMION_SERR = "VpAssertNMIOnSERR"

	CONST_VP_ASSERT_NMION_SERR_DISABLED = "disabled"
	CONST_VP_ASSERT_NMION_SERR_ENABLED = "enabled"
	CONST_VP_ASSERT_NMION_SERR_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ASSERT_NMION_SERR_PLATFORM_RECOMMENDED = "platform-recommended"
