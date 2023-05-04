import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CimcvmediaExtMgmtRuleEntry(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CimcvmediaExtMgmtRuleEntry")

	@staticmethod
	def ClassId():
		return "cimcvmediaExtMgmtRuleEntry"

	DN = "Dn"
	EXT_MGMT_IP_ADDR = "ExtMgmtIpAddr"
	MAPPING_NAME = "MappingName"
	MGMT_IF_IP_ADDR = "MgmtIfIpAddr"
	MOUNT_PROTOCOL = "MountProtocol"
	REMOTE_IP_ADDR = "RemoteIpAddr"
	REMOTE_PORT = "RemotePort"
	RN = "Rn"
	STATUS = "Status"

	CONST_MOUNT_PROTOCOL_CIFS = "cifs"
	CONST_MOUNT_PROTOCOL_HTTP = "http"
	CONST_MOUNT_PROTOCOL_HTTPS = "https"
	CONST_MOUNT_PROTOCOL_NFS = "nfs"
	CONST_MOUNT_PROTOCOL_UNKNOWN = "unknown"
