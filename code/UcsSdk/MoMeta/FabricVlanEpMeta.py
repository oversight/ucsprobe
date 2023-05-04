import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AssocPrimaryVlanState":UcsPropertyMeta("AssocPrimaryVlanState", "assocPrimaryVlanState", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["does-not-exists", "is-empty", "is-in-error-state", "is-not-primary-type", "ok"], ["0-4294967295"]),
	"AssocPrimaryVlanSwitchId":UcsPropertyMeta("AssocPrimaryVlanSwitchId", "assocPrimaryVlanSwitchId", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"EpDn":UcsPropertyMeta("EpDn", "epDn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["1-4093"]),
	"IfRole":UcsPropertyMeta("IfRole", "ifRole", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], ["0-4294967295"]),
	"IfType":UcsPropertyMeta("IfType", "ifType", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], ["0-4294967295"]),
	"IsNative":UcsPropertyMeta("IsNative", "isNative", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Locale":UcsPropertyMeta("Locale", "locale", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version141i, UcsPropertyMeta.CreateOnly, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,32}""", [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["error-misconfigured", "ok"], ["0-4294967295"]),
	"OverlapStateForA":UcsPropertyMeta("OverlapStateForA", "overlapStateForA", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-active", "ok", "primary-id-mismatch", "sharing-type-mismatch"], ["0-4294967295"]),
	"OverlapStateForB":UcsPropertyMeta("OverlapStateForB", "overlapStateForB", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-active", "ok", "primary-id-mismatch", "sharing-type-mismatch"], ["0-4294967295"]),
	"PeerDn":UcsPropertyMeta("PeerDn", "peerDn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"PubNwDn":UcsPropertyMeta("PubNwDn", "pubNwDn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PubNwId":UcsPropertyMeta("PubNwId", "pubNwId", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PubNwName":UcsPropertyMeta("PubNwName", "pubNwName", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Sharing":UcsPropertyMeta("Sharing", "sharing", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["community", "isolated", "none", "primary"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricVlanEp", "fabricVlanEp", "vlan-[Id]", _VersionMeta.Version141i, "InputOutput", 0x1ffL, [], [], ["Get"], ["read-only"])
}

