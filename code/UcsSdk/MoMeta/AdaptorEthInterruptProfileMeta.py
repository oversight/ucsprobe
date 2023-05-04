import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CoalescingTime":UcsPropertyMeta("CoalescingTime", "coalescingTime", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["0-65535"]),
	"CoalescingType":UcsPropertyMeta("CoalescingType", "coalescingType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["idle", "min"], ["0-4294967295"]),
	"Count":UcsPropertyMeta("Count", "count", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["1-514"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Mode":UcsPropertyMeta("Mode", "mode", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["intx", "msi", "msi-x"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthInterruptProfile", "adaptorEthInterruptProfile", "eth-int", _VersionMeta.Version101e, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"])
}

