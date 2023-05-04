import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfSerialPortAEnable(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfSerialPortAEnable")

	@staticmethod
	def ClassId():
		return "biosVfSerialPortAEnable"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_SERIAL_PORT_AENABLE = "VpSerialPortAEnable"

	CONST_VP_SERIAL_PORT_AENABLE_DISABLED = "disabled"
	CONST_VP_SERIAL_PORT_AENABLE_ENABLED = "enabled"
	CONST_VP_SERIAL_PORT_AENABLE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_SERIAL_PORT_AENABLE_PLATFORM_RECOMMENDED = "platform-recommended"
