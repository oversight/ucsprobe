import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareBundleInfo(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareBundleInfo")

	@staticmethod
	def ClassId():
		return "firmwareBundleInfo"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VERSION = "Version"

	CONST_TYPE_B_SERIES_BUNDLE = "b-series-bundle"
	CONST_TYPE_C_SERIES_BUNDLE = "c-series-bundle"
	CONST_TYPE_CATALOG = "catalog"
	CONST_TYPE_FULL_BUNDLE = "full-bundle"
	CONST_TYPE_IMAGE = "image"
	CONST_TYPE_INFRASTRUCTURE_BUNDLE = "infrastructure-bundle"
	CONST_TYPE_UNKNOWN = "unknown"
