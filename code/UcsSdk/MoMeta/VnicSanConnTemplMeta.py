import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IdentPoolName":UcsPropertyMeta("IdentPoolName", "identPoolName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"MaxDataFieldSize":UcsPropertyMeta("MaxDataFieldSize", "maxDataFieldSize", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["256-2112"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"NwCtrlPolicyName":UcsPropertyMeta("NwCtrlPolicyName", "nwCtrlPolicyName", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperIdentPoolName":UcsPropertyMeta("OperIdentPoolName", "operIdentPoolName", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperQosPolicyName":UcsPropertyMeta("OperQosPolicyName", "operQosPolicyName", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperStatsPolicyName":UcsPropertyMeta("OperStatsPolicyName", "operStatsPolicyName", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PinToGroupName":UcsPropertyMeta("PinToGroupName", "pinToGroupName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"QosPolicyName":UcsPropertyMeta("QosPolicyName", "qosPolicyName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"StatsPolicyName":UcsPropertyMeta("StatsPolicyName", "statsPolicyName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Target":UcsPropertyMeta("Target", "target", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((vm|adaptor|defaultValue),){0,2}(vm|adaptor|defaultValue){0,1}""", [], ["0-4294967295"]),
	"TemplType":UcsPropertyMeta("TemplType", "templType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, ["initial-template", "updating-template"], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicSanConnTempl", "vnicSanConnTempl", "san-conn-templ-[Name]", _VersionMeta.Version101e, "InputOutput", 0x3fffL, [], [u'faultInst', u'vnicFcIf'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-storage", "ls-storage-policy"])
}

