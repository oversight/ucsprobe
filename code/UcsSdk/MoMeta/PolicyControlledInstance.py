import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyControlledInstance(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyControlledInstance")

	@staticmethod
	def ClassId():
		return "policyControlledInstance"

	DEF_DN = "DefDn"
	DN = "Dn"
	EXTERNAL_RESOLVE_NAME = "ExternalResolveName"
	NAME = "Name"
	RESOLVE_TYPE = "ResolveType"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_RESOLVE_TYPE_NAME = "name"
	CONST_RESOLVE_TYPE_RN = "rn"
