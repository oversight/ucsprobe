import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeSwitchFirmwareInv(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeSwitchFirmwareInv")

	@staticmethod
	def ClassId():
		return "apeSwitchFirmwareInv"

	BIOS_VERSION = "BiosVersion"
	DN = "Dn"
	FABRIC = "Fabric"
	KS_STARTUP_VERSION = "KsStartupVersion"
	KS_VERSION = "KsVersion"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	SYS_STARTUP_VERSION = "SysStartupVersion"
	SYS_VERSION = "SysVersion"

	CONST_FABRIC_A = "A"
	CONST_FABRIC_B = "B"
	CONST_FABRIC_NONE = "NONE"
