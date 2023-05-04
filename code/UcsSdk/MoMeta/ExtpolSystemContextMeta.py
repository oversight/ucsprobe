import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Capability":UcsPropertyMeta("Capability", "capability", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr),){0,27}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr){0,1}""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Guid":UcsPropertyMeta("Guid", "guid", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Interest":UcsPropertyMeta("Interest", "interest", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr),){0,27}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|vm-slb|storage-broker|resource-mgr){0,1}""", [], ["0-4294967295"]),
	"Ip":UcsPropertyMeta("Ip", "ip", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Ipv6addr":UcsPropertyMeta("Ipv6addr", "ipv6addr", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Owner":UcsPropertyMeta("Owner", "owner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Site":UcsPropertyMeta("Site", "site", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ape", "boot-mgr", "identifier-mgr", "managed-endpoint", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-aggr", "resource-mgr", "service-reg", "stats-mgr", "storage-broker", "virtual-switching-mgr", "vm-mgr"], ["0-4294967295"]),
	"Version":UcsPropertyMeta("Version", "version", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ExtpolSystemContext", "extpolSystemContext", "sysctx", _VersionMeta.Version211a, "InputOutput", 0xfL, [], [], [None], ["read-only"])
}
