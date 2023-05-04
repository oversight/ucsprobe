import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricSanMonCloud(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricSanMonCloud")

	@staticmethod
	def ClassId():
		return "fabricSanMonCloud"

	DN = "Dn"
	MODE = "Mode"
	RN = "Rn"
	STATUS = "Status"

	CONST_MODE_END_HOST = "end-host"
	CONST_MODE_SWITCH = "switch"
