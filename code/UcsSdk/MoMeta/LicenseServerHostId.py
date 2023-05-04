import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseServerHostId(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseServerHostId")

	@staticmethod
	def ClassId():
		return "licenseServerHostId"

	DN = "Dn"
	HOST_ID = "HostId"
	RN = "Rn"
	SCOPE = "Scope"
	STATUS = "Status"

	CONST_SCOPE_A = "A"
	CONST_SCOPE_B = "B"
	CONST_SCOPE_SERVER = "server"
	CONST_SCOPE_UNKNOWN = "unknown"
