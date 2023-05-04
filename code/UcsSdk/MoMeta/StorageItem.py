import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageItem(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageItem")

	@staticmethod
	def ClassId():
		return "storageItem"

	DN = "Dn"
	NAME = "Name"
	OPER_STATE = "OperState"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"
	USED = "Used"

	CONST_OPER_STATE_CLEAN = "clean"
	CONST_OPER_STATE_NOT_CLEAN = "not-clean"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_SIZE_NOTHING = "nothing"
	CONST_USED_EMPTY = "empty"
	CONST_USED_FULL = "full"
	CONST_USED_NOT_APPLICABLE = "not-applicable"
