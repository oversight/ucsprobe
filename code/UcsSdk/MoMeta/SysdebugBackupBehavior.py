import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugBackupBehavior(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugBackupBehavior")

	@staticmethod
	def ClassId():
		return "sysdebugBackupBehavior"

	ACTION = "Action"
	CLEAR_ON_BACKUP = "ClearOnBackup"
	DN = "Dn"
	FORMAT = "Format"
	HOSTNAME = "Hostname"
	INTERVAL = "Interval"
	PROTO = "Proto"
	PWD = "Pwd"
	REMOTE_PATH = "RemotePath"
	RN = "Rn"
	STATUS = "Status"
	USER = "User"

	CONST_CLEAR_ON_BACKUP_FALSE = "false"
	CONST_CLEAR_ON_BACKUP_NO = "no"
	CONST_CLEAR_ON_BACKUP_TRUE = "true"
	CONST_CLEAR_ON_BACKUP_YES = "yes"
	CONST_FORMAT_ASCII = "ascii"
	CONST_FORMAT_BINARY = "binary"
	CONST_INTERVAL_1HOUR = "1hour"
	CONST_INTERVAL_1MONTH = "1month"
	CONST_INTERVAL_1WEEK = "1week"
	CONST_INTERVAL_24HOURS = "24hours"
	CONST_INTERVAL_2HOURS = "2hours"
	CONST_INTERVAL_4HOURS = "4hours"
	CONST_INTERVAL_8HOURS = "8hours"
	CONST_INTERVAL_NEVER = "never"
	CONST_PROTO_FTP = "ftp"
	CONST_PROTO_HTTP = "http"
	CONST_PROTO_NFS_COPY = "nfs-copy"
	CONST_PROTO_NONE = "none"
	CONST_PROTO_SCP = "scp"
	CONST_PROTO_SFTP = "sftp"
	CONST_PROTO_TFTP = "tftp"
