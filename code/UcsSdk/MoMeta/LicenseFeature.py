import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseFeature(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseFeature")

	@staticmethod
	def ClassId():
		return "licenseFeature"

	DESCR = "Descr"
	DN = "Dn"
	GRACE_PERIOD = "GracePeriod"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VENDOR = "Vendor"
	VERSION = "Version"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TYPE_BOOLEAN = "boolean"
	CONST_TYPE_COUNTED = "counted"
