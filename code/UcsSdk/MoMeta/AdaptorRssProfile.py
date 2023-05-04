import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorRssProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorRssProfile")

	@staticmethod
	def ClassId():
		return "adaptorRssProfile"

	DN = "Dn"
	RECEIVE_SIDE_SCALING = "ReceiveSideScaling"
	RN = "Rn"
	STATUS = "Status"

	CONST_RECEIVE_SIDE_SCALING_DISABLED = "disabled"
	CONST_RECEIVE_SIDE_SCALING_ENABLED = "enabled"
