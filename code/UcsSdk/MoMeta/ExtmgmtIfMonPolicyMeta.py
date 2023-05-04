import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"EnableHAFailover":UcsPropertyMeta("EnableHAFailover", "enableHAFailover", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"MaxFailReportCount":UcsPropertyMeta("MaxFailReportCount", "maxFailReportCount", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["2-5"]),
	"MonitorMechanism":UcsPropertyMeta("MonitorMechanism", "monitorMechanism", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["arpTargetPing", "gatewayPing", "miiStatus"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"PollInterval":UcsPropertyMeta("PollInterval", "pollInterval", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["90-300"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ExtmgmtIfMonPolicy", "extmgmtIfMonPolicy", "extmgmt-intf-monitor-policy", _VersionMeta.Version141i, "InputOutput", 0xfffL, [], [u'extmgmtArpTargets', u'extmgmtGatewayPing', u'extmgmtMiiStatus', u'extmgmtNdiscTargets'], ["Get", "Set"], ["admin", "ext-lan-config"])
}

