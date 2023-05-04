import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowMonSession(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowMonSession")

	@staticmethod
	def ClassId():
		return "fabricNetflowMonSession"

	ADMIN_STATE = "AdminState"
	CONFIG_FAIL_REASON = "ConfigFailReason"
	CONFIG_QUALIFIER = "ConfigQualifier"
	DESCR = "Descr"
	DN = "Dn"
	ID = "Id"
	IS_CONFIG_SUCCESS = "IsConfigSuccess"
	LOCALE = "Locale"
	NAME = "Name"
	PROTOCOL = "Protocol"
	RN = "Rn"
	SESSION = "Session"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
	CONST_IS_CONFIG_SUCCESS_FALSE = "false"
	CONST_IS_CONFIG_SUCCESS_NO = "no"
	CONST_IS_CONFIG_SUCCESS_TRUE = "true"
	CONST_IS_CONFIG_SUCCESS_YES = "yes"
	CONST_PROTOCOL_NETFLOW = "netflow"
