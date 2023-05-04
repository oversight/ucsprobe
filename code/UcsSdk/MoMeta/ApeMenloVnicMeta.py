import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Cookie":UcsPropertyMeta("Cookie", "cookie", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["0-4294967295"]),
	"Cos":UcsPropertyMeta("Cos", "cos", "byte", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Mac":UcsPropertyMeta("Mac", "mac", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"NicDn":UcsPropertyMeta("NicDn", "nicDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PifId":UcsPropertyMeta("PifId", "pifId", "byte", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"State":UcsPropertyMeta("State", "state", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["CreatePend", "Creating", "DestroyPend", "Destroying", "ModifyPend", "Modifying", "Present", "Unknown"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Eth", "Fc", "Scsi", "Unknown"], ["0-4294967295"]),
	"UplinkPortId":UcsPropertyMeta("UplinkPortId", "uplinkPortId", "byte", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, [], ["0-4294967295"]),
	"VifId":UcsPropertyMeta("VifId", "vifId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, [], ["0-4294967295"]),
	"VifType":UcsPropertyMeta("VifType", "vifType", "byte", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["0-4294967295"]),
	"VlanId":UcsPropertyMeta("VlanId", "vlanId", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, [], ["0-4294967295"]),
	"Vntag":UcsPropertyMeta("Vntag", "vntag", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, None, [], ["0-4294967295"]),
	"Wwnn":UcsPropertyMeta("Wwnn", "wwnn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"Wwpn":UcsPropertyMeta("Wwpn", "wwpn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApeMenloVnic", "apeMenloVnic", "AdapterVnic-[Name]", _VersionMeta.Version101e, "InputOutput", 0x1ffffL, [], [u'apeMenloVnicStats', u'apePaloVnicStats'], [None], ["read-only"])
}

