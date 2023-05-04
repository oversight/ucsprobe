import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DefGw":UcsPropertyMeta("DefGw", "defGw", "string", _VersionMeta.Version101e, UcsPropertyMeta.CreateOnly, 0x2L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"From":UcsPropertyMeta("From", "from", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"PrimDns":UcsPropertyMeta("PrimDns", "primDns", "string", _VersionMeta.Version201m, UcsPropertyMeta.CreateOnly, 0x10L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"SecDns":UcsPropertyMeta("SecDns", "secDns", "string", _VersionMeta.Version201m, UcsPropertyMeta.CreateOnly, 0x40L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Subnet":UcsPropertyMeta("Subnet", "subnet", "string", _VersionMeta.Version101e, UcsPropertyMeta.CreateOnly, 0x100L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"To":UcsPropertyMeta("To", "to", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x200L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("IppoolBlock", "ippoolBlock", "block-[From]-[To]", _VersionMeta.Version101e, "InputOutput", 0x3ffL, [], [], ["Add", "Get", "Remove"], ["admin", "ls-network-policy"])
}

