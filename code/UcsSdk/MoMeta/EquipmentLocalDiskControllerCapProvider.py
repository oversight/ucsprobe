import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentLocalDiskControllerCapProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentLocalDiskControllerCapProvider")

	@staticmethod
	def ClassId():
		return "equipmentLocalDiskControllerCapProvider"

	CARD_TYPE = "CardType"
	DELETED = "Deleted"
	DEPRECATED = "Deprecated"
	DN = "Dn"
	ELEMENT_LOAD_FAILURES = "ElementLoadFailures"
	ELEMENTS_LOADED = "ElementsLoaded"
	FORM = "Form"
	GENCOUNT = "Gencount"
	INTERNALPORTS = "Internalports"
	LOAD_ERRORS = "LoadErrors"
	LOAD_WARNINGS = "LoadWarnings"
	MGMT_PLANE_VER = "MgmtPlaneVer"
	MODEL = "Model"
	PROM_CARD_TYPE = "PromCardType"
	REVISION = "Revision"
	RN = "Rn"
	STATUS = "Status"
	VENDOR = "Vendor"

	CONST_CARD_TYPE_FLASH = "FLASH"
	CONST_CARD_TYPE_SAS = "SAS"
	CONST_DELETED_FALSE = "false"
	CONST_DELETED_NO = "no"
	CONST_DELETED_TRUE = "true"
	CONST_DELETED_YES = "yes"
	CONST_DEPRECATED_FALSE = "false"
	CONST_DEPRECATED_NO = "no"
	CONST_DEPRECATED_TRUE = "true"
	CONST_DEPRECATED_YES = "yes"
	CONST_FORM_EMBEDDED = "embedded"
	CONST_FORM_MEZZANINE = "mezzanine"
	CONST_FORM_NONE = "none"
	CONST_FORM_ON_BOARD = "on-board"
	CONST_FORM_PCI = "pci"
