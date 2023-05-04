import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Ipv4keys":UcsPropertyMeta("Ipv4keys", "ipv4keys", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((defaultValue|none|src-port|ipv4-src-address|ipv4-dest-address|dest-port|ip-protocol|ip-tos),){0,7}(defaultValue|none|src-port|ipv4-src-address|ipv4-dest-address|dest-port|ip-protocol|ip-tos){0,1}""", [], ["0-4294967295"]),
	"Ipv6keys":UcsPropertyMeta("Ipv6keys", "ipv6keys", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((defaultValue|none|src-port|ipv6-src-address|ipv6-dest-address|dest-port|ip-protocol),){0,6}(defaultValue|none|src-port|ipv6-src-address|ipv6-dest-address|dest-port|ip-protocol){0,1}""", [], ["0-4294967295"]),
	"KeyType":UcsPropertyMeta("KeyType", "keyType", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["ipv4keys", "ipv6keys", "l2keys"], ["0-4294967295"]),
	"L2keys":UcsPropertyMeta("L2keys", "l2keys", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((defaultValue|none|ethertype|dest-mac-address|src-mac-address),){0,4}(defaultValue|none|ethertype|dest-mac-address|src-mac-address){0,1}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"Nonkeys":UcsPropertyMeta("Nonkeys", "nonkeys", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((defaultValue|none|counter-packets-long|counter-bytes-long|sys-uptime-first|sys-uptime-last),){0,5}(defaultValue|none|counter-packets-long|counter-bytes-long|sys-uptime-first|sys-uptime-last){0,1}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"RecordType":UcsPropertyMeta("RecordType", "recordType", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["system-defined", "user-defined"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricFlowMonDefinition", "fabricFlowMonDefinition", "flow-record-[Name]", _VersionMeta.Version221b, "InputOutput", 0xfffL, [], [], [None], ["admin", "ext-lan-config", "ext-lan-policy"])
}

