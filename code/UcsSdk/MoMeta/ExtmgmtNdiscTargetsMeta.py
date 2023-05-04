import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applied", "ok"], ["0-4294967295"]),
	"ConfigStatusMessage":UcsPropertyMeta("ConfigStatusMessage", "configStatusMessage", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Ipv6Target1":UcsPropertyMeta("Ipv6Target1", "ipv6Target1", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Ipv6Target2":UcsPropertyMeta("Ipv6Target2", "ipv6Target2", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Ipv6Target3":UcsPropertyMeta("Ipv6Target3", "ipv6Target3", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"MaxDeadlineTimeout":UcsPropertyMeta("MaxDeadlineTimeout", "maxDeadlineTimeout", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["5-15"]),
	"NumberOfNdiscRequests":UcsPropertyMeta("NumberOfNdiscRequests", "numberOfNdiscRequests", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["1-5"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ExtmgmtNdiscTargets", "extmgmtNdiscTargets", "ndisc-target-policy", _VersionMeta.Version221b, "InputOutput", 0x1ffL, [], [u'faultInst'], ["Get", "Set"], ["admin", "ext-lan-config"])
}

