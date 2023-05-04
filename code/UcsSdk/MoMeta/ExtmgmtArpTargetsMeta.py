import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applied", "ok"], ["0-4294967295"]),
	"ConfigStatusMessage":UcsPropertyMeta("ConfigStatusMessage", "configStatusMessage", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"MaxDeadlineTimeout":UcsPropertyMeta("MaxDeadlineTimeout", "maxDeadlineTimeout", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["5-15"]),
	"NumberOfArpRequests":UcsPropertyMeta("NumberOfArpRequests", "numberOfArpRequests", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["1-5"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TargetIp1":UcsPropertyMeta("TargetIp1", "targetIp1", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x40L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"TargetIp2":UcsPropertyMeta("TargetIp2", "targetIp2", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"TargetIp3":UcsPropertyMeta("TargetIp3", "targetIp3", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x100L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ExtmgmtArpTargets", "extmgmtArpTargets", "arp-target-policy", _VersionMeta.Version141i, "InputOutput", 0x1ffL, [], [u'faultInst'], ["Get"], ["admin", "ext-lan-config"])
}

