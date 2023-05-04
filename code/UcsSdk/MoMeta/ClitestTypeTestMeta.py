import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Achar":UcsPropertyMeta("Achar", "achar", "byte", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, [], ["0-4294967295"]),
	"Adate":UcsPropertyMeta("Adate", "adate", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Adatetime":UcsPropertyMeta("Adatetime", "adatetime", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Afloat":UcsPropertyMeta("Afloat", "afloat", "float", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"Amac":UcsPropertyMeta("Amac", "amac", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"Anenum":UcsPropertyMeta("Anenum", "anenum", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["down", "kindOfUp", "sortOfDown", "up"], ["0-4294967295"]),
	"Anipv4":UcsPropertyMeta("Anipv4", "anipv4", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Anipv6":UcsPropertyMeta("Anipv6", "anipv6", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Ansbyte":UcsPropertyMeta("Ansbyte", "ansbyte", "sbyte", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["0-4294967295"]),
	"Ansint16":UcsPropertyMeta("Ansint16", "ansint16", "short", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"Ansint32":UcsPropertyMeta("Ansint32", "ansint32", "int", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, [], ["0-4294967295"]),
	"Ansint64":UcsPropertyMeta("Ansint64", "ansint64", "long", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, [], ["0-4294967295"]),
	"Apassword":UcsPropertyMeta("Apassword", "apassword", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["0-4294967295"]),
	"Arange":UcsPropertyMeta("Arange", "arange", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, [], ["7-55", "99-255"]),
	"Arcstring":UcsPropertyMeta("Arcstring", "arcstring", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, """[abcdefghijklmnoprstuvwyA-Z0-9]{0,15}""", [], ["0-4294967295"]),
	"Arxstring":UcsPropertyMeta("Arxstring", "arxstring", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8000L, None, None, """(red|blue|green)+(yellow|purple)+""", [], ["0-4294967295"]),
	"Astring":UcsPropertyMeta("Astring", "astring", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10000L, 0, 510, None, [], ["0-4294967295"]),
	"Atime":UcsPropertyMeta("Atime", "atime", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20000L, None, None, None, [], ["0-4294967295"]),
	"Aubyte":UcsPropertyMeta("Aubyte", "aubyte", "byte", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40000L, None, None, None, [], ["0-4294967295"]),
	"Auint16":UcsPropertyMeta("Auint16", "auint16", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80000L, None, None, None, [], ["0-4294967295"]),
	"Auint32":UcsPropertyMeta("Auint32", "auint32", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100000L, None, None, None, [], ["0-4294967295"]),
	"Auint64":UcsPropertyMeta("Auint64", "auint64", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200000L, None, None, None, [], ["0-4294967295"]),
	"Awwn":UcsPropertyMeta("Awwn", "awwn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x800000L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x1000000L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2000000L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ClitestTypeTest", "clitestTypeTest", "tt-", _VersionMeta.Version101e, "InputOutput", 0x7ffffffL, [], [], ["Get"], ["admin"])
}

