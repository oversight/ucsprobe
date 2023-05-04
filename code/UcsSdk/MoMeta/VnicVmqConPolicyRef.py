import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicVmqConPolicyRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicVmqConPolicyRef")

	@staticmethod
	def ClassId():
		return "vnicVmqConPolicyRef"

	CON_POLICY_NAME = "ConPolicyName"
	DN = "Dn"
	OPER_CON_POLICY_NAME = "OperConPolicyName"
	RN = "Rn"
	STATUS = "Status"

