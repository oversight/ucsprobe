import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Cookie":UcsPropertyMeta("Cookie", "cookie", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["0-4294967295"]),
	"Cos":UcsPropertyMeta("Cos", "cos", "byte", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Failover":UcsPropertyMeta("Failover", "failover", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Mac":UcsPropertyMeta("Mac", "mac", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"Mtu":UcsPropertyMeta("Mtu", "mtu", "ushort", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"NicDn":UcsPropertyMeta("NicDn", "nicDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PassThru":UcsPropertyMeta("PassThru", "passThru", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"State":UcsPropertyMeta("State", "state", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["CreatePend", "Creating", "DestroyPend", "Destroying", "ModifyPend", "Modifying", "Present", "Unknown"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"StdbyVifId":UcsPropertyMeta("StdbyVifId", "stdbyVifId", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Eth", "Fc", "Scsi", "Unknown"], ["0-4294967295"]),
	"UplinkPortId":UcsPropertyMeta("UplinkPortId", "uplinkPortId", "byte", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, [], ["0-4294967295"]),
	"VifId":UcsPropertyMeta("VifId", "vifId", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, None, [], ["0-4294967295"]),
	"VifType":UcsPropertyMeta("VifType", "vifType", "byte", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x8000L, None, None, None, [], ["0-4294967295"]),
	"VlanId":UcsPropertyMeta("VlanId", "vlanId", "ushort", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10000L, None, None, None, [], ["0-4294967295"]),
	"VmWare":UcsPropertyMeta("VmWare", "vmWare", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20000L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Vntag":UcsPropertyMeta("Vntag", "vntag", "ushort", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40000L, None, None, None, [], ["0-4294967295"]),
	"Wwnn":UcsPropertyMeta("Wwnn", "wwnn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApePaloVnic", "apePaloVnic", "AdapterVnic-[Name]", _VersionMeta.Version211a, "InputOutput", 0xfffffL, [], [u'apeMenloVnicStats', u'apePaloVnicStats'], [None], ["read-only"])
}

