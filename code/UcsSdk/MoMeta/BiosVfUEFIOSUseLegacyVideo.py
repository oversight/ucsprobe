import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfUEFIOSUseLegacyVideo(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfUEFIOSUseLegacyVideo")

	@staticmethod
	def ClassId():
		return "biosVfUEFIOSUseLegacyVideo"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_UEFIOSUSE_LEGACY_VIDEO = "VpUEFIOSUseLegacyVideo"

	CONST_VP_UEFIOSUSE_LEGACY_VIDEO_DISABLED = "disabled"
	CONST_VP_UEFIOSUSE_LEGACY_VIDEO_ENABLED = "enabled"
	CONST_VP_UEFIOSUSE_LEGACY_VIDEO_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_UEFIOSUSE_LEGACY_VIDEO_PLATFORM_RECOMMENDED = "platform-recommended"
