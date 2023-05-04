import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cdp":UcsPropertyMeta("Cdp", "cdp", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigQualifier":UcsPropertyMeta("ConfigQualifier", "configQualifier", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["invalid-name", "normal"], ["0-4294967295"]),
	"Cos":UcsPropertyMeta("Cos", "cos", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["any"], ["0-6", "255-255"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"ForgeMac":UcsPropertyMeta("ForgeMac", "forgeMac", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allow", "deny"], ["0-4294967295"]),
	"HostNwIOPerf":UcsPropertyMeta("HostNwIOPerf", "hostNwIOPerf", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["high-perf-reqd", "none"], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"MacRegisterMode":UcsPropertyMeta("MacRegisterMode", "macRegisterMode", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["all-host-vlans", "only-native-vlan"], ["0-4294967295"]),
	"MaxPorts":UcsPropertyMeta("MaxPorts", "maxPorts", "ushort", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["1-4096"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{1,31}""", [], ["0-4294967295"]),
	"NwCtrlPolicyName":UcsPropertyMeta("NwCtrlPolicyName", "nwCtrlPolicyName", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperNwCtrlPolicyName":UcsPropertyMeta("OperNwCtrlPolicyName", "operNwCtrlPolicyName", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperQosPolicyName":UcsPropertyMeta("OperQosPolicyName", "operQosPolicyName", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PinToGroupName":UcsPropertyMeta("PinToGroupName", "pinToGroupName", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"PortProfileUuid":UcsPropertyMeta("PortProfileUuid", "portProfileUuid", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
	"PrimaryVlanId":UcsPropertyMeta("PrimaryVlanId", "primaryVlanId", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["1-4093"]),
	"QosPolicyDn":UcsPropertyMeta("QosPolicyDn", "qosPolicyDn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"QosPolicyId":UcsPropertyMeta("QosPolicyId", "qosPolicyId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["none"], ["0-4294967295"]),
	"QosPolicyName":UcsPropertyMeta("QosPolicyName", "qosPolicyName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x800L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwABorderPort":UcsPropertyMeta("SwABorderPort", "swABorderPort", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"SwABorderSlot":UcsPropertyMeta("SwABorderSlot", "swABorderSlot", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"SwBBorderPort":UcsPropertyMeta("SwBBorderPort", "swBBorderPort", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"SwBBorderSlot":UcsPropertyMeta("SwBBorderSlot", "swBBorderSlot", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, ["regular", "sla-only"], ["0-4294967295"]),
	"UplinkFailAction":UcsPropertyMeta("UplinkFailAction", "uplinkFailAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["link-down", "warning"], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicProfile", "vnicProfile", "vnic-[Name]", _VersionMeta.Version101e, "InputOutput", 0x3fffL, [], [u'fabricNetflowMonSrcEp', u'faultInst', u'swNetflowMonitorRef', u'vmVnicProfCl', u'vnicEtherIf', u'vnicOProfileAlias', u'vnicProfileAlias'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-network", "ls-network-policy"])
}

