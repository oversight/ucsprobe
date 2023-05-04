import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AckAction":UcsPropertyMeta("AckAction", "ackAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["delete-on-clear", "initial-severity"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ClearAction":UcsPropertyMeta("ClearAction", "clearAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["delete", "retain"], ["0-4294967295"]),
	"ClearInterval":UcsPropertyMeta("ClearInterval", "clearInterval", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["never"], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"FlapInterval":UcsPropertyMeta("FlapInterval", "flapInterval", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["5-3600"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"RetentionInterval":UcsPropertyMeta("RetentionInterval", "retentionInterval", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["forever"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"SizeLimit":UcsPropertyMeta("SizeLimit", "sizeLimit", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["max"], ["0-20000"]),
	"SoakInterval":UcsPropertyMeta("SoakInterval", "soakInterval", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[0-9]{1,4}|(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["never"], ["0-4294967295"]),
	"SoakingSeverity":UcsPropertyMeta("SoakingSeverity", "soakingSeverity", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["condition", "info", "warning"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FaultPolicy", "faultPolicy", "fault-policy", _VersionMeta.Version101e, "InputOutput", 0x1fffL, [], [], ["Get", "Set"], ["admin", "fault"])
}

