import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Capability":UcsPropertyMeta("Capability", "capability", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr),){0,27}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr){0,1}""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConnProtocol":UcsPropertyMeta("ConnProtocol", "connProtocol", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ipv4", "ipv6", "unknown"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Host":UcsPropertyMeta("Host", "host", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """^[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?$|^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*(\.[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$""", [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["0-4294967295"]),
	"Interest":UcsPropertyMeta("Interest", "interest", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr),){0,27}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr){0,1}""", [], ["0-4294967295"]),
	"Ip":UcsPropertyMeta("Ip", "ip", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Ipv6":UcsPropertyMeta("Ipv6", "ipv6", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"LastPollTs":UcsPropertyMeta("LastPollTs", "lastPollTs", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lost-visibility", "registered", "registering", "registry-not-reachable", "synchronizing", "unregistered", "version-mismatch"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ape", "boot-mgr", "identifier-mgr", "managed-endpoint", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-aggr", "resource-mgr", "service-reg", "stats-mgr", "storage-broker", "virtual-switching-mgr", "vm-mgr"], ["0-4294967295"]),
	"Version":UcsPropertyMeta("Version", "version", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ExtpolController", "extpolController", "contro-[Id]", _VersionMeta.Version211a, "InputOutput", 0x1fL, [], [u'observeObserved', u'policyPolicyScopeCont'], ["Get"], ["admin"])
}

