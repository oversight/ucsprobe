import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtIntAuthPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtIntAuthPolicy")

	@staticmethod
	def ClassId():
		return "mgmtIntAuthPolicy"

	DN = "Dn"
	METHOD = "Method"
	NAME = "Name"
	PWD = "Pwd"
	RN = "Rn"
	STATUS = "Status"

	CONST_METHOD_NONE = "none"
	CONST_METHOD_PASSWORD = "password"
