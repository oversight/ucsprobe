import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Chassis1":UcsPropertyMeta("Chassis1", "chassis1", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Chassis2":UcsPropertyMeta("Chassis2", "chassis2", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Chassis3":UcsPropertyMeta("Chassis3", "chassis3", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"ChassisDeviceIoState1":UcsPropertyMeta("ChassisDeviceIoState1", "chassisDeviceIoState1", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ok", "openError", "readError", "unknown", "writeError"], ["0-4294967295"]),
	"ChassisDeviceIoState2":UcsPropertyMeta("ChassisDeviceIoState2", "chassisDeviceIoState2", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ok", "openError", "readError", "unknown", "writeError"], ["0-4294967295"]),
	"ChassisDeviceIoState3":UcsPropertyMeta("ChassisDeviceIoState3", "chassisDeviceIoState3", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ok", "openError", "readError", "unknown", "writeError"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"HaFailureReason":UcsPropertyMeta("HaFailureReason", "haFailureReason", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["PeerMgmtServicesUnresponsive", "chassisConfigIncomplete", "mgmtServicesUnresponsive", "networkInterfaceDown", "nodeDown", "none", "peerChassisConfigIncomplete", "peerNodeDown"], ["0-4294967295"]),
	"HaReadiness":UcsPropertyMeta("HaReadiness", "haReadiness", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["downgraded", "notReady", "ready", "unknown"], ["0-4294967295"]),
	"HaReady":UcsPropertyMeta("HaReady", "haReady", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Leadership":UcsPropertyMeta("Leadership", "leadership", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["electionFailed", "electionInProgress", "inapplicable", "primary", "subordinate", "unknown"], ["0-4294967295"]),
	"MgmtServicesState":UcsPropertyMeta("MgmtServicesState", "mgmtServicesState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["down", "switchoverInProgress", "unknown", "unresponsive", "up"], ["0-4294967295"]),
	"Problems":UcsPropertyMeta("Problems", "problems", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"SshAuthKeysCsum":UcsPropertyMeta("SshAuthKeysCsum", "sshAuthKeysCsum", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"SshAuthKeysSize":UcsPropertyMeta("SshAuthKeysSize", "sshAuthKeysSize", "ulong", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"SshKeyStatus":UcsPropertyMeta("SshKeyStatus", "sshKeyStatus", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["matched", "mismatched", "none"], ["0-4294967295"]),
	"SshRootPubKeyCsum":UcsPropertyMeta("SshRootPubKeyCsum", "sshRootPubKeyCsum", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"SshRootPubKeySize":UcsPropertyMeta("SshRootPubKeySize", "sshRootPubKeySize", "ulong", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"State":UcsPropertyMeta("State", "state", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["down", "unknown", "up"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"UmbilicalState":UcsPropertyMeta("UmbilicalState", "umbilicalState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["degraded", "failed", "full", "unknown"], ["0-4294967295"]),
	"VersionMismatch":UcsPropertyMeta("VersionMismatch", "versionMismatch", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Meta":UcsMoMeta("MgmtEntity", "mgmtEntity", "mgmt-entity-[Id]", _VersionMeta.Version101e, "InputOutput", 0x1fL, [], [u'faultInst', u'mgmtPmonEntry'], ["Get"], ["read-only"])
}

