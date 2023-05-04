import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsVersionBeh(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsVersionBeh")

	@staticmethod
	def ClassId():
		return "lsVersionBeh"

	DN = "Dn"
	PCI_ENUM = "PciEnum"
	RN = "Rn"
	STATUS = "Status"
	VCON_MAP = "VconMap"
	VNIC_MAP = "VnicMap"
	VNIC_ORDER = "VnicOrder"

	CONST_PCI_ENUM_MULTI_FUNC_ALL = "multi-func-all"
	CONST_PCI_ENUM_STATIC_ZERO_FUNC = "static-zero-func"
	CONST_PCI_ENUM_ZERO_FUNC_ALL = "zero-func-all"
	CONST_VCON_MAP_LINEAR_ORDERED = "linear-ordered"
	CONST_VCON_MAP_LINEAR_ORDERED_TO_ROUND_ROBIN = "linear-ordered-to-round-robin"
	CONST_VCON_MAP_ROUND_ROBIN = "round-robin"
	CONST_VCON_MAP_ROUND_ROBIN_TO_LINEAR_ORDERED = "round-robin-to-linear-ordered"
	CONST_VNIC_MAP_CAP_LOAD_DISTRIBUTE = "cap-load-distribute"
	CONST_VNIC_MAP_PHYSICAL_CAP_FIRST = "physical-cap-first"
	CONST_VNIC_ORDER_ALL_VNIC = "all-vnic"
	CONST_VNIC_ORDER_DYNAMIC_ALL_LAST = "dynamic-all-last"
	CONST_VNIC_ORDER_STATIC_ALL_FIRST = "static-all-first"
