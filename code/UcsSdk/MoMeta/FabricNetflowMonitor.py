import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowMonitor(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowMonitor")

	@staticmethod
	def ClassId():
		return "fabricNetflowMonitor"

	DESCR = "Descr"
	DN = "Dn"
	FLOW_MON_PROTOCOL = "FlowMonProtocol"
	FLOW_MON_RECORD_DEF = "FlowMonRecordDef"
	FLOW_TIMEOUT_POLICY = "FlowTimeoutPolicy"
	NAME = "Name"
	OPER_FLOW_MON_RECORD_DEF = "OperFlowMonRecordDef"
	OPER_FLOW_TIMEOUT_POLICY = "OperFlowTimeoutPolicy"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_FLOW_MON_PROTOCOL_NETFLOW = "netflow"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
