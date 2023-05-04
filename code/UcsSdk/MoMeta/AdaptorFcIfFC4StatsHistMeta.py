import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ControlRequests":UcsPropertyMeta("ControlRequests", "controlRequests", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ControlRequestsDelta":UcsPropertyMeta("ControlRequestsDelta", "controlRequestsDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ControlRequestsDeltaAvg":UcsPropertyMeta("ControlRequestsDeltaAvg", "controlRequestsDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ControlRequestsDeltaMax":UcsPropertyMeta("ControlRequestsDeltaMax", "controlRequestsDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ControlRequestsDeltaMin":UcsPropertyMeta("ControlRequestsDeltaMin", "controlRequestsDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"InputMegabytes":UcsPropertyMeta("InputMegabytes", "inputMegabytes", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputMegabytesDelta":UcsPropertyMeta("InputMegabytesDelta", "inputMegabytesDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputMegabytesDeltaAvg":UcsPropertyMeta("InputMegabytesDeltaAvg", "inputMegabytesDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputMegabytesDeltaMax":UcsPropertyMeta("InputMegabytesDeltaMax", "inputMegabytesDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputMegabytesDeltaMin":UcsPropertyMeta("InputMegabytesDeltaMin", "inputMegabytesDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputRequests":UcsPropertyMeta("InputRequests", "inputRequests", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputRequestsDelta":UcsPropertyMeta("InputRequestsDelta", "inputRequestsDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputRequestsDeltaAvg":UcsPropertyMeta("InputRequestsDeltaAvg", "inputRequestsDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputRequestsDeltaMax":UcsPropertyMeta("InputRequestsDeltaMax", "inputRequestsDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"InputRequestsDeltaMin":UcsPropertyMeta("InputRequestsDeltaMin", "inputRequestsDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"OutputMegabytes":UcsPropertyMeta("OutputMegabytes", "outputMegabytes", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputMegabytesDelta":UcsPropertyMeta("OutputMegabytesDelta", "outputMegabytesDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputMegabytesDeltaAvg":UcsPropertyMeta("OutputMegabytesDeltaAvg", "outputMegabytesDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputMegabytesDeltaMax":UcsPropertyMeta("OutputMegabytesDeltaMax", "outputMegabytesDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputMegabytesDeltaMin":UcsPropertyMeta("OutputMegabytesDeltaMin", "outputMegabytesDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputRequests":UcsPropertyMeta("OutputRequests", "outputRequests", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputRequestsDelta":UcsPropertyMeta("OutputRequestsDelta", "outputRequestsDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputRequestsDeltaAvg":UcsPropertyMeta("OutputRequestsDeltaAvg", "outputRequestsDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputRequestsDeltaMax":UcsPropertyMeta("OutputRequestsDeltaMax", "outputRequestsDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"OutputRequestsDeltaMin":UcsPropertyMeta("OutputRequestsDeltaMin", "outputRequestsDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorFcIfFC4StatsHist", "adaptorFcIfFC4StatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

