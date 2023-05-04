import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"FwVersionHi":UcsPropertyMeta("FwVersionHi", "fwVersionHi", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"FwVersionLo":UcsPropertyMeta("FwVersionLo", "fwVersionLo", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"FwVersionOpr":UcsPropertyMeta("FwVersionOpr", "fwVersionOpr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["gt", "lt", "none", "range"], ["0-4294967295"]),
	"Maximum":UcsPropertyMeta("Maximum", "maximum", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["unspecified"], ["0-65535", "4294967295-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[ !#$%\(\)\*\+,\-\./:;\?@\[\\\]\^_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x40L, None, None, None, ["eth-flow-monitoring-netflow", "fcoe", "non-virtualized-eth-if", "non-virtualized-fc-if", "path-encap-consolidated", "path-encap-virtual", "protected-eth-if", "protected-fc-if", "protected-fcoe", "uplink-aggregation", "virtualized-eth-if", "virtualized-eth-sriov", "virtualized-eth-sriov-usnic", "virtualized-eth-vmq", "virtualized-fc-if", "virtualized-fc-sriov", "virtualized-scsi-if"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorCapQual", "adaptorCapQual", "cap-[Type]", _VersionMeta.Version101e, "InputOutput", 0x7fL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "pn-policy"])
}

