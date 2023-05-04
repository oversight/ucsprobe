import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSnmpTrap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSnmpTrap")

	@staticmethod
	def ClassId():
		return "commSnmpTrap"

	COMMUNITY = "Community"
	DN = "Dn"
	HOSTNAME = "Hostname"
	NOTIFICATION_TYPE = "NotificationType"
	PORT = "Port"
	RN = "Rn"
	STATUS = "Status"
	V3_PRIVILEGE = "V3Privilege"
	VERSION = "Version"

	CONST_NOTIFICATION_TYPE_INFORMS = "informs"
	CONST_NOTIFICATION_TYPE_TRAPS = "traps"
	CONST_V3_PRIVILEGE_AUTH = "auth"
	CONST_V3_PRIVILEGE_NOAUTH = "noauth"
	CONST_V3_PRIVILEGE_PRIV = "priv"
	CONST_VERSION_V1 = "v1"
	CONST_VERSION_V2C = "v2c"
	CONST_VERSION_V3 = "v3"
