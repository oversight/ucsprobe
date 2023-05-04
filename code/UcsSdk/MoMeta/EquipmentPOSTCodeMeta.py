import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Code":UcsPropertyMeta("Code", "code", "string", _VersionMeta.Version101e, UcsPropertyMeta.CreateOnly, 0x2L, 0, 510, None, [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,384}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"GlobalId":UcsPropertyMeta("GlobalId", "globalId", "string", _VersionMeta.Version101e, UcsPropertyMeta.CreateOnly, 0x8L, None, None, None, ["No Errors"], ["0-4294967295"]),
	"LocalId":UcsPropertyMeta("LocalId", "localId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x10L, None, None, None, ["No Errors"], ["0-4294967295"]),
	"Method":UcsPropertyMeta("Method", "method", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """((POST|defaultValue|config-check|diag-check|sel-check),){0,4}(POST|defaultValue|config-check|diag-check|sel-check){0,1}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Recoverable":UcsPropertyMeta("Recoverable", "recoverable", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["non-recoverable", "recoverable", "unknown"], ["0-4294967295"]),
	"RecoveryAction":UcsPropertyMeta("RecoveryAction", "recoveryAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,384}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Severity":UcsPropertyMeta("Severity", "severity", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentPOSTCode", "equipmentPOSTCode", "code-[LocalId]", _VersionMeta.Version101e, "InputOutput", 0xffL, [], [], ["Get"], ["read-only"])
}

