import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfScrubPolicies(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfScrubPolicies")

	@staticmethod
	def ClassId():
		return "biosVfScrubPolicies"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_DEMAND_SCRUB = "VpDemandScrub"
	VP_PATROL_SCRUB = "VpPatrolScrub"

	CONST_VP_DEMAND_SCRUB_DISABLED = "disabled"
	CONST_VP_DEMAND_SCRUB_ENABLED = "enabled"
	CONST_VP_DEMAND_SCRUB_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_DEMAND_SCRUB_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_PATROL_SCRUB_DISABLED = "disabled"
	CONST_VP_PATROL_SCRUB_ENABLED = "enabled"
	CONST_VP_PATROL_SCRUB_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PATROL_SCRUB_PLATFORM_RECOMMENDED = "platform-recommended"
