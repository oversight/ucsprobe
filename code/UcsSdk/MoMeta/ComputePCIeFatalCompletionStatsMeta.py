import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AbortErrors":UcsPropertyMeta("AbortErrors", "AbortErrors", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors15Min":UcsPropertyMeta("AbortErrors15Min", "AbortErrors15Min", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors15MinH":UcsPropertyMeta("AbortErrors15MinH", "AbortErrors15MinH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors1Day":UcsPropertyMeta("AbortErrors1Day", "AbortErrors1Day", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors1DayH":UcsPropertyMeta("AbortErrors1DayH", "AbortErrors1DayH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors1Hour":UcsPropertyMeta("AbortErrors1Hour", "AbortErrors1Hour", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors1HourH":UcsPropertyMeta("AbortErrors1HourH", "AbortErrors1HourH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors1Week":UcsPropertyMeta("AbortErrors1Week", "AbortErrors1Week", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors1WeekH":UcsPropertyMeta("AbortErrors1WeekH", "AbortErrors1WeekH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors2Weeks":UcsPropertyMeta("AbortErrors2Weeks", "AbortErrors2Weeks", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AbortErrors2WeeksH":UcsPropertyMeta("AbortErrors2WeeksH", "AbortErrors2WeeksH", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors":UcsPropertyMeta("TimeoutErrors", "TimeoutErrors", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors15Min":UcsPropertyMeta("TimeoutErrors15Min", "TimeoutErrors15Min", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors15MinH":UcsPropertyMeta("TimeoutErrors15MinH", "TimeoutErrors15MinH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors1Day":UcsPropertyMeta("TimeoutErrors1Day", "TimeoutErrors1Day", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors1DayH":UcsPropertyMeta("TimeoutErrors1DayH", "TimeoutErrors1DayH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors1Hour":UcsPropertyMeta("TimeoutErrors1Hour", "TimeoutErrors1Hour", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors1HourH":UcsPropertyMeta("TimeoutErrors1HourH", "TimeoutErrors1HourH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors1Week":UcsPropertyMeta("TimeoutErrors1Week", "TimeoutErrors1Week", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors1WeekH":UcsPropertyMeta("TimeoutErrors1WeekH", "TimeoutErrors1WeekH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors2Weeks":UcsPropertyMeta("TimeoutErrors2Weeks", "TimeoutErrors2Weeks", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeoutErrors2WeeksH":UcsPropertyMeta("TimeoutErrors2WeeksH", "TimeoutErrors2WeeksH", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"UnexpectedErrors":UcsPropertyMeta("UnexpectedErrors", "unexpectedErrors", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors15Min":UcsPropertyMeta("UnexpectedErrors15Min", "unexpectedErrors15Min", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors15MinH":UcsPropertyMeta("UnexpectedErrors15MinH", "unexpectedErrors15MinH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors1Day":UcsPropertyMeta("UnexpectedErrors1Day", "unexpectedErrors1Day", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors1DayH":UcsPropertyMeta("UnexpectedErrors1DayH", "unexpectedErrors1DayH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors1Hour":UcsPropertyMeta("UnexpectedErrors1Hour", "unexpectedErrors1Hour", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors1HourH":UcsPropertyMeta("UnexpectedErrors1HourH", "unexpectedErrors1HourH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors1Week":UcsPropertyMeta("UnexpectedErrors1Week", "unexpectedErrors1Week", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors1WeekH":UcsPropertyMeta("UnexpectedErrors1WeekH", "unexpectedErrors1WeekH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors2Weeks":UcsPropertyMeta("UnexpectedErrors2Weeks", "unexpectedErrors2Weeks", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnexpectedErrors2WeeksH":UcsPropertyMeta("UnexpectedErrors2WeeksH", "unexpectedErrors2WeeksH", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ComputePCIeFatalCompletionStats", "computePCIeFatalCompletionStats", "pciefat-completion-stats", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "operations", "read-only"])
}

