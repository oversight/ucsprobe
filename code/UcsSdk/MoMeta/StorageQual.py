import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageQual")

	@staticmethod
	def ClassId():
		return "storageQual"

	BLOCK_SIZE = "BlockSize"
	DISKLESS = "Diskless"
	DN = "Dn"
	MAX_CAP = "MaxCap"
	MIN_CAP = "MinCap"
	NUMBER_OF_BLOCKS = "NumberOfBlocks"
	NUMBER_OF_FLEX_FLASH_CARDS = "NumberOfFlexFlashCards"
	PER_DISK_CAP = "PerDiskCap"
	RN = "Rn"
	STATUS = "Status"
	UNITS = "Units"

	CONST_BLOCK_SIZE_UNKNOWN = "unknown"
	CONST_DISKLESS_NO = "no"
	CONST_DISKLESS_UNSPECIFIED = "unspecified"
	CONST_DISKLESS_YES = "yes"
	CONST_MAX_CAP_UNKNOWN = "unknown"
	CONST_MIN_CAP_UNKNOWN = "unknown"
	CONST_NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
	CONST_NUMBER_OF_FLEX_FLASH_CARDS_UNKNOWN = "unknown"
	CONST_PER_DISK_CAP_UNKNOWN = "unknown"
	CONST_UNITS_UNSPECIFIED = "unspecified"
