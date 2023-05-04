import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CallhomeSource(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CallhomeSource")

	@staticmethod
	def ClassId():
		return "callhomeSource"

	ADDR = "Addr"
	CONTACT = "Contact"
	CONTRACT = "Contract"
	CUSTOMER = "Customer"
	DN = "Dn"
	EMAIL = "Email"
	FROM = "From"
	PHONE = "Phone"
	REPLY_TO = "ReplyTo"
	RN = "Rn"
	SITE = "Site"
	STATUS = "Status"
	URGENCY = "Urgency"

	CONST_URGENCY_ALERT = "alert"
	CONST_URGENCY_CRITICAL = "critical"
	CONST_URGENCY_DEBUG = "debug"
	CONST_URGENCY_EMERGENCY = "emergency"
	CONST_URGENCY_ERROR = "error"
	CONST_URGENCY_INFO = "info"
	CONST_URGENCY_NOTICE = "notice"
	CONST_URGENCY_WARNING = "warning"
