import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VpPort6064Emulation":UcsPropertyMeta("VpPort6064Emulation", "vpPort6064Emulation", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpUSBPortFront":UcsPropertyMeta("VpUSBPortFront", "vpUSBPortFront", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpUSBPortInternal":UcsPropertyMeta("VpUSBPortInternal", "vpUSBPortInternal", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpUSBPortKVM":UcsPropertyMeta("VpUSBPortKVM", "vpUSBPortKVM", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpUSBPortRear":UcsPropertyMeta("VpUSBPortRear", "vpUSBPortRear", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpUSBPortSDCard":UcsPropertyMeta("VpUSBPortSDCard", "vpUSBPortSDCard", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpUSBPortVMedia":UcsPropertyMeta("VpUSBPortVMedia", "vpUSBPortVMedia", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosVfUSBPortConfiguration", "biosVfUSBPortConfiguration", "USB-port-configuration", _VersionMeta.Version222c, "InputOutput", 0x7ffL, [], [], [None], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"])
}

