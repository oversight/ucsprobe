import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareHostPackModImpact(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareHostPackModImpact")

	@staticmethod
	def ClassId():
		return "firmwareHostPackModImpact"

	DN = "Dn"
	KEY_DN = "KeyDn"
	MAINT_POLICY_DN = "MaintPolicyDn"
	PN_DN = "PnDn"
	REBOOT_POLICY = "RebootPolicy"
	RN = "Rn"
	SERVICE_PROFILE_DN = "ServiceProfileDn"
	STATUS = "Status"

