import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcErrorRecoveryProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcErrorRecoveryProfile")

	@staticmethod
	def ClassId():
		return "adaptorFcErrorRecoveryProfile"

	DN = "Dn"
	ERROR_DETECT_TIMEOUT = "ErrorDetectTimeout"
	FCP_ERROR_RECOVERY = "FcpErrorRecovery"
	LINK_DOWN_TIMEOUT = "LinkDownTimeout"
	PORT_DOWN_IO_RETRY_COUNT = "PortDownIoRetryCount"
	PORT_DOWN_TIMEOUT = "PortDownTimeout"
	RESOURCE_ALLOCATION_TIMEOUT = "ResourceAllocationTimeout"
	RN = "Rn"
	STATUS = "Status"

	CONST_FCP_ERROR_RECOVERY_DISABLED = "disabled"
	CONST_FCP_ERROR_RECOVERY_ENABLED = "enabled"
