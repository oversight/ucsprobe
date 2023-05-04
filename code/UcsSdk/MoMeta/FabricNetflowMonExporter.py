import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowMonExporter(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowMonExporter")

	@staticmethod
	def ClassId():
		return "fabricNetflowMonExporter"

	DESCR = "Descr"
	DN = "Dn"
	DSCP = "Dscp"
	EXPORT_INTERNAL = "ExportInternal"
	EXPORTER_STATS_TIMEOUT = "ExporterStatsTimeout"
	FLOW_EXP_PROFILE = "FlowExpProfile"
	FLOW_MON_COLLECTOR = "FlowMonCollector"
	INTERFACE_TABLE_TIMEOUT = "InterfaceTableTimeout"
	NAME = "Name"
	OPER_FLOW_EXP_PROFILE = "OperFlowExpProfile"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PROTOCOL = "Protocol"
	RN = "Rn"
	STATUS = "Status"
	TEMPLATE_DATA_TIMEOUT = "TemplateDataTimeout"
	TRANSPORT = "Transport"
	TRANSPORT_PROTOCOL = "TransportProtocol"
	TYPE = "Type"
	VERSION = "Version"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTOCOL_NETFLOW = "netflow"
	CONST_TRANSPORT_PROTOCOL_SCTP = "sctp"
	CONST_TRANSPORT_PROTOCOL_UDP = "udp"
	CONST_VERSION_IPFIX = "ipfix"
	CONST_VERSION_V9 = "v9"
