import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageLocalDiskPartition(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageLocalDiskPartition")

	@staticmethod
	def ClassId():
		return "storageLocalDiskPartition"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	ORDER = "Order"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"
	TYPE = "Type"

	CONST_INT_ID_NONE = "none"
	CONST_ORDER_UNSPECIFIED = "unspecified"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SIZE_UNKNOWN = "unknown"
	CONST_TYPE_EXT2 = "ext2"
	CONST_TYPE_EXT3 = "ext3"
	CONST_TYPE_FAT32 = "fat32"
	CONST_TYPE_NONE = "none"
	CONST_TYPE_NTFS = "ntfs"
	CONST_TYPE_SWAP = "swap"
