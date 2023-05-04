import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["disable", "enable"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"ExtKey":UcsPropertyMeta("ExtKey", "extKey", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 1, 33, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version221b, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{1,40}""", [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"KeyInst":UcsPropertyMeta("KeyInst", "keyInst", "ushort", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Manager":UcsPropertyMeta("Manager", "manager", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["rhev-m", "scvmm", "unmanaged", "vcenter"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, 0x40L, None, None, """[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"Own":UcsPropertyMeta("Own", "own", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["discovered", "managed"], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x100L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Uuid":UcsPropertyMeta("Uuid", "uuid", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["microsoft", "undetermined", "vmware"], ["0-4294967295"]),
	"Meta":UcsMoMeta("VmSwitch", "vmSwitch", "switch-[Name]", _VersionMeta.Version111j, "InputOutput", 0x7ffL, [], [u'extvmmUpLinkPP', u'vmVnicProfInst'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-config", "ls-config-policy", "ls-network", "pn-policy"])
}

