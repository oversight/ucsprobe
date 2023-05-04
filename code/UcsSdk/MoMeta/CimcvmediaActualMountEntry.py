import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CimcvmediaActualMountEntry(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CimcvmediaActualMountEntry")

	@staticmethod
	def ClassId():
		return "cimcvmediaActualMountEntry"

	DEVICE_TYPE = "DeviceType"
	DN = "Dn"
	ENC_PWD = "EncPwd"
	ERROR_TYPE = "ErrorType"
	IMAGE_FILE_NAME = "ImageFileName"
	IMAGE_PATH = "ImagePath"
	MAPPING_NAME = "MappingName"
	MOUNT_PROTOCOL = "MountProtocol"
	OPER_MOUNT_STATUS = "OperMountStatus"
	PASSWORD = "Password"
	PWD_SET = "PwdSet"
	REMOTE_HOST = "RemoteHost"
	REMOTE_IP_ADDRESS = "RemoteIpAddress"
	REMOTE_PORT = "RemotePort"
	RN = "Rn"
	STATUS = "Status"
	USER_ID = "UserId"
	VIRTUAL_DISK_ID = "VirtualDiskId"

	CONST_DEVICE_TYPE_CDD = "cdd"
	CONST_DEVICE_TYPE_HDD = "hdd"
	CONST_DEVICE_TYPE_UNKNOWN = "unknown"
	CONST_ERROR_TYPE_ALREADY_MAPPED = "already-mapped"
	CONST_ERROR_TYPE_AUTHENTICATION_FAILED = "authentication-failed"
	CONST_ERROR_TYPE_BAD_PARAM = "bad-param"
	CONST_ERROR_TYPE_BAD_PATH = "bad-path"
	CONST_ERROR_TYPE_CONNECTION_REJECTED = "connection-rejected"
	CONST_ERROR_TYPE_CONNECTION_TIMEOUT = "connection-timeout"
	CONST_ERROR_TYPE_DISK_EJECTED = "disk-ejected"
	CONST_ERROR_TYPE_DISK_IO_FAILURE = "disk-io-failure"
	CONST_ERROR_TYPE_FILE_NOT_FOUND = "file-not-found"
	CONST_ERROR_TYPE_GENERIC_FAILURE = "generic-failure"
	CONST_ERROR_TYPE_IMAGE_STORE_FULL = "image-store-full"
	CONST_ERROR_TYPE_IMGAGE_DELETED = "imgage-deleted"
	CONST_ERROR_TYPE_INVALID_ARGUMENT = "invalid-argument"
	CONST_ERROR_TYPE_INVALID_VDISK_TYPE = "invalid-vdisk-type"
	CONST_ERROR_TYPE_INVALID_VDISK_USAGE = "invalid-vdisk-usage"
	CONST_ERROR_TYPE_MOUNT_IN_USE = "mount-in-use"
	CONST_ERROR_TYPE_NONE = "none"
	CONST_ERROR_TYPE_OPEN_RO_FAILED = "open-ro-failed"
	CONST_ERROR_TYPE_OPEN_RW_FAILED = "open-rw-failed"
	CONST_ERROR_TYPE_POSTMAP_ERROR = "postmap-error"
	CONST_ERROR_TYPE_UNKNOWN = "unknown"
	CONST_ERROR_TYPE_WRITE_TO_READONLY_FILE = "write-to-readonly-file"
	CONST_MOUNT_PROTOCOL_CIFS = "cifs"
	CONST_MOUNT_PROTOCOL_HTTP = "http"
	CONST_MOUNT_PROTOCOL_HTTPS = "https"
	CONST_MOUNT_PROTOCOL_NFS = "nfs"
	CONST_MOUNT_PROTOCOL_UNKNOWN = "unknown"
	CONST_OPER_MOUNT_STATUS_MOUNT_FAILED = "mount-failed"
	CONST_OPER_MOUNT_STATUS_MOUNTED = "mounted"
	CONST_OPER_MOUNT_STATUS_MOUNTING = "mounting"
	CONST_OPER_MOUNT_STATUS_NOT_MOUNTED = "not-mounted"
	CONST_OPER_MOUNT_STATUS_UNKNOWN = "unknown"
	CONST_OPER_MOUNT_STATUS_UNMOUNT_FAILED = "unmount-failed"
	CONST_OPER_MOUNT_STATUS_UNMOUNTING = "unmounting"
	CONST_PWD_SET_FALSE = "false"
	CONST_PWD_SET_NO = "no"
	CONST_PWD_SET_TRUE = "true"
	CONST_PWD_SET_YES = "yes"
