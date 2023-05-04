import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201q, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201q, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"PciEnum":UcsPropertyMeta("PciEnum", "pciEnum", "string", _VersionMeta.Version201q, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["multi-func-all", "static-zero-func", "zero-func-all"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201q, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201q, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VconMap":UcsPropertyMeta("VconMap", "vconMap", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["linear-ordered", "linear-ordered-to-round-robin", "round-robin", "round-robin-to-linear-ordered"], ["0-4294967295"]),
	"VnicMap":UcsPropertyMeta("VnicMap", "vnicMap", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["cap-load-distribute", "physical-cap-first"], ["0-4294967295"]),
	"VnicOrder":UcsPropertyMeta("VnicOrder", "vnicOrder", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["all-vnic", "dynamic-all-last", "static-all-first"], ["0-4294967295"]),
	"Meta":UcsMoMeta("LsVersionBeh", "lsVersionBeh", "ls-vers-beh", _VersionMeta.Version201q, "InputOutput", 0xffL, [], [], ["Get"], ["admin"])
}

