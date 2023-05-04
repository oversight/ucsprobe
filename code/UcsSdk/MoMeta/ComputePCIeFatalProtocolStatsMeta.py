import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DllpErrors":UcsPropertyMeta("DllpErrors", "dllpErrors", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors15Min":UcsPropertyMeta("DllpErrors15Min", "dllpErrors15Min", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors15MinH":UcsPropertyMeta("DllpErrors15MinH", "dllpErrors15MinH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors1Day":UcsPropertyMeta("DllpErrors1Day", "dllpErrors1Day", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors1DayH":UcsPropertyMeta("DllpErrors1DayH", "dllpErrors1DayH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors1Hour":UcsPropertyMeta("DllpErrors1Hour", "dllpErrors1Hour", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors1HourH":UcsPropertyMeta("DllpErrors1HourH", "dllpErrors1HourH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors1Week":UcsPropertyMeta("DllpErrors1Week", "dllpErrors1Week", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors1WeekH":UcsPropertyMeta("DllpErrors1WeekH", "dllpErrors1WeekH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors2Weeks":UcsPropertyMeta("DllpErrors2Weeks", "dllpErrors2Weeks", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DllpErrors2WeeksH":UcsPropertyMeta("DllpErrors2WeeksH", "dllpErrors2WeeksH", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"FlowControlErrors":UcsPropertyMeta("FlowControlErrors", "flowControlErrors", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors15Min":UcsPropertyMeta("FlowControlErrors15Min", "flowControlErrors15Min", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors15MinH":UcsPropertyMeta("FlowControlErrors15MinH", "flowControlErrors15MinH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors1Day":UcsPropertyMeta("FlowControlErrors1Day", "flowControlErrors1Day", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors1DayH":UcsPropertyMeta("FlowControlErrors1DayH", "flowControlErrors1DayH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors1Hour":UcsPropertyMeta("FlowControlErrors1Hour", "flowControlErrors1Hour", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors1HourH":UcsPropertyMeta("FlowControlErrors1HourH", "flowControlErrors1HourH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors1Week":UcsPropertyMeta("FlowControlErrors1Week", "flowControlErrors1Week", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors1WeekH":UcsPropertyMeta("FlowControlErrors1WeekH", "flowControlErrors1WeekH", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors2Weeks":UcsPropertyMeta("FlowControlErrors2Weeks", "flowControlErrors2Weeks", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FlowControlErrors2WeeksH":UcsPropertyMeta("FlowControlErrors2WeeksH", "flowControlErrors2WeeksH", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ComputePCIeFatalProtocolStats", "computePCIeFatalProtocolStats", "pciefat-protocol-stats", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "operations", "read-only"])
}

