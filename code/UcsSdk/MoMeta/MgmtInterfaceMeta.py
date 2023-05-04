import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigMessage":UcsPropertyMeta("ConfigMessage", "configMessage", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["incomplete", "unresolvedVlan", "unsupportedFirmware", "unsupportedServer", "unsupportedVlan", "valid"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"IpV4State":UcsPropertyMeta("IpV4State", "ipV4State", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["none", "pooled", "static"], ["0-4294967295"]),
	"IpV6State":UcsPropertyMeta("IpV6State", "ipV6State", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["none", "pooled", "static"], ["0-4294967295"]),
	"IsDefaultDerived":UcsPropertyMeta("IsDefaultDerived", "isDefaultDerived", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Mode":UcsPropertyMeta("Mode", "mode", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x10L, None, None, None, ["in-band"], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["deployed", "down", "notDeployed", "unknown", "up"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("MgmtInterface", "mgmtInterface", "iface-[Mode]", _VersionMeta.Version221b, "InputOutput", 0x7fL, [], [u'faultInst', u'mgmtVnet'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"])
}

