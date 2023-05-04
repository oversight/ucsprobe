import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"BwPercent":UcsPropertyMeta("BwPercent", "bwPercent", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-100"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Cos":UcsPropertyMeta("Cos", "cos", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["any"], ["0-6", "255-255"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Drop":UcsPropertyMeta("Drop", "drop", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["drop", "no-drop"], ["0-4294967295"]),
	"Mtu":UcsPropertyMeta("Mtu", "mtu", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["fc", "normal"], ["0-4294967295"]),
	"MulticastOptimize":UcsPropertyMeta("MulticastOptimize", "multicastOptimize", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Priority":UcsPropertyMeta("Priority", "priority", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x100L, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Weight":UcsPropertyMeta("Weight", "weight", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["best-effort", "none"], ["0-10"]),
	"Meta":UcsMoMeta("QosclassEthClassified", "qosclassEthClassified", "class-[Priority]", _VersionMeta.Version101e, "InputOutput", 0xfffL, [], [], ["Get", "Set"], ["admin", "ext-lan-qos", "ext-san-qos", "ls-network", "ls-network-policy", "ls-qos-policy"])
}

