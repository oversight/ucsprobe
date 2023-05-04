import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfResumeOnACPowerLoss(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfResumeOnACPowerLoss")

	@staticmethod
	def ClassId():
		return "biosVfResumeOnACPowerLoss"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_RESUME_ON_ACPOWER_LOSS = "VpResumeOnACPowerLoss"

	CONST_VP_RESUME_ON_ACPOWER_LOSS_LAST_STATE = "last-state"
	CONST_VP_RESUME_ON_ACPOWER_LOSS_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_RESUME_ON_ACPOWER_LOSS_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_RESUME_ON_ACPOWER_LOSS_RESET = "reset"
	CONST_VP_RESUME_ON_ACPOWER_LOSS_STAY_OFF = "stay-off"
