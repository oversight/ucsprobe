import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Action":UcsPropertyMeta("Action", "action", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x1L, None, None, """((defaultValue|none|log-full|on-clear|timer|on-assoc-change),){0,5}(defaultValue|none|log-full|on-clear|timer|on-assoc-change){0,1}""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ClearOnBackup":UcsPropertyMeta("ClearOnBackup", "clearOnBackup", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Format":UcsPropertyMeta("Format", "format", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["ascii", "binary"], ["0-4294967295"]),
	"Hostname":UcsPropertyMeta("Hostname", "hostname", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"Interval":UcsPropertyMeta("Interval", "interval", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["1hour", "1month", "1week", "24hours", "2hours", "4hours", "8hours", "never"], ["0-4294967295"]),
	"Proto":UcsPropertyMeta("Proto", "proto", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], ["0-4294967295"]),
	"Pwd":UcsPropertyMeta("Pwd", "pwd", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x100L, 0, 64, None, [], ["0-4294967295"]),
	"RemotePath":UcsPropertyMeta("RemotePath", "remotePath", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x200L, 1, 128, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"User":UcsPropertyMeta("User", "user", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x1000L, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SysdebugBackupBehavior", "sysdebugBackupBehavior", "backup", _VersionMeta.Version111j, "InputOutput", 0x1fffL, [], [], ["Get", "Set"], ["admin", "operations"])
}

