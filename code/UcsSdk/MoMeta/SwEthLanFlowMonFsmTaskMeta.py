import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Completion":UcsPropertyMeta("Completion", "completion", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cancelled", "completed", "processing", "scheduled"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Flags":UcsPropertyMeta("Flags", "flags", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """(defaultValue){0,1}""", [], ["0-4294967295"]),
	"Item":UcsPropertyMeta("Item", "item", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, None, None, None, None, ["Deploy", "nop"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"SeqId":UcsPropertyMeta("SeqId", "seqId", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SwEthLanFlowMonFsmTask", "swEthLanFlowMonFsmTask", "task-[Item]", _VersionMeta.Version221b, "OutputOnly", 0x0L, [], [], [None], [""])
}

