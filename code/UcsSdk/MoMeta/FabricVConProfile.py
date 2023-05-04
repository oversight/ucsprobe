import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricVConProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricVConProfile")

	@staticmethod
	def ClassId():
		return "fabricVConProfile"

	DESCR = "Descr"
	DN = "Dn"
	MEZZ_MAPPING = "MezzMapping"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_MEZZ_MAPPING_LINEAR_ORDERED = "linear-ordered"
	CONST_MEZZ_MAPPING_LINEAR_ORDERED_TO_ROUND_ROBIN = "linear-ordered-to-round-robin"
	CONST_MEZZ_MAPPING_ROUND_ROBIN = "round-robin"
	CONST_MEZZ_MAPPING_ROUND_ROBIN_TO_LINEAR_ORDERED = "round-robin-to-linear-ordered"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
