import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfOptionROMLoad(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfOptionROMLoad")

	@staticmethod
	def ClassId():
		return "biosVfOptionROMLoad"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_LOAD = "VpLoad"

	CONST_VP_LOAD_DISABLED = "disabled"
	CONST_VP_LOAD_ENABLED = "enabled"
	CONST_VP_LOAD_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LOAD_PLATFORM_RECOMMENDED = "platform-recommended"
