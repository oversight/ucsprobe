import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeScrubPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeScrubPolicy")

	@staticmethod
	def ClassId():
		return "computeScrubPolicy"

	BIOS_SETTINGS_SCRUB = "BiosSettingsScrub"
	DESCR = "Descr"
	DISK_SCRUB = "DiskScrub"
	DN = "Dn"
	FLEX_FLASH_SCRUB = "FlexFlashScrub"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_BIOS_SETTINGS_SCRUB_NO = "no"
	CONST_BIOS_SETTINGS_SCRUB_YES = "yes"
	CONST_DISK_SCRUB_NO = "no"
	CONST_DISK_SCRUB_YES = "yes"
	CONST_FLEX_FLASH_SCRUB_NO = "no"
	CONST_FLEX_FLASH_SCRUB_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
