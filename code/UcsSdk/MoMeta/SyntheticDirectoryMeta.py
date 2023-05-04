import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Atime":UcsPropertyMeta("Atime", "atime", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, [], ["0-4294967295"]),
	"Blksize":UcsPropertyMeta("Blksize", "blksize", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["0-4294967295"]),
	"Blocks":UcsPropertyMeta("Blocks", "blocks", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x8L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Ctime":UcsPropertyMeta("Ctime", "ctime", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"Dev":UcsPropertyMeta("Dev", "dev", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Gid":UcsPropertyMeta("Gid", "gid", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-4294967295"]),
	"Ino":UcsPropertyMeta("Ino", "ino", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x100L, None, None, None, [], ["0-4294967295"]),
	"Mode":UcsPropertyMeta("Mode", "mode", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"Mtime":UcsPropertyMeta("Mtime", "mtime", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, 0, 510, None, [], ["0-4294967295"]),
	"Nlink":UcsPropertyMeta("Nlink", "nlink", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["0-4294967295"]),
	"Path":UcsPropertyMeta("Path", "path", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, 0, 510, None, [], ["0-4294967295"]),
	"Rdev":UcsPropertyMeta("Rdev", "rdev", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8000L, 0, 256, None, [], ["0-4294967295"]),
	"Size":UcsPropertyMeta("Size", "size", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10000L, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Uid":UcsPropertyMeta("Uid", "uid", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40000L, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SyntheticDirectory", "syntheticDirectory", "dir-[Ino]", _VersionMeta.Version101e, "InputOutput", 0x7ffffL, [], [u'syntheticDirectory', u'syntheticFile'], ["Get"], ["admin"])
}

