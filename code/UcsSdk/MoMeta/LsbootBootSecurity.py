import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootBootSecurity(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootBootSecurity")

	@staticmethod
	def ClassId():
		return "lsbootBootSecurity"

	DN = "Dn"
	RN = "Rn"
	SECURE_BOOT = "SecureBoot"
	STATUS = "Status"

	CONST_SECURE_BOOT_FALSE = "false"
	CONST_SECURE_BOOT_NO = "no"
	CONST_SECURE_BOOT_TRUE = "true"
	CONST_SECURE_BOOT_YES = "yes"
