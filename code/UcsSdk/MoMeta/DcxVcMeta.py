import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"BorderPortId":UcsPropertyMeta("BorderPortId", "borderPortId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BorderSlotId":UcsPropertyMeta("BorderSlotId", "borderSlotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BorderVfcId":UcsPropertyMeta("BorderVfcId", "borderVfcId", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Cdp":UcsPropertyMeta("Cdp", "cdp", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Cookie":UcsPropertyMeta("Cookie", "cookie", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Cos":UcsPropertyMeta("Cos", "cos", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["any"], ["0-6", "255-255"]),
	"DerivedFromId":UcsPropertyMeta("DerivedFromId", "derivedFromId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Encap":UcsPropertyMeta("Encap", "encap", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["consolidated", "virtual"], ["0-4294967295"]),
	"FcoeId":UcsPropertyMeta("FcoeId", "fcoeId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"ForgeMac":UcsPropertyMeta("ForgeMac", "forgeMac", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allow", "deny"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["0-4294967295"]),
	"InstType":UcsPropertyMeta("InstType", "instType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], ["0-4294967295"]),
	"Lc":UcsPropertyMeta("Lc", "lc", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], ["0-4294967295"]),
	"LinkState":UcsPropertyMeta("LinkState", "linkState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["admin-down", "down", "error", "unallocated", "unavailable", "unknown", "up"], ["0-4294967295"]),
	"Locale":UcsPropertyMeta("Locale", "locale", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], ["0-4294967295"]),
	"MacRegisterMode":UcsPropertyMeta("MacRegisterMode", "macRegisterMode", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["all-host-vlans", "only-native-vlan"], ["0-4294967295"]),
	"MonTrafDir":UcsPropertyMeta("MonTrafDir", "monTrafDir", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["both", "rx", "tx"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperBorderPortId":UcsPropertyMeta("OperBorderPortId", "operBorderPortId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OperBorderSlotId":UcsPropertyMeta("OperBorderSlotId", "operBorderSlotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["active", "admin-down", "error", "link-down", "passive", "unknown"], ["0-4294967295"]),
	"PeerId":UcsPropertyMeta("PeerId", "peerId", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ProtState":UcsPropertyMeta("ProtState", "protState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["active", "no-protection", "passive"], ["0-4294967295"]),
	"QosPolicyDn":UcsPropertyMeta("QosPolicyDn", "qosPolicyDn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"QosPolicyId":UcsPropertyMeta("QosPolicyId", "qosPolicyId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["none"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Role":UcsPropertyMeta("Role", "role", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], ["0-4294967295"]),
	"State":UcsPropertyMeta("State", "state", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["CreatePend", "Creating", "DestroyPend", "Destroying", "ModifyPend", "Modifying", "Present", "Unknown"], ["0-4294967295"]),
	"StateQual":UcsPropertyMeta("StateQual", "stateQual", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Tag":UcsPropertyMeta("Tag", "tag", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"UplinkFailAction":UcsPropertyMeta("UplinkFailAction", "uplinkFailAction", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, None, None, None, None, ["link-down", "warning"], ["0-4294967295"]),
	"Vnic":UcsPropertyMeta("Vnic", "vnic", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("DcxVc", "dcxVc", "vc-[Id]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'faultInst', u'swCmclan', u'swNetflowMonitorRef', u'swUlan', u'swVlan', u'swVsan'], ["Get"], ["read-only"])
}

