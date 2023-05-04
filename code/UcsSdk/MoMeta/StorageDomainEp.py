import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageDomainEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageDomainEp")

	@staticmethod
	def ClassId():
		return "storageDomainEp"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

