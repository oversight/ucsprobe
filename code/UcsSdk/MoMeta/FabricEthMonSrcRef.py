import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthMonSrcRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthMonSrcRef")

	@staticmethod
	def ClassId():
		return "fabricEthMonSrcRef"

	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	SOURCE_DN = "SourceDn"
	SOURCE_TYPE = "SourceType"
	STATUS = "Status"
	TYPE = "Type"

	CONST_SOURCE_TYPE_FCOEUPLINK_PORT = "fcoeuplink-port"
	CONST_SOURCE_TYPE_FCOEUPLINK_PORTCHANNEL = "fcoeuplink-portchannel"
	CONST_SOURCE_TYPE_HOST_PORT = "host-port"
	CONST_SOURCE_TYPE_NAS_PORT = "nas-port"
	CONST_SOURCE_TYPE_NAS_PORT_CHANNEL = "nas-port-channel"
	CONST_SOURCE_TYPE_PORT_CHANNEL = "port-channel"
	CONST_SOURCE_TYPE_SERVER_PORT = "server-port"
	CONST_SOURCE_TYPE_STORAGE = "storage"
	CONST_SOURCE_TYPE_UPLINK_PORT = "uplink-port"
	CONST_SOURCE_TYPE_VHBA = "vhba"
	CONST_SOURCE_TYPE_VLAN = "vlan"
	CONST_SOURCE_TYPE_VM_NIC = "vm-nic"
	CONST_SOURCE_TYPE_VNIC = "vnic"
