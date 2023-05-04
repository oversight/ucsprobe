import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricOrgVlanPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricOrgVlanPolicy")

	@staticmethod
	def ClassId():
		return "fabricOrgVlanPolicy"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
