import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"CType":UcsPropertyMeta("CType", "cType", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x1L, None, None, None, ["mux", "mux-access", "mux-fabric", "mux-fabricpc", "mux-fabricpc-to-hostpc", "mux-fabricpc-to-hostport", "mux-fabricport-to-hostpc", "mux-hostpc-to-adaptorpc", "mux-to-chassis", "mux-to-host", "switch-access", "switch-fabric", "switch-fabricpc", "switch-to-host", "switch-to-mux"], ["0-4294967295"]),
	"ChassisId":UcsPropertyMeta("ChassisId", "chassisId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-255"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DiagLldpTransmit":UcsPropertyMeta("DiagLldpTransmit", "diagLldpTransmit", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"EpDn":UcsPropertyMeta("EpDn", "epDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"IfRole":UcsPropertyMeta("IfRole", "ifRole", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], ["0-4294967295"]),
	"IfType":UcsPropertyMeta("IfType", "ifType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], ["0-4294967295"]),
	"Locale":UcsPropertyMeta("Locale", "locale", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PeerChassisId":UcsPropertyMeta("PeerChassisId", "peerChassisId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-255"]),
	"PeerDn":UcsPropertyMeta("PeerDn", "peerDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PeerMac":UcsPropertyMeta("PeerMac", "peerMac", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"PeerPortId":UcsPropertyMeta("PeerPortId", "peerPortId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PeerSlotId":UcsPropertyMeta("PeerSlotId", "peerSlotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PortId":UcsPropertyMeta("PortId", "portId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Side":UcsPropertyMeta("Side", "side", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["left", "right"], ["0-4294967295"]),
	"SlotId":UcsPropertyMeta("SlotId", "slotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricPathEp", "fabricPathEp", "ep-[CType]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'portTrustMode'], ["Get"], ["read-only"])
}

