import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaLdapGroupRule(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaLdapGroupRule")

	@staticmethod
	def ClassId():
		return "aaaLdapGroupRule"

	AUTHORIZATION = "Authorization"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TARGET_ATTR = "TargetAttr"
	TRAVERSAL = "Traversal"
	USE_PRIMARY_GROUP = "UsePrimaryGroup"

	CONST_AUTHORIZATION_DISABLE = "disable"
	CONST_AUTHORIZATION_ENABLE = "enable"
	CONST_TRAVERSAL_NON_RECURSIVE = "non-recursive"
	CONST_TRAVERSAL_RECURSIVE = "recursive"
	CONST_USE_PRIMARY_GROUP_FALSE = "false"
	CONST_USE_PRIMARY_GROUP_NO = "no"
	CONST_USE_PRIMARY_GROUP_TRUE = "true"
	CONST_USE_PRIMARY_GROUP_YES = "yes"
