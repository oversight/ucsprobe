import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcPortStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcPortStats")

	@staticmethod
	def ClassId():
		return "adaptorFcPortStats"

	DN = "Dn"
	INTERVALS = "Intervals"
	RN = "Rn"
	RX_BAD_FRAMES = "RxBadFrames"
	RX_BAD_FRAMES_DELTA = "RxBadFramesDelta"
	RX_BAD_FRAMES_DELTA_AVG = "RxBadFramesDeltaAvg"
	RX_BAD_FRAMES_DELTA_MAX = "RxBadFramesDeltaMax"
	RX_BAD_FRAMES_DELTA_MIN = "RxBadFramesDeltaMin"
	RX_FRAMES = "RxFrames"
	RX_FRAMES_DELTA = "RxFramesDelta"
	RX_FRAMES_DELTA_AVG = "RxFramesDeltaAvg"
	RX_FRAMES_DELTA_MAX = "RxFramesDeltaMax"
	RX_FRAMES_DELTA_MIN = "RxFramesDeltaMin"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TX_BAD_FRAMES = "TxBadFrames"
	TX_BAD_FRAMES_DELTA = "TxBadFramesDelta"
	TX_BAD_FRAMES_DELTA_AVG = "TxBadFramesDeltaAvg"
	TX_BAD_FRAMES_DELTA_MAX = "TxBadFramesDeltaMax"
	TX_BAD_FRAMES_DELTA_MIN = "TxBadFramesDeltaMin"
	TX_FRAMES = "TxFrames"
	TX_FRAMES_DELTA = "TxFramesDelta"
	TX_FRAMES_DELTA_AVG = "TxFramesDeltaAvg"
	TX_FRAMES_DELTA_MAX = "TxFramesDeltaMax"
	TX_FRAMES_DELTA_MIN = "TxFramesDeltaMin"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
