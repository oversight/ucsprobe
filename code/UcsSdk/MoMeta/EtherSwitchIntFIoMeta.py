import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Ack":UcsPropertyMeta("Ack", "ack", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], ["0-4294967295"]),
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"ChassisId":UcsPropertyMeta("ChassisId", "chassisId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-255"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DelFeTs":UcsPropertyMeta("DelFeTs", "delFeTs", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["never"], ["0-4294967295"]),
	"Discovery":UcsPropertyMeta("Discovery", "discovery", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["absent", "mis-connect", "missing", "new", "present"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Encap":UcsPropertyMeta("Encap", "encap", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["dot1q", "isl", "negotiate", "proprietary", "unknown"], ["0-4294967295"]),
	"EpDn":UcsPropertyMeta("EpDn", "epDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"IfRole":UcsPropertyMeta("IfRole", "ifRole", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], ["0-4294967295"]),
	"IfType":UcsPropertyMeta("IfType", "ifType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], ["0-4294967295"]),
	"Locale":UcsPropertyMeta("Locale", "locale", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], ["0-4294967295"]),
	"Mode":UcsPropertyMeta("Mode", "mode", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["E", "F", "SD", "access", "fabric", "n_proxy", "trunk", "unknown"], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"NewFeTs":UcsPropertyMeta("NewFeTs", "newFeTs", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["never"], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["admin-down", "error-disabled", "failed", "hardware-failure", "indeterminate", "link-down", "link-up", "no-license", "sfp-not-present", "software-failure", "udld-aggr-down", "up"], ["0-4294967295"]),
	"PeerChassisId":UcsPropertyMeta("PeerChassisId", "peerChassisId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-255"]),
	"PeerDn":UcsPropertyMeta("PeerDn", "peerDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PeerPortId":UcsPropertyMeta("PeerPortId", "peerPortId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PeerSlotId":UcsPropertyMeta("PeerSlotId", "peerSlotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PortId":UcsPropertyMeta("PortId", "portId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, None, None, None, [], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"SlotId":UcsPropertyMeta("SlotId", "slotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"StateQual":UcsPropertyMeta("StateQual", "stateQual", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"Ts":UcsPropertyMeta("Ts", "ts", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"XcvrType":UcsPropertyMeta("XcvrType", "xcvrType", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["10gbaseer", "10gbaselr", "10gbaselrm", "10gbasesr", "cwdm1471", "cwdm1531", "cwdm1551", "fet", "h10gcu1m", "h10gcu3m", "h10gcu5m", "h10gcu7m", "h10glrmsm", "h10gusr", "sfp", "unknown", "x2"], ["0-4294967295"]),
	"Meta":UcsMoMeta("EtherSwitchIntFIo", "etherSwitchIntFIo", "port-[PortId]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'equipmentXcvr', u'faultInst', u'portDomainEp'], ["Get"], ["read-only"])
}

