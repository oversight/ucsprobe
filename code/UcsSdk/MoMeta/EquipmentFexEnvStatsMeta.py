import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Die1":UcsPropertyMeta("Die1", "die1", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Die1Avg":UcsPropertyMeta("Die1Avg", "die1Avg", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Die1Max":UcsPropertyMeta("Die1Max", "die1Max", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Die1Min":UcsPropertyMeta("Die1Min", "die1Min", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Inlet":UcsPropertyMeta("Inlet", "inlet", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Inlet1":UcsPropertyMeta("Inlet1", "inlet1", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Inlet1Avg":UcsPropertyMeta("Inlet1Avg", "inlet1Avg", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Inlet1Max":UcsPropertyMeta("Inlet1Max", "inlet1Max", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Inlet1Min":UcsPropertyMeta("Inlet1Min", "inlet1Min", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"InletAvg":UcsPropertyMeta("InletAvg", "inletAvg", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"InletMax":UcsPropertyMeta("InletMax", "inletMax", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"InletMin":UcsPropertyMeta("InletMin", "inletMin", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"InputStatus":UcsPropertyMeta("InputStatus", "inputStatus", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Outlet1":UcsPropertyMeta("Outlet1", "outlet1", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Outlet1Avg":UcsPropertyMeta("Outlet1Avg", "outlet1Avg", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Outlet1Max":UcsPropertyMeta("Outlet1Max", "outlet1Max", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Outlet1Min":UcsPropertyMeta("Outlet1Min", "outlet1Min", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Outlet2":UcsPropertyMeta("Outlet2", "outlet2", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Outlet2Avg":UcsPropertyMeta("Outlet2Avg", "outlet2Avg", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Outlet2Max":UcsPropertyMeta("Outlet2Max", "outlet2Max", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Outlet2Min":UcsPropertyMeta("Outlet2Min", "outlet2Min", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentFexEnvStats", "equipmentFexEnvStats", "env-stats", _VersionMeta.Version141i, "OutputOnly", 0x0L, [], [u'equipmentFexEnvStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

