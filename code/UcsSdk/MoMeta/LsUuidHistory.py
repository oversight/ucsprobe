import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsUuidHistory(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsUuidHistory")

	@staticmethod
	def ClassId():
		return "lsUuidHistory"

	DN = "Dn"
	OLDUUID = "Olduuid"
	RN = "Rn"
	STATUS = "Status"

