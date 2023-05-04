import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["off", "on"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IntervalDays":UcsPropertyMeta("IntervalDays", "intervalDays", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["1-30"]),
	"LastDeadline":UcsPropertyMeta("LastDeadline", "lastDeadline", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"MaximumRetryCount":UcsPropertyMeta("MaximumRetryCount", "maximumRetryCount", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-5"]),
	"MinimumSendNowIntervalSeconds":UcsPropertyMeta("MinimumSendNowIntervalSeconds", "minimumSendNowIntervalSeconds", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["1-2000000000"]),
	"NextDeadline":UcsPropertyMeta("NextDeadline", "nextDeadline", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"PollIntervalSeconds":UcsPropertyMeta("PollIntervalSeconds", "pollIntervalSeconds", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["10-3600"]),
	"RetryCount":UcsPropertyMeta("RetryCount", "retryCount", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RetryDelayMinutes":UcsPropertyMeta("RetryDelayMinutes", "retryDelayMinutes", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-60"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x100L, 0, 256, None, [], ["0-4294967295"]),
	"SendNow":UcsPropertyMeta("SendNow", "sendNow", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TimeOfDayHour":UcsPropertyMeta("TimeOfDayHour", "timeOfDayHour", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, [], ["0-23"]),
	"TimeOfDayMinute":UcsPropertyMeta("TimeOfDayMinute", "timeOfDayMinute", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["0-59"]),
	"TimeOfLastAttempt":UcsPropertyMeta("TimeOfLastAttempt", "timeOfLastAttempt", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"TimeOfLastSuccess":UcsPropertyMeta("TimeOfLastSuccess", "timeOfLastSuccess", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"Meta":UcsMoMeta("CallhomePeriodicSystemInventory", "callhomePeriodicSystemInventory", "periodicsysteminventory", _VersionMeta.Version101e, "InputOutput", 0x1fffL, [], [], ["Get", "Set"], ["admin", "operations"])
}

