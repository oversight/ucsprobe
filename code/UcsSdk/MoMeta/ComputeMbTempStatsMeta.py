import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"FmTempSenIo":UcsPropertyMeta("FmTempSenIo", "fmTempSenIo", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenIoAvg":UcsPropertyMeta("FmTempSenIoAvg", "fmTempSenIoAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenIoMax":UcsPropertyMeta("FmTempSenIoMax", "fmTempSenIoMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenIoMin":UcsPropertyMeta("FmTempSenIoMin", "fmTempSenIoMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRear":UcsPropertyMeta("FmTempSenRear", "fmTempSenRear", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearAvg":UcsPropertyMeta("FmTempSenRearAvg", "fmTempSenRearAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearL":UcsPropertyMeta("FmTempSenRearL", "fmTempSenRearL", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearLAvg":UcsPropertyMeta("FmTempSenRearLAvg", "fmTempSenRearLAvg", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearLMax":UcsPropertyMeta("FmTempSenRearLMax", "fmTempSenRearLMax", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearLMin":UcsPropertyMeta("FmTempSenRearLMin", "fmTempSenRearLMin", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearMax":UcsPropertyMeta("FmTempSenRearMax", "fmTempSenRearMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearMin":UcsPropertyMeta("FmTempSenRearMin", "fmTempSenRearMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearR":UcsPropertyMeta("FmTempSenRearR", "fmTempSenRearR", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearRAvg":UcsPropertyMeta("FmTempSenRearRAvg", "fmTempSenRearRAvg", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearRMax":UcsPropertyMeta("FmTempSenRearRMax", "fmTempSenRearRMax", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FmTempSenRearRMin":UcsPropertyMeta("FmTempSenRearRMin", "fmTempSenRearRMin", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ComputeMbTempStats", "computeMbTempStats", "temp-stats", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [u'computeMbTempStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

