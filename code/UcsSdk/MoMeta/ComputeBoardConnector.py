import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeBoardConnector(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeBoardConnector")

	@staticmethod
	def ClassId():
		return "computeBoardConnector"

	BOARD_CONNECTOR_TYPE = "BoardConnectorType"
	DN = "Dn"
	MASTER_SLOT_ID = "MasterSlotId"
	RN = "Rn"
	SLAVE_SLOT_ID = "SlaveSlotId"
	STATUS = "Status"

	CONST_BOARD_CONNECTOR_TYPE_CONN_LINKED = "conn-linked"
	CONST_BOARD_CONNECTOR_TYPE_CONN_UNLINKED = "conn-unlinked"
