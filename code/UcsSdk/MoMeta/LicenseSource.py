import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseSource(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseSource")

	@staticmethod
	def ClassId():
		return "licenseSource"

	ALWAYS_USE = "AlwaysUse"
	DN = "Dn"
	HOST_ID = "HostId"
	HOST_NAME = "HostName"
	RN = "Rn"
	SKU = "Sku"
	STATUS = "Status"
	VENDOR_DAEMON_PATH = "VendorDaemonPath"

	CONST_ALWAYS_USE_FALSE = "false"
	CONST_ALWAYS_USE_NO = "no"
	CONST_ALWAYS_USE_TRUE = "true"
	CONST_ALWAYS_USE_YES = "yes"
