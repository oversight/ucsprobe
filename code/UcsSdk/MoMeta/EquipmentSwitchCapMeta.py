import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"FanModulesSupported":UcsPropertyMeta("FanModulesSupported", "fanModulesSupported", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"LocatorBeaconSupported":UcsPropertyMeta("LocatorBeaconSupported", "locatorBeaconSupported", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"MaxActiveSpanSessionCount":UcsPropertyMeta("MaxActiveSpanSessionCount", "maxActiveSpanSessionCount", "uint", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxEth1gPort":UcsPropertyMeta("MaxEth1gPort", "maxEth1gPort", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxEth1gSlot":UcsPropertyMeta("MaxEth1gSlot", "maxEth1gSlot", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxEthPcMembers":UcsPropertyMeta("MaxEthPcMembers", "maxEthPcMembers", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxEthPcs":UcsPropertyMeta("MaxEthPcs", "maxEthPcs", "uint", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxFcoePcMembers":UcsPropertyMeta("MaxFcoePcMembers", "maxFcoePcMembers", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxUplinkPorts":UcsPropertyMeta("MaxUplinkPorts", "maxUplinkPorts", "uint", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MgmtDaughterCardSlotId":UcsPropertyMeta("MgmtDaughterCardSlotId", "mgmtDaughterCardSlotId", "uint", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"SerenoNetflowSupported":UcsPropertyMeta("SerenoNetflowSupported", "serenoNetflowSupported", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentSwitchCap", "equipmentSwitchCap", "switch-cap", _VersionMeta.Version111j, "InputOutput", 0x7fL, [], [], ["Get"], [""])
}

