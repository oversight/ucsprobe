import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageLocalDiskConfigPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageLocalDiskConfigPolicy")

	@staticmethod
	def ClassId():
		return "storageLocalDiskConfigPolicy"

	DESCR = "Descr"
	DN = "Dn"
	FLEX_FLASH_RAIDREPORTING_STATE = "FlexFlashRAIDReportingState"
	FLEX_FLASH_STATE = "FlexFlashState"
	MODE = "Mode"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PROTECT_CONFIG = "ProtectConfig"
	RN = "Rn"
	STATUS = "Status"

	CONST_FLEX_FLASH_RAIDREPORTING_STATE_DISABLE = "disable"
	CONST_FLEX_FLASH_RAIDREPORTING_STATE_ENABLE = "enable"
	CONST_FLEX_FLASH_STATE_DISABLE = "disable"
	CONST_FLEX_FLASH_STATE_ENABLE = "enable"
	CONST_INT_ID_NONE = "none"
	CONST_MODE_ANY_CONFIGURATION = "any-configuration"
	CONST_MODE_BEST_EFFORT_MIRRORED = "best-effort-mirrored"
	CONST_MODE_BEST_EFFORT_MIRRORED_STRIPED = "best-effort-mirrored-striped"
	CONST_MODE_BEST_EFFORT_STRIPED = "best-effort-striped"
	CONST_MODE_BEST_EFFORT_STRIPED_DUAL_PARITY = "best-effort-striped-dual-parity"
	CONST_MODE_BEST_EFFORT_STRIPED_PARITY = "best-effort-striped-parity"
	CONST_MODE_DUAL_DISK = "dual-disk"
	CONST_MODE_NO_LOCAL_STORAGE = "no-local-storage"
	CONST_MODE_NO_RAID = "no-raid"
	CONST_MODE_RAID_MIRRORED = "raid-mirrored"
	CONST_MODE_RAID_MIRRORED_STRIPED = "raid-mirrored-striped"
	CONST_MODE_RAID_STRIPED = "raid-striped"
	CONST_MODE_RAID_STRIPED_DUAL_PARITY = "raid-striped-dual-parity"
	CONST_MODE_RAID_STRIPED_DUAL_PARITY_STRIPED = "raid-striped-dual-parity-striped"
	CONST_MODE_RAID_STRIPED_PARITY = "raid-striped-parity"
	CONST_MODE_RAID_STRIPED_PARITY_STRIPED = "raid-striped-parity-striped"
	CONST_MODE_SINGLE_DISK = "single-disk"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTECT_CONFIG_FALSE = "false"
	CONST_PROTECT_CONFIG_NO = "no"
	CONST_PROTECT_CONFIG_TRUE = "true"
	CONST_PROTECT_CONFIG_YES = "yes"
