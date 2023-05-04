import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysfileDigest(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysfileDigest")

	@staticmethod
	def ClassId():
		return "sysfileDigest"

	CREATION_TS = "CreationTS"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	SIZE = "Size"
	SOURCE = "Source"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TS = "Ts"
	URI = "Uri"

	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
