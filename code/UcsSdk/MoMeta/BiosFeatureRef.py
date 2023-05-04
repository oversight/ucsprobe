import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosFeatureRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosFeatureRef")

	@staticmethod
	def ClassId():
		return "biosFeatureRef"

	DN = "Dn"
	FTR_MO_CLASS_NAME = "FtrMoClassName"
	IS_SUPPORTED = "IsSupported"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_YES = "yes"
