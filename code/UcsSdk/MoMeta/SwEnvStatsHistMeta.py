import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"FanCtrlrInlet1":UcsPropertyMeta("FanCtrlrInlet1", "fanCtrlrInlet1", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet1Avg":UcsPropertyMeta("FanCtrlrInlet1Avg", "fanCtrlrInlet1Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet1Max":UcsPropertyMeta("FanCtrlrInlet1Max", "fanCtrlrInlet1Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet1Min":UcsPropertyMeta("FanCtrlrInlet1Min", "fanCtrlrInlet1Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet2":UcsPropertyMeta("FanCtrlrInlet2", "fanCtrlrInlet2", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet2Avg":UcsPropertyMeta("FanCtrlrInlet2Avg", "fanCtrlrInlet2Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet2Max":UcsPropertyMeta("FanCtrlrInlet2Max", "fanCtrlrInlet2Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet2Min":UcsPropertyMeta("FanCtrlrInlet2Min", "fanCtrlrInlet2Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet3":UcsPropertyMeta("FanCtrlrInlet3", "fanCtrlrInlet3", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet3Avg":UcsPropertyMeta("FanCtrlrInlet3Avg", "fanCtrlrInlet3Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet3Max":UcsPropertyMeta("FanCtrlrInlet3Max", "fanCtrlrInlet3Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet3Min":UcsPropertyMeta("FanCtrlrInlet3Min", "fanCtrlrInlet3Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet4":UcsPropertyMeta("FanCtrlrInlet4", "fanCtrlrInlet4", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet4Avg":UcsPropertyMeta("FanCtrlrInlet4Avg", "fanCtrlrInlet4Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet4Max":UcsPropertyMeta("FanCtrlrInlet4Max", "fanCtrlrInlet4Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"FanCtrlrInlet4Min":UcsPropertyMeta("FanCtrlrInlet4Min", "fanCtrlrInlet4Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"MainBoardOutlet1":UcsPropertyMeta("MainBoardOutlet1", "mainBoardOutlet1", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MainBoardOutlet1Avg":UcsPropertyMeta("MainBoardOutlet1Avg", "mainBoardOutlet1Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MainBoardOutlet1Max":UcsPropertyMeta("MainBoardOutlet1Max", "mainBoardOutlet1Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MainBoardOutlet1Min":UcsPropertyMeta("MainBoardOutlet1Min", "mainBoardOutlet1Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MainBoardOutlet2":UcsPropertyMeta("MainBoardOutlet2", "mainBoardOutlet2", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MainBoardOutlet2Avg":UcsPropertyMeta("MainBoardOutlet2Avg", "mainBoardOutlet2Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MainBoardOutlet2Max":UcsPropertyMeta("MainBoardOutlet2Max", "mainBoardOutlet2Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MainBoardOutlet2Min":UcsPropertyMeta("MainBoardOutlet2Min", "mainBoardOutlet2Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"PsuCtrlrInlet1":UcsPropertyMeta("PsuCtrlrInlet1", "psuCtrlrInlet1", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"PsuCtrlrInlet1Avg":UcsPropertyMeta("PsuCtrlrInlet1Avg", "psuCtrlrInlet1Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"PsuCtrlrInlet1Max":UcsPropertyMeta("PsuCtrlrInlet1Max", "psuCtrlrInlet1Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"PsuCtrlrInlet1Min":UcsPropertyMeta("PsuCtrlrInlet1Min", "psuCtrlrInlet1Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"PsuCtrlrInlet2":UcsPropertyMeta("PsuCtrlrInlet2", "psuCtrlrInlet2", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"PsuCtrlrInlet2Avg":UcsPropertyMeta("PsuCtrlrInlet2Avg", "psuCtrlrInlet2Avg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"PsuCtrlrInlet2Max":UcsPropertyMeta("PsuCtrlrInlet2Max", "psuCtrlrInlet2Max", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"PsuCtrlrInlet2Min":UcsPropertyMeta("PsuCtrlrInlet2Min", "psuCtrlrInlet2Min", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SwEnvStatsHist", "swEnvStatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

