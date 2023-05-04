import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseFeatureCapProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseFeatureCapProvider")

	@staticmethod
	def ClassId():
		return "licenseFeatureCapProvider"

	DEF_QUANT = "DefQuant"
	DELETED = "Deleted"
	DEPRECATED = "Deprecated"
	DN = "Dn"
	ELEMENT_LOAD_FAILURES = "ElementLoadFailures"
	ELEMENTS_LOADED = "ElementsLoaded"
	FEATURE_NAME = "FeatureName"
	GENCOUNT = "Gencount"
	GRACE_PERIOD = "GracePeriod"
	LIC_VENDOR = "LicVendor"
	LIC_VERSION = "LicVersion"
	LOAD_ERRORS = "LoadErrors"
	LOAD_WARNINGS = "LoadWarnings"
	MGMT_PLANE_VER = "MgmtPlaneVer"
	MODEL = "Model"
	REVISION = "Revision"
	RN = "Rn"
	SKU = "Sku"
	STATUS = "Status"
	TYPE = "Type"
	VENDOR = "Vendor"

	CONST_DELETED_FALSE = "false"
	CONST_DELETED_NO = "no"
	CONST_DELETED_TRUE = "true"
	CONST_DELETED_YES = "yes"
	CONST_DEPRECATED_FALSE = "false"
	CONST_DEPRECATED_NO = "no"
	CONST_DEPRECATED_TRUE = "true"
	CONST_DEPRECATED_YES = "yes"
	CONST_TYPE_BOOLEAN = "boolean"
	CONST_TYPE_COUNTED = "counted"
