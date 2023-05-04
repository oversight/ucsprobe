import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicEthLif(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicEthLif")

	@staticmethod
	def ClassId():
		return "vnicEthLif"

	ADDR = "Addr"
	DN = "Dn"
	NAME = "Name"
	NIC_DN = "NicDn"
	OWNER = "Owner"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TYPE = "Type"
	VNIC_DN = "VnicDn"

	CONST_OWNER_CONN_POLICY = "conn_policy"
	CONST_OWNER_LOGICAL = "logical"
	CONST_OWNER_PHYSICAL = "physical"
	CONST_OWNER_POLICY = "policy"
	CONST_OWNER_UNKNOWN = "unknown"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_TYPE_ETHER = "ether"
	CONST_TYPE_FC = "fc"
	CONST_TYPE_IPC = "ipc"
	CONST_TYPE_SCSI = "scsi"
	CONST_TYPE_UNKNOWN = "unknown"
