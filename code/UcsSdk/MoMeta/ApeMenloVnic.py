import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeMenloVnic(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeMenloVnic")

	@staticmethod
	def ClassId():
		return "apeMenloVnic"

	COOKIE = "Cookie"
	COS = "Cos"
	DN = "Dn"
	MAC = "Mac"
	NAME = "Name"
	NIC_DN = "NicDn"
	PIF_ID = "PifId"
	RN = "Rn"
	STATE = "State"
	STATUS = "Status"
	TYPE = "Type"
	UPLINK_PORT_ID = "UplinkPortId"
	VIF_ID = "VifId"
	VIF_TYPE = "VifType"
	VLAN_ID = "VlanId"
	VNTAG = "Vntag"
	WWNN = "Wwnn"
	WWPN = "Wwpn"

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
