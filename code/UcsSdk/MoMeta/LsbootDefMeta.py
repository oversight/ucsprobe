import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdvBootOrderApplicable":UcsPropertyMeta("AdvBootOrderApplicable", "advBootOrderApplicable", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"BootMode":UcsPropertyMeta("BootMode", "bootMode", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, ["legacy", "uefi"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x4L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"EnforceVnicName":UcsPropertyMeta("EnforceVnicName", "enforceVnicName", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Purpose":UcsPropertyMeta("Purpose", "purpose", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["operational", "utility"], ["0-4294967295"]),
	"RebootOnUpdate":UcsPropertyMeta("RebootOnUpdate", "rebootOnUpdate", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x100L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("LsbootDef", "lsbootDef", "boot-policy", _VersionMeta.Version101e, "InputOutput", 0x3ffL, [], [u'lsbootBootSecurity', u'lsbootIScsi', u'lsbootLan', u'lsbootSan', u'lsbootStorage', u'lsbootVirtualMedia'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"])
}

