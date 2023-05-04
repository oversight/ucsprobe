import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwFabricZoneNsOverride(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwFabricZoneNsOverride")

	@staticmethod
	def ClassId():
		return "swFabricZoneNsOverride"

	DN = "Dn"
	LIMIT = "Limit"
	RN = "Rn"
	STATUS = "Status"

