import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack", "user-discard"], ["0-4294967295"]),
	"AutoDelete":UcsPropertyMeta("AutoDelete", "autoDelete", "string", _VersionMeta.Version222c, UcsPropertyMeta.CreateOnly, 0x2L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"BackupDate":UcsPropertyMeta("BackupDate", "backupDate", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"BackupIssue":UcsPropertyMeta("BackupIssue", "backupIssue", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["none", "outdated"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, 0x10L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"IgnoreCap":UcsPropertyMeta("IgnoreCap", "ignoreCap", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperScheduler":UcsPropertyMeta("OperScheduler", "operScheduler", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"Scheduler":UcsPropertyMeta("Scheduler", "scheduler", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("MgmtBackupPolicyConfig", "mgmtBackupPolicyConfig", "bkup-policy-cfg", _VersionMeta.Version222c, "InputOutput", 0xfffL, [], [u'faultInst', u'trigLocalSched'], [None], ["admin"])
}

