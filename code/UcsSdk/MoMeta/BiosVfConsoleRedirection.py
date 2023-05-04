import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfConsoleRedirection(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfConsoleRedirection")

	@staticmethod
	def ClassId():
		return "biosVfConsoleRedirection"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_BAUD_RATE = "VpBaudRate"
	VP_CONSOLE_REDIRECTION = "VpConsoleRedirection"
	VP_FLOW_CONTROL = "VpFlowControl"
	VP_LEGACY_OSREDIRECTION = "VpLegacyOSRedirection"
	VP_PUTTY_KEY_PAD = "VpPuttyKeyPad"
	VP_TERMINAL_TYPE = "VpTerminalType"

	CONST_VP_BAUD_RATE_115200 = "115200"
	CONST_VP_BAUD_RATE_19200 = "19200"
	CONST_VP_BAUD_RATE_38400 = "38400"
	CONST_VP_BAUD_RATE_57600 = "57600"
	CONST_VP_BAUD_RATE_9600 = "9600"
	CONST_VP_BAUD_RATE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_BAUD_RATE_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_CONSOLE_REDIRECTION_COM_0 = "com-0"
	CONST_VP_CONSOLE_REDIRECTION_DISABLED = "disabled"
	CONST_VP_CONSOLE_REDIRECTION_ENABLED = "enabled"
	CONST_VP_CONSOLE_REDIRECTION_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_CONSOLE_REDIRECTION_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_CONSOLE_REDIRECTION_SERIAL_PORT_A = "serial-port-a"
	CONST_VP_CONSOLE_REDIRECTION_SERIAL_PORT_B = "serial-port-b"
	CONST_VP_FLOW_CONTROL_NONE = "none"
	CONST_VP_FLOW_CONTROL_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_FLOW_CONTROL_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_FLOW_CONTROL_RTS_CTS = "rts-cts"
	CONST_VP_LEGACY_OSREDIRECTION_DISABLED = "disabled"
	CONST_VP_LEGACY_OSREDIRECTION_ENABLED = "enabled"
	CONST_VP_LEGACY_OSREDIRECTION_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LEGACY_OSREDIRECTION_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_PUTTY_KEY_PAD_ESCN = "escn"
	CONST_VP_PUTTY_KEY_PAD_LINUX = "linux"
	CONST_VP_PUTTY_KEY_PAD_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PUTTY_KEY_PAD_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_PUTTY_KEY_PAD_SCO = "sco"
	CONST_VP_PUTTY_KEY_PAD_VT100 = "vt100"
	CONST_VP_PUTTY_KEY_PAD_VT400 = "vt400"
	CONST_VP_PUTTY_KEY_PAD_XTERMR6 = "xtermr6"
	CONST_VP_TERMINAL_TYPE_PC_ANSI = "pc-ansi"
	CONST_VP_TERMINAL_TYPE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_TERMINAL_TYPE_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_TERMINAL_TYPE_VT_UTF8 = "vt-utf8"
	CONST_VP_TERMINAL_TYPE_VT100 = "vt100"
	CONST_VP_TERMINAL_TYPE_VT100_PLUS = "vt100-plus"
