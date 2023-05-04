import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicVnicBehPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicVnicBehPolicy")

	@staticmethod
	def ClassId():
		return "vnicVnicBehPolicy"

	ACTION = "Action"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	NW_TEMPL_NAME = "NwTemplName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ACTION_HW_INHERIT = "hw-inherit"
	CONST_ACTION_NONE = "none"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TYPE_VHBA = "vhba"
	CONST_TYPE_VNIC = "vnic"
