import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Direction":UcsPropertyMeta("Direction", "direction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x2L, None, None, None, ["receive", "transmit"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Index":UcsPropertyMeta("Index", "index", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-2"]),
	"NfMonitorName":UcsPropertyMeta("NfMonitorName", "nfMonitorName", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"OperNfMonitorName":UcsPropertyMeta("OperNfMonitorName", "operNfMonitorName", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricNetflowMonitorRef", "fabricNetflowMonitorRef", "flow-monitor-[NfMonitorName]-dir-[Direction]", _VersionMeta.Version221b, "InputOutput", 0x7fL, [], [u'faultInst'], [None], ["admin", "ext-lan-config", "ext-lan-policy"])
}

