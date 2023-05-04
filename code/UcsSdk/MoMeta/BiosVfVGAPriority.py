import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfVGAPriority(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfVGAPriority")

	@staticmethod
	def ClassId():
		return "biosVfVGAPriority"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_VGAPRIORITY = "VpVGAPriority"

	CONST_VP_VGAPRIORITY_OFFBOARD = "offboard"
	CONST_VP_VGAPRIORITY_ONBOARD = "onboard"
	CONST_VP_VGAPRIORITY_ONBOARD_VGA_DISABLED = "onboard-vga-disabled"
	CONST_VP_VGAPRIORITY_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_VGAPRIORITY_PLATFORM_RECOMMENDED = "platform-recommended"
