import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaDomainAuth(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaDomainAuth")

	@staticmethod
	def ClassId():
		return "aaaDomainAuth"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OPER_PROVIDER_GROUP = "OperProviderGroup"
	OPER_REALM = "OperRealm"
	PROVIDER_GROUP = "ProviderGroup"
	REALM = "Realm"
	RN = "Rn"
	STATUS = "Status"
	USE2_FACTOR = "Use2Factor"

	CONST_OPER_REALM_LDAP = "ldap"
	CONST_OPER_REALM_LOCAL = "local"
	CONST_OPER_REALM_NONE = "none"
	CONST_OPER_REALM_RADIUS = "radius"
	CONST_OPER_REALM_TACACS = "tacacs"
	CONST_REALM_LDAP = "ldap"
	CONST_REALM_LOCAL = "local"
	CONST_REALM_NONE = "none"
	CONST_REALM_RADIUS = "radius"
	CONST_REALM_TACACS = "tacacs"
	CONST_USE2_FACTOR_FALSE = "false"
	CONST_USE2_FACTOR_NO = "no"
	CONST_USE2_FACTOR_TRUE = "true"
	CONST_USE2_FACTOR_YES = "yes"
