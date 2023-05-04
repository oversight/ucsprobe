import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"ForceDeploy":UcsPropertyMeta("ForceDeploy", "forceDeploy", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"InfraBundleName":UcsPropertyMeta("InfraBundleName", "infraBundleName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"InfraBundleVersion":UcsPropertyMeta("InfraBundleVersion", "infraBundleVersion", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, 0, 510, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Mode":UcsPropertyMeta("Mode", "mode", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["one-shot", "staged"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x100L, 0, 256, None, [], ["0-4294967295"]),
	"StageSize":UcsPropertyMeta("StageSize", "stageSize", "ushort", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"UpdateTrigger":UcsPropertyMeta("UpdateTrigger", "updateTrigger", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], ["0-4294967295"]),
	"Meta":UcsMoMeta("FirmwareInfraPack", "firmwareInfraPack", "fw-infra-pack-[Name]", _VersionMeta.Version211a, "InputOutput", 0xfffL, [], [u'firmwarePackItem'], ["Get", "Set"], ["admin"])
}

