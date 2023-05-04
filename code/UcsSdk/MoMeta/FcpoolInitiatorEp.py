import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FcpoolInitiatorEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FcpoolInitiatorEp")

	@staticmethod
	def ClassId():
		return "fcpoolInitiatorEp"

	DN = "Dn"
	ID = "Id"
	INITIATOR_DN = "InitiatorDn"
	PURPOSE = "Purpose"
	RN = "Rn"
	STATUS = "Status"

	CONST_PURPOSE_NODE_WWN = "node-wwn"
	CONST_PURPOSE_PORT_WWN = "port-wwn"
