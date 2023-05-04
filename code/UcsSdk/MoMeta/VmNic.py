import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmNic(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmNic")

	@staticmethod
	def ClassId():
		return "vmNic"

	DN = "Dn"
	DVS_GEN_PORT_ID = "DvsGenPortId"
	DVS_PORT_ID = "DvsPortId"
	DVS_SWITCH_ID = "DvsSwitchId"
	HOST_IF_DN = "HostIfDn"
	MAC_ADDR = "MacAddr"
	NAME = "Name"
	OWNER = "Owner"
	PH_SWITCH_ID = "PhSwitchId"
	PROFILE_ID = "ProfileId"
	PROFILE_NAME = "ProfileName"
	RN = "Rn"
	STATUS = "Status"
	STATUS_CHANGE_TS = "StatusChangeTs"
	SWITCH_ID = "SwitchId"
	TYPE = "Type"
	UUID = "Uuid"
	V_STATUS = "VStatus"
	VC_DN = "VcDn"
	VIF_ID = "VifId"
	VMND_GUID = "VmndGuid"
	VMND_NAME = "VmndName"
	VNIC_DN = "VnicDn"

	CONST_OWNER_CONN_POLICY = "conn_policy"
	CONST_OWNER_LOGICAL = "logical"
	CONST_OWNER_PHYSICAL = "physical"
	CONST_OWNER_POLICY = "policy"
	CONST_OWNER_UNKNOWN = "unknown"
	CONST_PH_SWITCH_ID_A = "A"
	CONST_PH_SWITCH_ID_B = "B"
	CONST_PH_SWITCH_ID_NONE = "NONE"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_TYPE_ETHER = "ether"
	CONST_TYPE_FC = "fc"
	CONST_TYPE_IPC = "ipc"
	CONST_TYPE_SCSI = "scsi"
	CONST_TYPE_UNKNOWN = "unknown"
	CONST_V_STATUS_OFFLINE = "offline"
	CONST_V_STATUS_ONLINE = "online"
	CONST_V_STATUS_UNKNOWN = "unknown"
