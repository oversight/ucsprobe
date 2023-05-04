import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Addr":UcsPropertyMeta("Addr", "addr", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DefGw":UcsPropertyMeta("DefGw", "defGw", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"OperName":UcsPropertyMeta("OperName", "operName", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PrimDns":UcsPropertyMeta("PrimDns", "primDns", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"SecDns":UcsPropertyMeta("SecDns", "secDns", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Subnet":UcsPropertyMeta("Subnet", "subnet", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicIpV4MgmtPooledAddr", "vnicIpV4MgmtPooledAddr", "ipv4-pooled-addr", _VersionMeta.Version221b, "InputOutput", 0x1fL, [], [u'faultInst', u'vnicIpV4History'], ["Get", "Remove", "Set"], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"])
}

