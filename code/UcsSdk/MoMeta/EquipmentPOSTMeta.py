import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Code":UcsPropertyMeta("Code", "code", "string", _VersionMeta.Version111j, UcsPropertyMeta.CreateOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Created":UcsPropertyMeta("Created", "created", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,384}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"GlobalId":UcsPropertyMeta("GlobalId", "globalId", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["No Errors"], ["0-4294967295"]),
	"LocalId":UcsPropertyMeta("LocalId", "localId", "string", _VersionMeta.Version111j, UcsPropertyMeta.CreateOnly, None, None, None, None, ["No Errors"], ["0-4294967295"]),
	"Method":UcsPropertyMeta("Method", "method", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """((POST|defaultValue|config-check|diag-check|sel-check),){0,4}(POST|defaultValue|config-check|diag-check|sel-check){0,1}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Recoverable":UcsPropertyMeta("Recoverable", "recoverable", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["non-recoverable", "recoverable", "unknown"], ["0-4294967295"]),
	"RecoveryAction":UcsPropertyMeta("RecoveryAction", "recoveryAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,384}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Severity":UcsPropertyMeta("Severity", "severity", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version111j, UcsPropertyMeta.CreateOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Value":UcsPropertyMeta("Value", "value", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentPOST", "equipmentPOST", "code-[GlobalId]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

