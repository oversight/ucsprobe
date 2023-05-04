import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtvmmKeyRing(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtvmmKeyRing")

	@staticmethod
	def ClassId():
		return "extvmmKeyRing"

	CERT_FILE = "CertFile"
	DN = "Dn"
	LOCATION = "Location"
	NAME = "Name"
	PATH = "Path"
	RN = "Rn"
	STATUS = "Status"

	CONST_LOCATION_FTP = "ftp"
	CONST_LOCATION_NONE = "none"
	CONST_LOCATION_SCP = "scp"
	CONST_LOCATION_SFTP = "sftp"
	CONST_LOCATION_TFTP = "tftp"
	CONST_LOCATION_VOLATILE = "volatile"
	CONST_LOCATION_WORKSPACE = "workspace"
