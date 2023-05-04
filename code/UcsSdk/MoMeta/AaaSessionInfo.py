import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaSessionInfo(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaSessionInfo")

	@staticmethod
	def ClassId():
		return "aaaSessionInfo"

	ADDRESS = "Address"
	DEST_IP = "DestIp"
	DN = "Dn"
	ETIME = "Etime"
	ID = "Id"
	PRIV = "Priv"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	USER = "User"
	USER_TYPE = "UserType"

	CONST_TYPE_ALL = "all"
	CONST_TYPE_KVM = "kvm"
	CONST_TYPE_SOL = "sol"
	CONST_TYPE_VMEDIA = "vmedia"
	CONST_USER_TYPE_IPMI = "ipmi"
	CONST_USER_TYPE_LOCAL = "local"
	CONST_USER_TYPE_REMOTE = "remote"
