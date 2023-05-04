import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthMonFiltRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthMonFiltRef")

	@staticmethod
	def ClassId():
		return "fabricEthMonFiltRef"

	DN = "Dn"
	RN = "Rn"
	SRC_FILT_DN = "SrcFiltDn"
	STATUS = "Status"
	TYPE = "Type"

