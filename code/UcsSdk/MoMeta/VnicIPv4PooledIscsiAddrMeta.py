import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Addr":UcsPropertyMeta("Addr", "addr", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DefGw":UcsPropertyMeta("DefGw", "defGw", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"IdentPoolName":UcsPropertyMeta("IdentPoolName", "identPoolName", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"OperIdentPoolName":UcsPropertyMeta("OperIdentPoolName", "operIdentPoolName", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PrimDns":UcsPropertyMeta("PrimDns", "primDns", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"SecDns":UcsPropertyMeta("SecDns", "secDns", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Subnet":UcsPropertyMeta("Subnet", "subnet", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicIPv4PooledIscsiAddr", "vnicIPv4PooledIscsiAddr", "ipv4-pooled-iscsiaddr", _VersionMeta.Version201m, "InputOutput", 0x1fL, [], [u'faultInst', u'vnicIPv4Dns', u'vnicIpV4History'], ["Get", "Set"], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"])
}

