import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Addr":UcsPropertyMeta("Addr", "addr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"NicDn":UcsPropertyMeta("NicDn", "nicDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Owner":UcsPropertyMeta("Owner", "owner", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["conn_policy", "logical", "physical", "policy", "unknown"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], ["0-4294967295"]),
	"VnicDn":UcsPropertyMeta("VnicDn", "vnicDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicFcLif", "vnicFcLif", "eth-lif-[Name]", _VersionMeta.Version101e, "InputOutput", 0x7fL, [], [u'vnicLifVsan'], ["Get"], ["read-only"])
}

