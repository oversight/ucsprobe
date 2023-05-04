import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfQPILinkFrequencySelect(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfQPILinkFrequencySelect")

	@staticmethod
	def ClassId():
		return "biosVfQPILinkFrequencySelect"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_QPILINK_FREQUENCY_SELECT = "VpQPILinkFrequencySelect"

	CONST_VP_QPILINK_FREQUENCY_SELECT_64 = "64"
	CONST_VP_QPILINK_FREQUENCY_SELECT_72 = "72"
	CONST_VP_QPILINK_FREQUENCY_SELECT_80 = "80"
	CONST_VP_QPILINK_FREQUENCY_SELECT_AUTO = "auto"
	CONST_VP_QPILINK_FREQUENCY_SELECT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_QPILINK_FREQUENCY_SELECT_PLATFORM_RECOMMENDED = "platform-recommended"
