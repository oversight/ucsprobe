import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricFcMonFiltEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricFcMonFiltEp")

	@staticmethod
	def ClassId():
		return "fabricFcMonFiltEp"

	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	SESSION = "Session"
	STATUS = "Status"
	TYPE = "Type"

