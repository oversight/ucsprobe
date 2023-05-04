import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Alias":UcsPropertyMeta("Alias", "alias", "string", _VersionMeta.Version201m, UcsPropertyMeta.Naming, 0x1L, 1, 510, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"MgmtPlane":UcsPropertyMeta("MgmtPlane", "mgmtPlane", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["rhev-m", "scvmm", "unmanaged", "vcenter"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VSwitchId":UcsPropertyMeta("VSwitchId", "vSwitchId", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{1,40}""", [], ["0-4294967295"]),
	"VSwitchName":UcsPropertyMeta("VSwitchName", "vSwitchName", "string", _VersionMeta.Version201m, UcsPropertyMeta.Naming, 0x20L, None, None, """[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicOProfileAlias", "vnicOProfileAlias", "swid-[VSwitchName]alias-[Alias]", _VersionMeta.Version201m, "InputOutput", 0x3fL, [], [], ["Get"], ["read-only"])
}

