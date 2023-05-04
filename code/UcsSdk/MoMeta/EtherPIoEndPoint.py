import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherPIoEndPoint(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherPIoEndPoint")

	@staticmethod
	def ClassId():
		return "etherPIoEndPoint"

	_END_POINT_DN = "EndPointDn"
	DN = "Dn"
	EP_CLOUD_TYPE = "EpCloudType"
	RN = "Rn"
	STATUS = "Status"
	USR_LBL = "UsrLbl"

	CONST_EP_CLOUD_TYPE_LAN = "lan"
	CONST_EP_CLOUD_TYPE_SAN = "san"
	CONST_EP_CLOUD_TYPE_UNCLASSIFIED = "unclassified"
