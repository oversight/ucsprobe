import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricFcMonSrcRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricFcMonSrcRef")

	@staticmethod
	def ClassId():
		return "fabricFcMonSrcRef"

	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	SOURCE_DN = "SourceDn"
	SOURCE_TYPE = "SourceType"
	STATUS = "Status"
	TYPE = "Type"

	CONST_SOURCE_TYPE_PORT_CHANNEL = "port-channel"
	CONST_SOURCE_TYPE_STORAGE = "storage"
	CONST_SOURCE_TYPE_UPLINK_PORT = "uplink-port"
	CONST_SOURCE_TYPE_VHBA = "vhba"
	CONST_SOURCE_TYPE_VSAN = "vsan"
