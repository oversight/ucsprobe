import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CimcvmediaConfigMountEntry(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CimcvmediaConfigMountEntry")

	@staticmethod
	def ClassId():
		return "cimcvmediaConfigMountEntry"

	DESCRIPTION = "Description"
	DEVICE_TYPE = "DeviceType"
	DN = "Dn"
	ENC_PWD = "EncPwd"
	IMAGE_FILE_NAME = "ImageFileName"
	IMAGE_PATH = "ImagePath"
	MAPPING_NAME = "MappingName"
	MOUNT_PROTOCOL = "MountProtocol"
	PASSWORD = "Password"
	PWD_SET = "PwdSet"
	REMOTE_HOST = "RemoteHost"
	REMOTE_IP_ADDRESS = "RemoteIpAddress"
	REMOTE_PORT = "RemotePort"
	RN = "Rn"
	STATUS = "Status"
	USER_ID = "UserId"

	CONST_DEVICE_TYPE_CDD = "cdd"
	CONST_DEVICE_TYPE_HDD = "hdd"
	CONST_DEVICE_TYPE_UNKNOWN = "unknown"
	CONST_MOUNT_PROTOCOL_CIFS = "cifs"
	CONST_MOUNT_PROTOCOL_HTTP = "http"
	CONST_MOUNT_PROTOCOL_HTTPS = "https"
	CONST_MOUNT_PROTOCOL_NFS = "nfs"
	CONST_MOUNT_PROTOCOL_UNKNOWN = "unknown"
	CONST_PWD_SET_FALSE = "false"
	CONST_PWD_SET_NO = "no"
	CONST_PWD_SET_TRUE = "true"
	CONST_PWD_SET_YES = "yes"
