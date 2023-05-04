import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfDirectCacheAccess(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfDirectCacheAccess")

	@staticmethod
	def ClassId():
		return "biosVfDirectCacheAccess"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_DIRECT_CACHE_ACCESS = "VpDirectCacheAccess"

	CONST_VP_DIRECT_CACHE_ACCESS_DISABLED = "disabled"
	CONST_VP_DIRECT_CACHE_ACCESS_ENABLED = "enabled"
	CONST_VP_DIRECT_CACHE_ACCESS_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_DIRECT_CACHE_ACCESS_PLATFORM_RECOMMENDED = "platform-recommended"
