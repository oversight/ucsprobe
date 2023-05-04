import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DomainNetworkFeature(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DomainNetworkFeature")

	@staticmethod
	def ClassId():
		return "domainNetworkFeature"

	DN = "Dn"
	FUNCTIONAL_STATE = "FunctionalState"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_FUNCTIONAL_STATE_DISABLED = "disabled"
	CONST_FUNCTIONAL_STATE_ENABLED = "enabled"
	CONST_TYPE_MAJOR = "major"
	CONST_TYPE_MINOR = "minor"
