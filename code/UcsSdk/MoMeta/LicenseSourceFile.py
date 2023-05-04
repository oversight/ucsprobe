import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseSourceFile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseSourceFile")

	@staticmethod
	def ClassId():
		return "licenseSourceFile"

	DN = "Dn"
	EXP = "Exp"
	HOST_ID = "HostId"
	ID = "Id"
	LINE = "Line"
	PAK = "Pak"
	QUANT = "Quant"
	RN = "Rn"
	SIG = "Sig"
	STATUS = "Status"
	TYPE = "Type"

	CONST_EXP_NEVER = "never"
	CONST_TYPE_FEATURE = "feature"
	CONST_TYPE_INCREMENT = "increment"
	CONST_TYPE_UPGRADE = "upgrade"
