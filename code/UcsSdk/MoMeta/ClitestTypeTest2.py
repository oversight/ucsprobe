import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ClitestTypeTest2(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ClitestTypeTest2")

	@staticmethod
	def ClassId():
		return "clitestTypeTest2"

	A_PARTIAL_ENUM = "APartialEnum"
	ABITMASK = "Abitmask"
	ACHARBUF = "Acharbuf"
	DN = "Dn"
	FILE_DIR = "FileDir"
	FILE_HOST = "FileHost"
	FILE_NAME = "FileName"
	FILE_PASSWD = "FilePasswd"
	FILE_PATH = "FilePath"
	FILE_PORT = "FilePort"
	FILE_PROTO = "FileProto"
	FILE_USER = "FileUser"
	RN = "Rn"
	STATUS = "Status"

	CONST_A_PARTIAL_ENUM_DEFAULT = "default"
	CONST_A_PARTIAL_ENUM_UNTAGGED = "untagged"
	CONST_FILE_PROTO_FTP = "ftp"
	CONST_FILE_PROTO_HTTP = "http"
	CONST_FILE_PROTO_NFS_COPY = "nfs-copy"
	CONST_FILE_PROTO_NONE = "none"
	CONST_FILE_PROTO_SCP = "scp"
	CONST_FILE_PROTO_SFTP = "sftp"
	CONST_FILE_PROTO_TFTP = "tftp"
