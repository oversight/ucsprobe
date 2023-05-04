import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConPolicyName":UcsPropertyMeta("ConPolicyName", "conPolicyName", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x2L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"UsnicCount":UcsPropertyMeta("UsnicCount", "usnicCount", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorUsnicConnDef", "adaptorUsnicConnDef", "usnic-conn-def-[ConPolicyName]", _VersionMeta.Version221b, "InputOutput", 0x1fL, [], [u'adaptorEthCompQueueProfile', u'adaptorEthFailoverProfile', u'adaptorEthInterruptProfile', u'adaptorEthOffloadProfile', u'adaptorEthRecvQueueProfile', u'adaptorEthWorkQueueProfile', u'adaptorExtIpV6RssHashProfile', u'adaptorIpV4RssHashProfile', u'adaptorIpV6RssHashProfile', u'adaptorRssProfile'], [None], ["admin", "ls-compute", "ls-config", "ls-server"])
}

