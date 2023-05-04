import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Access":UcsPropertyMeta("Access", "access", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["read-only", "read-only-local", "read-only-remote", "read-only-remote-cimc", "read-write", "read-write-drive", "read-write-local", "read-write-remote", "read-write-remote-cimc"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Order":UcsPropertyMeta("Order", "order", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["1-16"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["iscsi", "lan", "san", "storage", "virtual-media"], ["0-4294967295"]),
	"Meta":UcsMoMeta("LsbootStorage", "lsbootStorage", "storage", _VersionMeta.Version101e, "InputOutput", 0x1fL, [], [u'lsbootLocalStorage', u'lsbootSanImage'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"])
}

