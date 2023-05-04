import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfProcessorPrefetchConfig(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfProcessorPrefetchConfig")

	@staticmethod
	def ClassId():
		return "biosVfProcessorPrefetchConfig"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ADJACENT_CACHE_LINE_PREFETCHER = "VpAdjacentCacheLinePrefetcher"
	VP_DCUIPPREFETCHER = "VpDCUIPPrefetcher"
	VP_DCUSTREAMER_PREFETCH = "VpDCUStreamerPrefetch"
	VP_HARDWARE_PREFETCHER = "VpHardwarePrefetcher"

	CONST_VP_ADJACENT_CACHE_LINE_PREFETCHER_DISABLED = "disabled"
	CONST_VP_ADJACENT_CACHE_LINE_PREFETCHER_ENABLED = "enabled"
	CONST_VP_ADJACENT_CACHE_LINE_PREFETCHER_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ADJACENT_CACHE_LINE_PREFETCHER_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_DCUIPPREFETCHER_DISABLED = "disabled"
	CONST_VP_DCUIPPREFETCHER_ENABLED = "enabled"
	CONST_VP_DCUIPPREFETCHER_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_DCUIPPREFETCHER_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_DCUSTREAMER_PREFETCH_DISABLED = "disabled"
	CONST_VP_DCUSTREAMER_PREFETCH_ENABLED = "enabled"
	CONST_VP_DCUSTREAMER_PREFETCH_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_DCUSTREAMER_PREFETCH_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_HARDWARE_PREFETCHER_DISABLED = "disabled"
	CONST_VP_HARDWARE_PREFETCHER_ENABLED = "enabled"
	CONST_VP_HARDWARE_PREFETCHER_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_HARDWARE_PREFETCHER_PLATFORM_RECOMMENDED = "platform-recommended"
