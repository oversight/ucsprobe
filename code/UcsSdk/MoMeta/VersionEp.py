import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VersionEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VersionEp")

	@staticmethod
	def ClassId():
		return "versionEp"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

