import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentBladeIOMConnDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentBladeIOMConnDef")

	@staticmethod
	def ClassId():
		return "equipmentBladeIOMConnDef"

	DESCR = "Descr"
	DN = "Dn"
	IOCARD_TYPE = "IocardType"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PORT_BANDWIDTH = "PortBandwidth"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PORT_BANDWIDTH_10GBPS = "10gbps"
	CONST_PORT_BANDWIDTH_1GBPS = "1gbps"
	CONST_PORT_BANDWIDTH_20GBPS = "20gbps"
	CONST_PORT_BANDWIDTH_40GBPS = "40gbps"
	CONST_PORT_BANDWIDTH_INDETERMINATE = "indeterminate"
