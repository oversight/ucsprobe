import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentRaidDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentRaidDef")

	@staticmethod
	def ClassId():
		return "equipmentRaidDef"

	DESCR = "Descr"
	DN = "Dn"
	LEVEL = "Level"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_LEVEL_ANY_CONFIGURATION = "any-configuration"
	CONST_LEVEL_BEST_EFFORT_MIRRORED = "best-effort-mirrored"
	CONST_LEVEL_BEST_EFFORT_MIRRORED_STRIPED = "best-effort-mirrored-striped"
	CONST_LEVEL_BEST_EFFORT_STRIPED = "best-effort-striped"
	CONST_LEVEL_BEST_EFFORT_STRIPED_DUAL_PARITY = "best-effort-striped-dual-parity"
	CONST_LEVEL_BEST_EFFORT_STRIPED_PARITY = "best-effort-striped-parity"
	CONST_LEVEL_DUAL_DISK = "dual-disk"
	CONST_LEVEL_NO_LOCAL_STORAGE = "no-local-storage"
	CONST_LEVEL_NO_RAID = "no-raid"
	CONST_LEVEL_RAID_MIRRORED = "raid-mirrored"
	CONST_LEVEL_RAID_MIRRORED_STRIPED = "raid-mirrored-striped"
	CONST_LEVEL_RAID_STRIPED = "raid-striped"
	CONST_LEVEL_RAID_STRIPED_DUAL_PARITY = "raid-striped-dual-parity"
	CONST_LEVEL_RAID_STRIPED_DUAL_PARITY_STRIPED = "raid-striped-dual-parity-striped"
	CONST_LEVEL_RAID_STRIPED_PARITY = "raid-striped-parity"
	CONST_LEVEL_RAID_STRIPED_PARITY_STRIPED = "raid-striped-parity-striped"
	CONST_LEVEL_SINGLE_DISK = "single-disk"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
