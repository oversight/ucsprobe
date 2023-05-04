import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorIscsiTargetIf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorIscsiTargetIf")

	@staticmethod
	def ClassId():
		return "adaptorIscsiTargetIf"

	DHCP_VENDOR_ID = "DhcpVendorId"
	DN = "Dn"
	IP_ADDRESS = "IpAddress"
	LUN = "Lun"
	NAME = "Name"
	PORT_NUMBER = "PortNumber"
	PRIORITY = "Priority"
	RN = "Rn"
	STATUS = "Status"

