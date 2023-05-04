import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootLan(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootLan")

	@staticmethod
	def ClassId():
		return "lsbootLan"

	ACCESS = "Access"
	DN = "Dn"
	ORDER = "Order"
	PROT = "Prot"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ACCESS_READ_ONLY = "read-only"
	CONST_ACCESS_READ_ONLY_LOCAL = "read-only-local"
	CONST_ACCESS_READ_ONLY_REMOTE = "read-only-remote"
	CONST_ACCESS_READ_ONLY_REMOTE_CIMC = "read-only-remote-cimc"
	CONST_ACCESS_READ_WRITE = "read-write"
	CONST_ACCESS_READ_WRITE_DRIVE = "read-write-drive"
	CONST_ACCESS_READ_WRITE_LOCAL = "read-write-local"
	CONST_ACCESS_READ_WRITE_REMOTE = "read-write-remote"
	CONST_ACCESS_READ_WRITE_REMOTE_CIMC = "read-write-remote-cimc"
	CONST_PROT_GPXE = "gpxe"
	CONST_PROT_I_SCSI = "iSCSI"
	CONST_PROT_PXE = "pxe"
	CONST_TYPE_ISCSI = "iscsi"
	CONST_TYPE_LAN = "lan"
	CONST_TYPE_SAN = "san"
	CONST_TYPE_STORAGE = "storage"
	CONST_TYPE_VIRTUAL_MEDIA = "virtual-media"
