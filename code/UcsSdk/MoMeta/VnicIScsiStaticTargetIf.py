import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIScsiStaticTargetIf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIScsiStaticTargetIf")

	@staticmethod
	def ClassId():
		return "vnicIScsiStaticTargetIf"

	AUTH_PROFILE_NAME = "AuthProfileName"
	DN = "Dn"
	IP_ADDRESS = "IpAddress"
	NAME = "Name"
	OPER_AUTH_PROFILE_NAME = "OperAuthProfileName"
	PORT = "Port"
	PRIORITY = "Priority"
	RN = "Rn"
	STATUS = "Status"

