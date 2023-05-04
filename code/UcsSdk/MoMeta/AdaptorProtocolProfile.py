import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorProtocolProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorProtocolProfile")

	@staticmethod
	def ClassId():
		return "adaptorProtocolProfile"

	BOOT_TO_TARGET = "BootToTarget"
	CONNECTION_TIME_OUT = "ConnectionTimeOut"
	DHCP_TIME_OUT = "DhcpTimeOut"
	DN = "Dn"
	HBA_MODE = "HbaMode"
	LUN_BUSY_RETRY_COUNT = "LunBusyRetryCount"
	RN = "Rn"
	STATUS = "Status"
	TCP_TIME_STAMP = "TcpTimeStamp"

	CONST_BOOT_TO_TARGET_FALSE = "false"
	CONST_BOOT_TO_TARGET_NO = "no"
	CONST_BOOT_TO_TARGET_TRUE = "true"
	CONST_BOOT_TO_TARGET_YES = "yes"
	CONST_HBA_MODE_FALSE = "false"
	CONST_HBA_MODE_NO = "no"
	CONST_HBA_MODE_TRUE = "true"
	CONST_HBA_MODE_YES = "yes"
	CONST_TCP_TIME_STAMP_FALSE = "false"
	CONST_TCP_TIME_STAMP_NO = "no"
	CONST_TCP_TIME_STAMP_TRUE = "true"
	CONST_TCP_TIME_STAMP_YES = "yes"
