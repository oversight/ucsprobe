import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class OrgOrg(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"OrgOrg")

	@staticmethod
	def ClassId():
		return "orgOrg"

	DESCR = "Descr"
	DN = "Dn"
	LEVEL = "Level"
	NAME = "Name"
	PERM_ACCESS = "PermAccess"
	RN = "Rn"
	STATUS = "Status"

	CONST_LEVEL_1 = "1"
	CONST_LEVEL_2 = "2"
	CONST_LEVEL_3 = "3"
	CONST_LEVEL_4 = "4"
	CONST_LEVEL_5 = "5"
	CONST_LEVEL_ROOT = "root"
	CONST_PERM_ACCESS_FALSE = "false"
	CONST_PERM_ACCESS_NO = "no"
	CONST_PERM_ACCESS_TRUE = "true"
	CONST_PERM_ACCESS_YES = "yes"
