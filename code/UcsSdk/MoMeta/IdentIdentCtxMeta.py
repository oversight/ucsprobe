import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Assigned":UcsPropertyMeta("Assigned", "assigned", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConsDn":UcsPropertyMeta("ConsDn", "consDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"ConsType":UcsPropertyMeta("ConsType", "consType", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["chassis", "server", "vhba", "vm", "vmnic", "vnic"], ["0-4294967295"]),
	"DefinedInIdm":UcsPropertyMeta("DefinedInIdm", "definedInIdm", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["no", "yes"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"IdentPoolName":UcsPropertyMeta("IdentPoolName", "identPoolName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"IdentType":UcsPropertyMeta("IdentType", "identType", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ipV4", "ipV6", "iqn", "mac", "uuid", "vlan", "wwnn", "wwpn"], ["0-4294967295"]),
	"Intent":UcsPropertyMeta("Intent", "intent", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["add-pooled", "assign", "delete-pooled", "requisition", "unassign"], ["0-4294967295"]),
	"PoolDn":UcsPropertyMeta("PoolDn", "poolDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PoolOrgDn":UcsPropertyMeta("PoolOrgDn", "poolOrgDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PooledId":UcsPropertyMeta("PooledId", "pooledId", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RetStatus":UcsPropertyMeta("RetStatus", "retStatus", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["assigned-by-other", "failed", "out-of-sync", "succeeded", "synced"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"SeqNum":UcsPropertyMeta("SeqNum", "seqNum", "uint", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x8L, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SupplId1":UcsPropertyMeta("SupplId1", "supplId1", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"SupplId2":UcsPropertyMeta("SupplId2", "supplId2", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"SupplId3":UcsPropertyMeta("SupplId3", "supplId3", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"SupplId4":UcsPropertyMeta("SupplId4", "supplId4", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("IdentIdentCtx", "identIdentCtx", "IdCtx-[SeqNum]", _VersionMeta.Version211a, "InputOutput", 0x1fL, [], [], [None], ["read-only"])
}

