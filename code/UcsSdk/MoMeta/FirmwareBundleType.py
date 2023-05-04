import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareBundleType(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareBundleType")

	@staticmethod
	def ClassId():
		return "firmwareBundleType"

	DN = "Dn"
	INV_TAG = "InvTag"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_B_SERIES_BUNDLE = "b-series-bundle"
	CONST_TYPE_C_SERIES_BUNDLE = "c-series-bundle"
	CONST_TYPE_CATALOG = "catalog"
	CONST_TYPE_FULL_BUNDLE = "full-bundle"
	CONST_TYPE_IMAGE = "image"
	CONST_TYPE_INFRASTRUCTURE_BUNDLE = "infrastructure-bundle"
	CONST_TYPE_UNKNOWN = "unknown"
