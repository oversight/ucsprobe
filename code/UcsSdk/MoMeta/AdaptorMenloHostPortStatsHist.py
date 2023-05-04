import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloHostPortStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloHostPortStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorMenloHostPortStatsHist"

	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
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

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
