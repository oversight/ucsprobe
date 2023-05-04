import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwNetflowExporter(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwNetflowExporter")

	@staticmethod
	def ClassId():
		return "swNetflowExporter"

	DESTINATION_IP_ADDRESS = "DestinationIpAddress"
	DESTINATION_PORT = "DestinationPort"
	DN = "Dn"
	DSCP = "Dscp"
	EXPORT_INTERNAL = "ExportInternal"
	EXPORTER_STATS_TIMEOUT = "ExporterStatsTimeout"
	INTERFACE_TABLE_TIMEOUT = "InterfaceTableTimeout"
	IS_VALID_CONFIG = "IsValidConfig"
	LIFE_CYCLE = "LifeCycle"
	NAME = "Name"
	PEER_DN = "PeerDn"
	PROTOCOL = "Protocol"
	RN = "Rn"
	SOURCE_VLAN = "SourceVlan"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TEMPLATE_DATA_TIMEOUT = "TemplateDataTimeout"
	TRANSPORT = "Transport"
	TRANSPORT_PROTOCOL = "TransportProtocol"
	TYPE = "Type"
	VERSION = "Version"

	CONST_IS_VALID_CONFIG_INCOMPLETE = "incomplete"
	CONST_IS_VALID_CONFIG_OK = "ok"
	CONST_LIFE_CYCLE_DELETED = "deleted"
	CONST_LIFE_CYCLE_NEW = "new"
	CONST_LIFE_CYCLE_NORMAL = "normal"
	CONST_PROTOCOL_NETFLOW = "netflow"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_TRANSPORT_PROTOCOL_SCTP = "sctp"
	CONST_TRANSPORT_PROTOCOL_UDP = "udp"
	CONST_VERSION_IPFIX = "ipfix"
	CONST_VERSION_V9 = "v9"
