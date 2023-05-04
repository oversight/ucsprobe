import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cdp":UcsPropertyMeta("Cdp", "cdp", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version102d, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version102d, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"MacRegisterMode":UcsPropertyMeta("MacRegisterMode", "macRegisterMode", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["all-host-vlans", "only-native-vlan"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version102d, UcsPropertyMeta.Naming, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"UplinkFailAction":UcsPropertyMeta("UplinkFailAction", "uplinkFailAction", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["link-down", "warning"], ["0-4294967295"]),
	"Meta":UcsMoMeta("NwctrlDefinition", "nwctrlDefinition", "nwctrl-[Name]", _VersionMeta.Version102d, "InputOutput", 0x3ffL, [], [u'dpsecMac'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-network", "ls-network-policy"])
}

