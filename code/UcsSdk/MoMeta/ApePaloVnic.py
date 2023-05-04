import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApePaloVnic(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApePaloVnic")

	@staticmethod
	def ClassId():
		return "apePaloVnic"

	COOKIE = "Cookie"
	COS = "Cos"
	DN = "Dn"
	FAILOVER = "Failover"
	MAC = "Mac"
	MTU = "Mtu"
	NAME = "Name"
	NIC_DN = "NicDn"
	PASS_THRU = "PassThru"
	RN = "Rn"
	STATE = "State"
	STATUS = "Status"
	STDBY_VIF_ID = "StdbyVifId"
	TYPE = "Type"
	UPLINK_PORT_ID = "UplinkPortId"
	VIF_ID = "VifId"
	VIF_TYPE = "VifType"
	VLAN_ID = "VlanId"
	VM_WARE = "VmWare"
	VNTAG = "Vntag"
	WWNN = "Wwnn"

	CONST_FAILOVER_FALSE = "false"
	CONST_FAILOVER_NO = "no"
	CONST_FAILOVER_TRUE = "true"
	CONST_FAILOVER_YES = "yes"
	CONST_PASS_THRU_FALSE = "false"
	CONST_PASS_THRU_NO = "no"
	CONST_PASS_THRU_TRUE = "true"
	CONST_PASS_THRU_YES = "yes"
	CONST_STATE_CREATE_PEND = "CreatePend"
	CONST_STATE_CREATING = "Creating"
	CONST_STATE_DESTROY_PEND = "DestroyPend"
	CONST_STATE_DESTROYING = "Destroying"
	CONST_STATE_MODIFY_PEND = "ModifyPend"
	CONST_STATE_MODIFYING = "Modifying"
	CONST_STATE_PRESENT = "Present"
	CONST_STATE_UNKNOWN = "Unknown"
	CONST_TYPE_ETH = "Eth"
	CONST_TYPE_FC = "Fc"
	CONST_TYPE_SCSI = "Scsi"
	CONST_TYPE_UNKNOWN = "Unknown"
	CONST_VM_WARE_FALSE = "false"
	CONST_VM_WARE_NO = "no"
	CONST_VM_WARE_TRUE = "true"
	CONST_VM_WARE_YES = "yes"
