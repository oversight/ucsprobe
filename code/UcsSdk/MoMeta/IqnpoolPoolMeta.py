import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Assigned":UcsPropertyMeta("Assigned", "assigned", "uint", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AssignmentOrder":UcsPropertyMeta("AssignmentOrder", "assignmentOrder", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["default", "sequential"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version201m, UcsPropertyMeta.Naming, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{1,32}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Prefix":UcsPropertyMeta("Prefix", "prefix", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[0-9a-zA-Z\.:-]{1,150}$""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Size":UcsPropertyMeta("Size", "size", "uint", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("IqnpoolPool", "iqnpoolPool", "iqn-pool-[Name]", _VersionMeta.Version201m, "InputOutput", 0x1ffL, [], [u'faultInst', u'iqnpoolBlock', u'iqnpoolPooled'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-storage-policy"])
}

