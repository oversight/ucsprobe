import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentLocalDiskDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentLocalDiskDef")

	@staticmethod
	def ClassId():
		return "equipmentLocalDiskDef"

	BLOCK_SIZE = "BlockSize"
	CACHE_SIZE = "CacheSize"
	CAPACITY = "Capacity"
	DESCR = "Descr"
	DN = "Dn"
	FORCE_UPDATE_VERSION = "ForceUpdateVersion"
	LINK_SPEED = "LinkSpeed"
	NAME = "Name"
	NUMBER_OF_BLOCKS = "NumberOfBlocks"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	ROTATIONAL_SPEED = "RotationalSpeed"
	SEEK_AVERAGE_READ_WRITE = "SeekAverageReadWrite"
	SEEK_TRACK_TO_TRACK_READ_WRITE = "SeekTrackToTrackReadWrite"
	STATUS = "Status"
	TECHNOLOGY = "Technology"

	CONST_FORCE_UPDATE_VERSION_FALSE = "false"
	CONST_FORCE_UPDATE_VERSION_NO = "no"
	CONST_FORCE_UPDATE_VERSION_TRUE = "true"
	CONST_FORCE_UPDATE_VERSION_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TECHNOLOGY_HDD = "HDD"
	CONST_TECHNOLOGY_SSD = "SSD"
	CONST_TECHNOLOGY_UNSPECIFIED = "unspecified"
