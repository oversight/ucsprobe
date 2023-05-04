import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConcurCap":UcsPropertyMeta("ConcurCap", "concurCap", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, ["unlimited"], ["0-65535"]),
	"Day":UcsPropertyMeta("Day", "day", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday", "even-day", "every-day", "odd-day"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Hour":UcsPropertyMeta("Hour", "hour", "ushort", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-23"]),
	"JobCount":UcsPropertyMeta("JobCount", "jobCount", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Minute":UcsPropertyMeta("Minute", "minute", "ushort", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-59"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"ProcBreak":UcsPropertyMeta("ProcBreak", "procBreak", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]),
	"ProcCap":UcsPropertyMeta("ProcCap", "procCap", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["unlimited"], ["0-65535"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TimeCap":UcsPropertyMeta("TimeCap", "timeCap", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]),
	"Meta":UcsMoMeta("TrigRecurrWindow", "trigRecurrWindow", "recurr-[Name]", _VersionMeta.Version141i, "InputOutput", 0xfffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "ls-compute", "ls-config", "ls-server"])
}

