import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["disabled", "enabled", "remove"], ["0-4294967295"]),
	"BoardAggregationRole":UcsPropertyMeta("BoardAggregationRole", "boardAggregationRole", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["multi-master", "multi-slave", "none", "single"], ["0-4294967295"]),
	"ChassisId":UcsPropertyMeta("ChassisId", "chassisId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, ["N/A"], ["1-255"]),
	"CheckpointTrigTs":UcsPropertyMeta("CheckpointTrigTs", "checkpointTrigTs", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["never"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x4L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DeepCheckpointTrigTs":UcsPropertyMeta("DeepCheckpointTrigTs", "deepCheckpointTrigTs", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["never"], ["0-4294967295"]),
	"DiscTrigTs":UcsPropertyMeta("DiscTrigTs", "discTrigTs", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["never"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"EpDn":UcsPropertyMeta("EpDn", "epDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"EqType":UcsPropertyMeta("EqType", "eqType", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["blade", "chassis", "fex", "rack-unit", "unknown"], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version201m, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"IfRole":UcsPropertyMeta("IfRole", "ifRole", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], ["0-4294967295"]),
	"IfType":UcsPropertyMeta("IfType", "ifType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], ["0-4294967295"]),
	"Lc":UcsPropertyMeta("Lc", "lc", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["in-service", "migrate", "out-of-service", "out-of-service-slave"], ["0-4294967295"]),
	"LicGP":UcsPropertyMeta("LicGP", "licGP", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LicState":UcsPropertyMeta("LicState", "licState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], ["0-4294967295"]),
	"Locale":UcsPropertyMeta("Locale", "locale", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x10L, 1, 510, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["down", "error-misconfigured", "unknown", "up"], ["0-4294967295"]),
	"OperStateReason":UcsPropertyMeta("OperStateReason", "operStateReason", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"PeerChassisId":UcsPropertyMeta("PeerChassisId", "peerChassisId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-255"]),
	"PeerDn":UcsPropertyMeta("PeerDn", "peerDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PeerPortId":UcsPropertyMeta("PeerPortId", "peerPortId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PeerSlotId":UcsPropertyMeta("PeerSlotId", "peerSlotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PortId":UcsPropertyMeta("PortId", "portId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["1-48"]),
	"ProfileDn":UcsPropertyMeta("ProfileDn", "profileDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x80L, 1, 510, None, [], ["0-4294967295"]),
	"SlotId":UcsPropertyMeta("SlotId", "slotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["1-4"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x200L, 1, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricComputePhEp", "fabricComputePhEp", "compute-ep-ven-[Vendor]-mod-[Model]-ser-[Serial]", _VersionMeta.Version101e, "InputOutput", 0x3ffL, [], [u'fabricLastAckedSlot', u'faultInst'], ["Get", "Set"], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"])
}

