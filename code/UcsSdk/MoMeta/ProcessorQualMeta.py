import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Arch":UcsPropertyMeta("Arch", "arch", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["Dual-Core_Opteron", "Intel_P4_C", "Opteron", "Pentium_4", "Turion_64", "Xeon", "Xeon_MP", "any"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"MaxCores":UcsPropertyMeta("MaxCores", "maxCores", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["unspecified"], ["0-65535"]),
	"MaxProcs":UcsPropertyMeta("MaxProcs", "maxProcs", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["unspecified"], ["0-65535"]),
	"MaxThreads":UcsPropertyMeta("MaxThreads", "maxThreads", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["unspecified"], ["0-65535"]),
	"MinCores":UcsPropertyMeta("MinCores", "minCores", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["unspecified"], ["0-65535"]),
	"MinProcs":UcsPropertyMeta("MinProcs", "minProcs", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["unspecified"], ["0-65535"]),
	"MinThreads":UcsPropertyMeta("MinThreads", "minThreads", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["unspecified"], ["0-65535"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """[ !#$%\(\)\*\+,\-\./:;\?@\[\\\]\^_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Speed":UcsPropertyMeta("Speed", "speed", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["unspecified"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Stepping":UcsPropertyMeta("Stepping", "stepping", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, ["unspecified"], ["0-4294967295"]),
	"Meta":UcsMoMeta("ProcessorQual", "processorQual", "cpu", _VersionMeta.Version101e, "InputOutput", 0x3fffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "pn-policy"])
}

