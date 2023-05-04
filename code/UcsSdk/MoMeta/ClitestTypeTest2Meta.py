import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"APartialEnum":UcsPropertyMeta("APartialEnum", "aPartialEnum", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["default", "untagged"], ["0-4096"]),
	"Abitmask":UcsPropertyMeta("Abitmask", "abitmask", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """((up|down|kindOfUp|sortOfDown),){0,3}(up|down|kindOfUp|sortOfDown){0,1}""", [], ["0-4294967295"]),
	"Acharbuf":UcsPropertyMeta("Acharbuf", "acharbuf", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x8L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"FileDir":UcsPropertyMeta("FileDir", "fileDir", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, 0, 510, None, [], ["0-4294967295"]),
	"FileHost":UcsPropertyMeta("FileHost", "fileHost", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, 0, 510, None, [], ["0-4294967295"]),
	"FileName":UcsPropertyMeta("FileName", "fileName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, 0, 510, None, [], ["0-4294967295"]),
	"FilePasswd":UcsPropertyMeta("FilePasswd", "filePasswd", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,80}""", [], ["0-4294967295"]),
	"FilePath":UcsPropertyMeta("FilePath", "filePath", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, 0, 510, None, [], ["0-4294967295"]),
	"FilePort":UcsPropertyMeta("FilePort", "filePort", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, [], ["0-4294967295"]),
	"FileProto":UcsPropertyMeta("FileProto", "fileProto", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], ["0-4294967295"]),
	"FileUser":UcsPropertyMeta("FileUser", "fileUser", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2000L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ClitestTypeTest2", "clitestTypeTest2", "tt2-", _VersionMeta.Version101e, "InputOutput", 0x7fffL, [], [], ["Get"], ["admin"])
}

