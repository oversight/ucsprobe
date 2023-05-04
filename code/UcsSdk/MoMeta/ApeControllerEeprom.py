import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeControllerEeprom(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeControllerEeprom")

	@staticmethod
	def ClassId():
		return "apeControllerEeprom"

	DATABASE_VERSION = "DatabaseVersion"
	DN = "Dn"
	HEARTBEAT_REQUEST = "HeartbeatRequest"
	HEARTBEAT_RESPONSE = "HeartbeatResponse"
	RN = "Rn"
	SIDE = "Side"
	STATUS = "Status"

	CONST_SIDE_LEFT = "Left"
	CONST_SIDE_RIGHT = "Right"
	CONST_SIDE_UNKNOWN = "Unknown"
