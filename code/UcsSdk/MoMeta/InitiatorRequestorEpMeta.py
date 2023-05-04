import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AllocState":UcsPropertyMeta("AllocState", "allocState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allocated", "allocating", "failed", "none"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"EpDn":UcsPropertyMeta("EpDn", "epDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SysId":UcsPropertyMeta("SysId", "sysId", "uint", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x20L, None, None, None, [], ["0-4294967295"]),
	"SysName":UcsPropertyMeta("SysName", "sysName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("InitiatorRequestorEp", "initiatorRequestorEp", "req-sysid-[SysId]-id-[Id]", _VersionMeta.Version211a, "InputOutput", 0x3fL, [], [u'initiatorGroupEp'], [None], ["read-only"])
}

