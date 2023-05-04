import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminInbandIfState":UcsPropertyMeta("AdminInbandIfState", "adminInbandIfState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disable", "enable"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"InbandIfGw":UcsPropertyMeta("InbandIfGw", "inbandIfGw", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"InbandIfIp":UcsPropertyMeta("InbandIfIp", "inbandIfIp", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"InbandIfMask":UcsPropertyMeta("InbandIfMask", "inbandIfMask", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"InbandIfVnet":UcsPropertyMeta("InbandIfVnet", "inbandIfVnet", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4090"]),
	"InventoryStatus":UcsPropertyMeta("InventoryStatus", "inventoryStatus", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|up|remote-eth-port-inventory|fc-pc-inventory|fc-port-inventory|switch-fru|vlan-comp-grp-inventory|switch-inventory|vlan-port-count|mgmt-port-inventory|card-inventory|xcvr-inventory|eth-pc-inventory|eth-port-inventory),){0,13}(defaultValue|up|remote-eth-port-inventory|fc-pc-inventory|fc-port-inventory|switch-fru|vlan-comp-grp-inventory|switch-inventory|vlan-port-count|mgmt-port-inventory|card-inventory|xcvr-inventory|eth-pc-inventory|eth-port-inventory){0,1}""", [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"OobIfGw":UcsPropertyMeta("OobIfGw", "oobIfGw", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"OobIfIp":UcsPropertyMeta("OobIfIp", "oobIfIp", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"OobIfMask":UcsPropertyMeta("OobIfMask", "oobIfMask", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Operability":UcsPropertyMeta("Operability", "operability", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["inoperable", "operable", "unknown"], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Thermal":UcsPropertyMeta("Thermal", "thermal", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
	"TotalMemory":UcsPropertyMeta("TotalMemory", "totalMemory", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("NetworkElement", "networkElement", "switch-[Id]", _VersionMeta.Version101e, "InputOutput", 0xffL, [], [u'equipmentFan', u'equipmentFanModule', u'equipmentLocatorLed', u'equipmentPsu', u'equipmentSwitchCard', u'extmgmtIf', u'faultInst', u'firmwareStatus', u'mgmtController', u'mgmtIPv6IfConfig', u'networkOperLevel', u'nfsMountInst', u'storageItem', u'swAccessDomain', u'swCardEnvStats', u'swEnvStats', u'swEthLanBorder', u'swEthLanFlowMon', u'swEthLanMon', u'swFabricZoneNs', u'swFcSanBorder', u'swFcSanMon', u'swPhys', u'swSystemStats', u'swUtilityDomain', u'swVlanPortNs'], ["Get"], ["admin", "ext-lan-config"])
}

