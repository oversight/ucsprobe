import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtProfDerivedInterface(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtProfDerivedInterface")

	@staticmethod
	def ClassId():
		return "mgmtProfDerivedInterface"

	CONFIG_MESSAGE = "ConfigMessage"
	CONFIG_STATE = "ConfigState"
	DN = "Dn"
	IP_V4_STATE = "IpV4State"
	IP_V6_STATE = "IpV6State"
	MODE = "Mode"
	OPER_STATE = "OperState"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIG_STATE_INCOMPLETE = "incomplete"
	CONST_CONFIG_STATE_UNRESOLVED_VLAN = "unresolvedVlan"
	CONST_CONFIG_STATE_UNSUPPORTED_FIRMWARE = "unsupportedFirmware"
	CONST_CONFIG_STATE_UNSUPPORTED_SERVER = "unsupportedServer"
	CONST_CONFIG_STATE_UNSUPPORTED_VLAN = "unsupportedVlan"
	CONST_CONFIG_STATE_VALID = "valid"
	CONST_IP_V4_STATE_NONE = "none"
	CONST_IP_V4_STATE_POOLED = "pooled"
	CONST_IP_V4_STATE_STATIC = "static"
	CONST_IP_V6_STATE_NONE = "none"
	CONST_IP_V6_STATE_POOLED = "pooled"
	CONST_IP_V6_STATE_STATIC = "static"
	CONST_MODE_IN_BAND = "in-band"
	CONST_OPER_STATE_DEPLOYED = "deployed"
	CONST_OPER_STATE_DOWN = "down"
	CONST_OPER_STATE_NOT_DEPLOYED = "notDeployed"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_OPER_STATE_UP = "up"
