import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdpVifId":UcsPropertyMeta("AdpVifId", "adpVifId", "uint", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Cookie":UcsPropertyMeta("Cookie", "cookie", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"LinkState":UcsPropertyMeta("LinkState", "linkState", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["admin-down", "down", "error", "unallocated", "unavailable", "unknown", "up"], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["active", "admin-down", "error", "link-down", "passive", "unknown"], ["0-4294967295"]),
	"PhSwitchId":UcsPropertyMeta("PhSwitchId", "phSwitchId", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, 0x4L, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"PhsAccessCardId":UcsPropertyMeta("PhsAccessCardId", "phsAccessCardId", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PhsAccessPortId":UcsPropertyMeta("PhsAccessPortId", "phsAccessPortId", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PhsBorderCardId":UcsPropertyMeta("PhsBorderCardId", "phsBorderCardId", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PhsBorderPortId":UcsPropertyMeta("PhsBorderPortId", "phsBorderPortId", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"StateQual":UcsPropertyMeta("StateQual", "stateQual", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"StatusChangeTs":UcsPropertyMeta("StatusChangeTs", "statusChangeTs", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"VStatus":UcsPropertyMeta("VStatus", "vStatus", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["offline", "online", "unknown"], ["0-4294967295"]),
	"VcDn":UcsPropertyMeta("VcDn", "vcDn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"VifId":UcsPropertyMeta("VifId", "vifId", "uint", _VersionMeta.Version111j, UcsPropertyMeta.Naming, 0x20L, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VmVif", "vmVif", "sw-[PhSwitchId]vif-[VifId]", _VersionMeta.Version111j, "InputOutput", 0x3fL, [], [u'faultInst'], ["Get"], ["admin"])
}

