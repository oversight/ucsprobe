import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Dscp":UcsPropertyMeta("Dscp", "dscp", "ushort", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-63"]),
	"ExportInternal":UcsPropertyMeta("ExportInternal", "exportInternal", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ExporterStatsTimeout":UcsPropertyMeta("ExporterStatsTimeout", "exporterStatsTimeout", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["1-86400"]),
	"FlowExpProfile":UcsPropertyMeta("FlowExpProfile", "flowExpProfile", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"FlowMonCollector":UcsPropertyMeta("FlowMonCollector", "flowMonCollector", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"InterfaceTableTimeout":UcsPropertyMeta("InterfaceTableTimeout", "interfaceTableTimeout", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["1-86400"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x100L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"OperFlowExpProfile":UcsPropertyMeta("OperFlowExpProfile", "operFlowExpProfile", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Protocol":UcsPropertyMeta("Protocol", "protocol", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["netflow"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TemplateDataTimeout":UcsPropertyMeta("TemplateDataTimeout", "templateDataTimeout", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["1-86400"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"TransportProtocol":UcsPropertyMeta("TransportProtocol", "transportProtocol", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["sctp", "udp"], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"Version":UcsPropertyMeta("Version", "version", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ipfix", "v9"], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricNetflowMonExporter", "fabricNetflowMonExporter", "lanFlowMonExporter-eth-netflow-[Name]", _VersionMeta.Version221b, "InputOutput", 0x1fffL, [], [u'faultInst'], [None], ["admin", "ext-lan-config", "ext-lan-policy"])
}

