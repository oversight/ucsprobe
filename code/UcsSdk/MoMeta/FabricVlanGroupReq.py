import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricVlanGroupReq(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricVlanGroupReq")

	@staticmethod
	def ClassId():
		return "fabricVlanGroupReq"

	CONFIG_ISSUES = "ConfigIssues"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_LAN = "lan"
	CONST_TYPE_SAN = "san"
