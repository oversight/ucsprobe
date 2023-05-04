import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfFRB2Timer(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfFRB2Timer")

	@staticmethod
	def ClassId():
		return "biosVfFRB2Timer"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_FRB2_TIMER = "VpFRB2Timer"

	CONST_VP_FRB2_TIMER_DISABLED = "disabled"
	CONST_VP_FRB2_TIMER_ENABLED = "enabled"
	CONST_VP_FRB2_TIMER_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_FRB2_TIMER_PLATFORM_RECOMMENDED = "platform-recommended"
