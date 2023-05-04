import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DomainServerFeatureCont(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DomainServerFeatureCont")

	@staticmethod
	def ClassId():
		return "domainServerFeatureCont"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

