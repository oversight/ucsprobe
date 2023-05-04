import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicConnDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicConnDef")

	@staticmethod
	def ClassId():
		return "vnicConnDef"

	DN = "Dn"
	LAN_CONN_POLICY_NAME = "LanConnPolicyName"
	OPER_LAN_CONN_POLICY_NAME = "OperLanConnPolicyName"
	OPER_SAN_CONN_POLICY_NAME = "OperSanConnPolicyName"
	RN = "Rn"
	SAN_CONN_POLICY_NAME = "SanConnPolicyName"
	STATUS = "Status"

