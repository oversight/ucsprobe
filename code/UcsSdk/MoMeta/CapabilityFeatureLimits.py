import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CapabilityFeatureLimits(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CapabilityFeatureLimits")

	@staticmethod
	def ClassId():
		return "capabilityFeatureLimits"

	DESCR = "Descr"
	DN = "Dn"
	FEATURE_STATUS = "FeatureStatus"
	LIMIT = "Limit"
	NAME = "Name"
	PLATFORM = "Platform"
	RN = "Rn"
	STATUS = "Status"

	CONST_FEATURE_STATUS_SUPPORTED = "supported"
	CONST_FEATURE_STATUS_UNSUPPORTED = "unsupported"
	CONST_PLATFORM_UCS6100 = "ucs6100"
	CONST_PLATFORM_UCS6200 = "ucs6200"
