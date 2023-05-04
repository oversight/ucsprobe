import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfSriovConfig(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfSriovConfig")

	@staticmethod
	def ClassId():
		return "biosVfSriovConfig"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_SRIOV = "VpSriov"

	CONST_VP_SRIOV_DISABLED = "disabled"
	CONST_VP_SRIOV_ENABLED = "enabled"
	CONST_VP_SRIOV_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_SRIOV_PLATFORM_RECOMMENDED = "platform-recommended"
