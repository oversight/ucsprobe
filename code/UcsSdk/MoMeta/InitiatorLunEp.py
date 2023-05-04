import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorLunEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorLunEp")

	@staticmethod
	def ClassId():
		return "initiatorLunEp"

	BOOTABLE = "Bootable"
	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"

	CONST_BOOTABLE_FALSE = "false"
	CONST_BOOTABLE_NO = "no"
	CONST_BOOTABLE_TRUE = "true"
	CONST_BOOTABLE_YES = "yes"
