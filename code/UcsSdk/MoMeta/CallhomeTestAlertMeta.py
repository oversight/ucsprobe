import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Description":UcsPropertyMeta("Description", "description", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Group":UcsPropertyMeta("Group", "group", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["diagnostic", "environmental", "unknown"], ["0-4294967295"]),
	"Level":UcsPropertyMeta("Level", "level", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["critical", "debug", "fatal", "major", "minor", "normal", "notify", "unknown", "warning"], ["0-4294967295"]),
	"MessageSubtype":UcsPropertyMeta("MessageSubtype", "messageSubtype", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["delta", "full", "goldmajor", "goldminor", "goldnormal", "major", "minor", "nosubtype", "test", "unknown"], ["0-4294967295"]),
	"MessageType":UcsPropertyMeta("MessageType", "messageType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["conf", "diag", "env", "inventory", "syslog", "test", "unknown"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"SendNow":UcsPropertyMeta("SendNow", "sendNow", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("CallhomeTestAlert", "callhomeTestAlert", "testalert", _VersionMeta.Version101e, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin", "operations"])
}

