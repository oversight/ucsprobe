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
	"VpBaudRate":UcsPropertyMeta("VpBaudRate", "vpBaudRate", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["115200", "19200", "38400", "57600", "9600", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpConsoleRedirection":UcsPropertyMeta("VpConsoleRedirection", "vpConsoleRedirection", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["com-0", "disabled", "enabled", "platform-default", "platform-recommended", "serial-port-a", "serial-port-b"], ["0-4294967295"]),
	"VpFlowControl":UcsPropertyMeta("VpFlowControl", "vpFlowControl", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["none", "platform-default", "platform-recommended", "rts-cts"], ["0-4294967295"]),
	"VpLegacyOSRedirection":UcsPropertyMeta("VpLegacyOSRedirection", "vpLegacyOSRedirection", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPuttyKeyPad":UcsPropertyMeta("VpPuttyKeyPad", "vpPuttyKeyPad", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["escn", "linux", "platform-default", "platform-recommended", "sco", "vt100", "vt400", "xtermr6"], ["0-4294967295"]),
	"VpTerminalType":UcsPropertyMeta("VpTerminalType", "vpTerminalType", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["pc-ansi", "platform-default", "platform-recommended", "vt-utf8", "vt100", "vt100-plus"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosVfConsoleRedirection", "biosVfConsoleRedirection", "Console-redirection", _VersionMeta.Version111j, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"])
}

