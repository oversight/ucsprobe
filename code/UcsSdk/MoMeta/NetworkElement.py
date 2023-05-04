import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class NetworkElement(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"NetworkElement")

	@staticmethod
	def ClassId():
		return "networkElement"

	ADMIN_INBAND_IF_STATE = "AdminInbandIfState"
	DN = "Dn"
	ID = "Id"
	INBAND_IF_GW = "InbandIfGw"
	INBAND_IF_IP = "InbandIfIp"
	INBAND_IF_MASK = "InbandIfMask"
	INBAND_IF_VNET = "InbandIfVnet"
	INVENTORY_STATUS = "InventoryStatus"
	MODEL = "Model"
	OOB_IF_GW = "OobIfGw"
	OOB_IF_IP = "OobIfIp"
	OOB_IF_MASK = "OobIfMask"
	OPERABILITY = "Operability"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	THERMAL = "Thermal"
	TOTAL_MEMORY = "TotalMemory"
	VENDOR = "Vendor"

	CONST_ADMIN_INBAND_IF_STATE_DISABLE = "disable"
	CONST_ADMIN_INBAND_IF_STATE_ENABLE = "enable"
	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
	CONST_OPERABILITY_INOPERABLE = "inoperable"
	CONST_OPERABILITY_OPERABLE = "operable"
	CONST_OPERABILITY_UNKNOWN = "unknown"
	CONST_THERMAL_LOWER_CRITICAL = "lower-critical"
	CONST_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_THERMAL_NOT_SUPPORTED = "not-supported"
	CONST_THERMAL_OK = "ok"
	CONST_THERMAL_UNKNOWN = "unknown"
	CONST_THERMAL_UPPER_CRITICAL = "upper-critical"
	CONST_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
