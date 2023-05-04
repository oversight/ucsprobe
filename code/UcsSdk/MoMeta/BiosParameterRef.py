import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosParameterRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosParameterRef")

	@staticmethod
	def ClassId():
		return "biosParameterRef"

	DN = "Dn"
	IS_SUPPORTED = "IsSupported"
	NAME = "Name"
	PROPERTY_NAME = "PropertyName"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_YES = "yes"
