import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcIfFrameStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcIfFrameStats")

	@staticmethod
	def ClassId():
		return "adaptorFcIfFrameStats"

	DN = "Dn"
	DUMPED_FRAMES = "DumpedFrames"
	DUMPED_FRAMES_DELTA = "DumpedFramesDelta"
	DUMPED_FRAMES_DELTA_AVG = "DumpedFramesDeltaAvg"
	DUMPED_FRAMES_DELTA_MAX = "DumpedFramesDeltaMax"
	DUMPED_FRAMES_DELTA_MIN = "DumpedFramesDeltaMin"
	ERROR_FRAMES = "ErrorFrames"
	ERROR_FRAMES_DELTA = "ErrorFramesDelta"
	ERROR_FRAMES_DELTA_AVG = "ErrorFramesDeltaAvg"
	ERROR_FRAMES_DELTA_MAX = "ErrorFramesDeltaMax"
	ERROR_FRAMES_DELTA_MIN = "ErrorFramesDeltaMin"
	INTERVALS = "Intervals"
	RN = "Rn"
	RX_FRAMES = "RxFrames"
	RX_FRAMES_DELTA = "RxFramesDelta"
	RX_FRAMES_DELTA_AVG = "RxFramesDeltaAvg"
	RX_FRAMES_DELTA_MAX = "RxFramesDeltaMax"
	RX_FRAMES_DELTA_MIN = "RxFramesDeltaMin"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TX_FRAMES = "TxFrames"
	TX_FRAMES_DELTA = "TxFramesDelta"
	TX_FRAMES_DELTA_AVG = "TxFramesDeltaAvg"
	TX_FRAMES_DELTA_MAX = "TxFramesDeltaMax"
	TX_FRAMES_DELTA_MIN = "TxFramesDeltaMin"
	UPDATE = "Update"

	CONST_DUMPED_FRAMES_NA = "NA"
	CONST_DUMPED_FRAMES_DELTA_NA = "NA"
	CONST_DUMPED_FRAMES_DELTA_AVG_NA = "NA"
	CONST_DUMPED_FRAMES_DELTA_MAX_NA = "NA"
	CONST_DUMPED_FRAMES_DELTA_MIN_NA = "NA"
	CONST_ERROR_FRAMES_NA = "NA"
	CONST_ERROR_FRAMES_DELTA_NA = "NA"
	CONST_ERROR_FRAMES_DELTA_AVG_NA = "NA"
	CONST_ERROR_FRAMES_DELTA_MAX_NA = "NA"
	CONST_ERROR_FRAMES_DELTA_MIN_NA = "NA"
	CONST_RX_FRAMES_NA = "NA"
	CONST_RX_FRAMES_DELTA_NA = "NA"
	CONST_RX_FRAMES_DELTA_AVG_NA = "NA"
	CONST_RX_FRAMES_DELTA_MAX_NA = "NA"
	CONST_RX_FRAMES_DELTA_MIN_NA = "NA"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
	CONST_TX_FRAMES_NA = "NA"
	CONST_TX_FRAMES_DELTA_NA = "NA"
	CONST_TX_FRAMES_DELTA_AVG_NA = "NA"
	CONST_TX_FRAMES_DELTA_MAX_NA = "NA"
	CONST_TX_FRAMES_DELTA_MIN_NA = "NA"
