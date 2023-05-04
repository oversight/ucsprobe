import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricFcMonFiltRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricFcMonFiltRef")

	@staticmethod
	def ClassId():
		return "fabricFcMonFiltRef"

	DN = "Dn"
	RN = "Rn"
	SRC_FILT_DN = "SrcFiltDn"
	STATUS = "Status"
	TYPE = "Type"

