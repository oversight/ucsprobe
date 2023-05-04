import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherErrStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherErrStats")

	@staticmethod
	def ClassId():
		return "etherErrStats"

	ALIGN = "Align"
	ALIGN_DELTA = "AlignDelta"
	ALIGN_DELTA_AVG = "AlignDeltaAvg"
	ALIGN_DELTA_MAX = "AlignDeltaMax"
	ALIGN_DELTA_MIN = "AlignDeltaMin"
	DEFERRED_TX = "DeferredTx"
	DEFERRED_TX_DELTA = "DeferredTxDelta"
	DEFERRED_TX_DELTA_AVG = "DeferredTxDeltaAvg"
	DEFERRED_TX_DELTA_MAX = "DeferredTxDeltaMax"
	DEFERRED_TX_DELTA_MIN = "DeferredTxDeltaMin"
	DN = "Dn"
	FCS = "Fcs"
	FCS_DELTA = "FcsDelta"
	FCS_DELTA_AVG = "FcsDeltaAvg"
	FCS_DELTA_MAX = "FcsDeltaMax"
	FCS_DELTA_MIN = "FcsDeltaMin"
	INT_MAC_RX = "IntMacRx"
	INT_MAC_RX_DELTA = "IntMacRxDelta"
	INT_MAC_RX_DELTA_AVG = "IntMacRxDeltaAvg"
	INT_MAC_RX_DELTA_MAX = "IntMacRxDeltaMax"
	INT_MAC_RX_DELTA_MIN = "IntMacRxDeltaMin"
	INT_MAC_TX = "IntMacTx"
	INT_MAC_TX_DELTA = "IntMacTxDelta"
	INT_MAC_TX_DELTA_AVG = "IntMacTxDeltaAvg"
	INT_MAC_TX_DELTA_MAX = "IntMacTxDeltaMax"
	INT_MAC_TX_DELTA_MIN = "IntMacTxDeltaMin"
	INTERVALS = "Intervals"
	OUT_DISCARD = "OutDiscard"
	OUT_DISCARD_DELTA = "OutDiscardDelta"
	OUT_DISCARD_DELTA_AVG = "OutDiscardDeltaAvg"
	OUT_DISCARD_DELTA_MAX = "OutDiscardDeltaMax"
	OUT_DISCARD_DELTA_MIN = "OutDiscardDeltaMin"
	RCV = "Rcv"
	RCV_DELTA = "RcvDelta"
	RCV_DELTA_AVG = "RcvDeltaAvg"
	RCV_DELTA_MAX = "RcvDeltaMax"
	RCV_DELTA_MIN = "RcvDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UNDER_SIZE = "UnderSize"
	UNDER_SIZE_DELTA = "UnderSizeDelta"
	UNDER_SIZE_DELTA_AVG = "UnderSizeDeltaAvg"
	UNDER_SIZE_DELTA_MAX = "UnderSizeDeltaMax"
	UNDER_SIZE_DELTA_MIN = "UnderSizeDeltaMin"
	UPDATE = "Update"
	XMIT = "Xmit"
	XMIT_DELTA = "XmitDelta"
	XMIT_DELTA_AVG = "XmitDeltaAvg"
	XMIT_DELTA_MAX = "XmitDeltaMax"
	XMIT_DELTA_MIN = "XmitDeltaMin"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"