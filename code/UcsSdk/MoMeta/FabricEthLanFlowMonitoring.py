import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthLanFlowMonitoring(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthLanFlowMonitoring")

	@staticmethod
	def ClassId():
		return "fabricEthLanFlowMonitoring"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_TYPE_ETH_FLOW_MONITORING = "eth-flow-monitoring"
	CONST_TYPE_SPAN = "span"
	CONST_TYPE_UNKNOWN = "unknown"
