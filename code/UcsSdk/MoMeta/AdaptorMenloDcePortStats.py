import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloDcePortStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloDcePortStats")

	@staticmethod
	def ClassId():
		return "adaptorMenloDcePortStats"

	DN = "Dn"
	INTERVALS = "Intervals"
	MENLO_PORT_INDEX = "MenloPortIndex"
	RN = "Rn"
	RX_PAUSE_CFC = "RxPauseCFC"
	RX_PAUSE_CFCDELTA = "RxPauseCFCDelta"
	RX_PAUSE_CFCDELTA_AVG = "RxPauseCFCDeltaAvg"
	RX_PAUSE_CFCDELTA_MAX = "RxPauseCFCDeltaMax"
	RX_PAUSE_CFCDELTA_MIN = "RxPauseCFCDeltaMin"
	RX_PAUSE_PFC = "RxPausePFC"
	RX_PAUSE_PFCDELTA = "RxPausePFCDelta"
	RX_PAUSE_PFCDELTA_AVG = "RxPausePFCDeltaAvg"
	RX_PAUSE_PFCDELTA_MAX = "RxPausePFCDeltaMax"
	RX_PAUSE_PFCDELTA_MIN = "RxPausePFCDeltaMin"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TX_PAUSE_CFC = "TxPauseCFC"
	TX_PAUSE_CFCDELTA = "TxPauseCFCDelta"
	TX_PAUSE_CFCDELTA_AVG = "TxPauseCFCDeltaAvg"
	TX_PAUSE_CFCDELTA_MAX = "TxPauseCFCDeltaMax"
	TX_PAUSE_CFCDELTA_MIN = "TxPauseCFCDeltaMin"
	TX_PAUSE_PFC = "TxPausePFC"
	TX_PAUSE_PFCDELTA = "TxPausePFCDelta"
	TX_PAUSE_PFCDELTA_AVG = "TxPausePFCDeltaAvg"
	TX_PAUSE_PFCDELTA_MAX = "TxPausePFCDeltaMax"
	TX_PAUSE_PFCDELTA_MIN = "TxPausePFCDeltaMin"
	UPDATE = "Update"

	CONST_MENLO_PORT_INDEX_0 = "0"
	CONST_MENLO_PORT_INDEX_0_A = "0_A"
	CONST_MENLO_PORT_INDEX_0_B = "0_B"
	CONST_MENLO_PORT_INDEX_1 = "1"
	CONST_MENLO_PORT_INDEX_1_A = "1_A"
	CONST_MENLO_PORT_INDEX_1_B = "1_B"
	CONST_MENLO_PORT_INDEX_UNKNOWN = "unknown"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
