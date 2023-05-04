import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwVlanPortNsOverride(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwVlanPortNsOverride")

	@staticmethod
	def ClassId():
		return "swVlanPortNsOverride"

	DN = "Dn"
	LIMIT = "Limit"
	RN = "Rn"
	STATUS = "Status"

