import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VpIntelVTDATSSupport":UcsPropertyMeta("VpIntelVTDATSSupport", "vpIntelVTDATSSupport", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpIntelVTDCoherencySupport":UcsPropertyMeta("VpIntelVTDCoherencySupport", "vpIntelVTDCoherencySupport", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpIntelVTDInterruptRemapping":UcsPropertyMeta("VpIntelVTDInterruptRemapping", "vpIntelVTDInterruptRemapping", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpIntelVTDPassThroughDMASupport":UcsPropertyMeta("VpIntelVTDPassThroughDMASupport", "vpIntelVTDPassThroughDMASupport", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpIntelVTForDirectedIO":UcsPropertyMeta("VpIntelVTForDirectedIO", "vpIntelVTForDirectedIO", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosVfIntelVTForDirectedIO", "biosVfIntelVTForDirectedIO", "Intel-VT-for-directed-IO", _VersionMeta.Version111j, "InputOutput", 0x1ffL, [], [], ["Get", "Set"], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"])
}

