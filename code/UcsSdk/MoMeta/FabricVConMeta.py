import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"EquipmentDn":UcsPropertyMeta("EquipmentDn", "equipmentDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Fabric":UcsPropertyMeta("Fabric", "fabric", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["A", "B", "NONE", "any"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, 0x8L, None, None, None, ["1", "2", "3", "4"], ["0-4294967295"]),
	"InstType":UcsPropertyMeta("InstType", "instType", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["auto", "manual", "policy"], ["0-4294967295"]),
	"Placement":UcsPropertyMeta("Placement", "placement", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["auto", "physical"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Select":UcsPropertyMeta("Select", "select", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["all", "assigned-only", "dynamic-only", "exclude-dynamic", "exclude-unassigned", "exclude-usnic", "unassigned-only", "usnic-only"], ["0-4294967295"]),
	"Share":UcsPropertyMeta("Share", "share", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["different-transport", "exclusive-only", "exclusive-preferred", "same-transport", "shared"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((fc|ethernet|defaultValue),){0,2}(fc|ethernet|defaultValue){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricVCon", "fabricVCon", "vcon-[Id]", _VersionMeta.Version111j, "InputOutput", 0x7ffL, [], [], ["Add", "Get", "Set"], ["admin", "ext-lan-policy", "ls-network", "ls-network-policy", "ls-server-policy", "ls-storage-policy"])
}

