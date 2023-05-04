import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentHostIfCapProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentHostIfCapProvider")

	@staticmethod
	def ClassId():
		return "equipmentHostIfCapProvider"

	DELETED = "Deleted"
	DEPRECATED = "Deprecated"
	DN = "Dn"
	ELEMENT_LOAD_FAILURES = "ElementLoadFailures"
	ELEMENTS_LOADED = "ElementsLoaded"
	GENCOUNT = "Gencount"
	LOAD_ERRORS = "LoadErrors"
	LOAD_WARNINGS = "LoadWarnings"
	MGMT_PLANE_VER = "MgmtPlaneVer"
	MODEL = "Model"
	PROM_CARD_TYPE = "PromCardType"
	REVISION = "Revision"
	RN = "Rn"
	STATUS = "Status"
	VENDOR = "Vendor"

	CONST_DELETED_FALSE = "false"
	CONST_DELETED_NO = "no"
	CONST_DELETED_TRUE = "true"
	CONST_DELETED_YES = "yes"
	CONST_DEPRECATED_FALSE = "false"
	CONST_DEPRECATED_NO = "no"
	CONST_DEPRECATED_TRUE = "true"
	CONST_DEPRECATED_YES = "yes"
