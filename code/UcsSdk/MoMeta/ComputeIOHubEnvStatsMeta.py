import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version131c, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Temperature":UcsPropertyMeta("Temperature", "temperature", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"TemperatureAvg":UcsPropertyMeta("TemperatureAvg", "temperatureAvg", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"TemperatureMax":UcsPropertyMeta("TemperatureMax", "temperatureMax", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"TemperatureMin":UcsPropertyMeta("TemperatureMin", "temperatureMin", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ComputeIOHubEnvStats", "computeIOHubEnvStats", "iohub-stats", _VersionMeta.Version131c, "OutputOnly", 0x0L, [], [u'computeIOHubEnvStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

