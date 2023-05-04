import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowMonitorRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowMonitorRef")

	@staticmethod
	def ClassId():
		return "fabricNetflowMonitorRef"

	DIRECTION = "Direction"
	DN = "Dn"
	INDEX = "Index"
	NF_MONITOR_NAME = "NfMonitorName"
	OPER_NF_MONITOR_NAME = "OperNfMonitorName"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_DIRECTION_RECEIVE = "receive"
	CONST_DIRECTION_TRANSMIT = "transmit"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
