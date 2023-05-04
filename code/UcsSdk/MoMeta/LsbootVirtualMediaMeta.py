import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Access":UcsPropertyMeta("Access", "access", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x1L, None, None, None, ["read-only", "read-only-local", "read-only-remote", "read-only-remote-cimc", "read-write", "read-write-drive", "read-write-local", "read-write-remote", "read-write-remote-cimc"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"LunId":UcsPropertyMeta("LunId", "lunId", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"MappingName":UcsPropertyMeta("MappingName", "mappingName", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Order":UcsPropertyMeta("Order", "order", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["1-16"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["iscsi", "lan", "san", "storage", "virtual-media"], ["0-4294967295"]),
	"Meta":UcsMoMeta("LsbootVirtualMedia", "lsbootVirtualMedia", "[Access]-vm", _VersionMeta.Version101e, "InputOutput", 0xffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"])
}

