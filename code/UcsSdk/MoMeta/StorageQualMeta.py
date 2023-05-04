import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BlockSize":UcsPropertyMeta("BlockSize", "blockSize", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["unknown"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Diskless":UcsPropertyMeta("Diskless", "diskless", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["no", "unspecified", "yes"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"MaxCap":UcsPropertyMeta("MaxCap", "maxCap", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["unknown"], ["0-4294967295"]),
	"MinCap":UcsPropertyMeta("MinCap", "minCap", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["unknown"], ["0-4294967295"]),
	"NumberOfBlocks":UcsPropertyMeta("NumberOfBlocks", "numberOfBlocks", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["unknown"], ["0-4294967295"]),
	"NumberOfFlexFlashCards":UcsPropertyMeta("NumberOfFlexFlashCards", "numberOfFlexFlashCards", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["unknown"], ["0-4294967295"]),
	"PerDiskCap":UcsPropertyMeta("PerDiskCap", "perDiskCap", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["unknown"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Units":UcsPropertyMeta("Units", "units", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["unspecified"], ["0-4294967295"]),
	"Meta":UcsMoMeta("StorageQual", "storageQual", "local-storage", _VersionMeta.Version101e, "InputOutput", 0xfffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "pn-policy"])
}

