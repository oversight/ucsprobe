import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfOnboardStorage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfOnboardStorage")

	@staticmethod
	def ClassId():
		return "biosVfOnboardStorage"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ONBOARD_SCUSTORAGE_SUPPORT = "VpOnboardSCUStorageSupport"

	CONST_VP_ONBOARD_SCUSTORAGE_SUPPORT_DISABLED = "disabled"
	CONST_VP_ONBOARD_SCUSTORAGE_SUPPORT_ENABLED = "enabled"
	CONST_VP_ONBOARD_SCUSTORAGE_SUPPORT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ONBOARD_SCUSTORAGE_SUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"
