import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyDigest(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyDigest")

	@staticmethod
	def ClassId():
		return "policyDigest"

	CONTEXT = "Context"
	DESCR = "Descr"
	DN = "Dn"
	LABEL = "Label"
	NAME = "Name"
	ON_BEHALF_OF_IDENT = "OnBehalfOfIdent"
	ON_BEHALF_OF_TYPE = "OnBehalfOfType"
	REQUESTOR_OWNERSHIP = "RequestorOwnership"
	RESOLVE_TYPE = "ResolveType"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	USAGE = "Usage"

	CONST_REQUESTOR_OWNERSHIP_LOCAL = "local"
	CONST_REQUESTOR_OWNERSHIP_PENDING_POLICY = "pending-policy"
	CONST_REQUESTOR_OWNERSHIP_POLICY = "policy"
	CONST_RESOLVE_TYPE_NAME = "name"
	CONST_RESOLVE_TYPE_RN = "rn"
