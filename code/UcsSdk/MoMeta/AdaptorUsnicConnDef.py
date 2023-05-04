import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorUsnicConnDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorUsnicConnDef")

	@staticmethod
	def ClassId():
		return "adaptorUsnicConnDef"

	CON_POLICY_NAME = "ConPolicyName"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	USNIC_COUNT = "UsnicCount"

