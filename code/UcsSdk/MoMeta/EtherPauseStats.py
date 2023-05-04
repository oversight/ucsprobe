import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherPauseStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherPauseStats")

	@staticmethod
	def ClassId():
		return "etherPauseStats"

	DN = "Dn"
	INTERVALS = "Intervals"
	RECV_PAUSE = "RecvPause"
	RECV_PAUSE_DELTA = "RecvPauseDelta"
	RECV_PAUSE_DELTA_AVG = "RecvPauseDeltaAvg"
	RECV_PAUSE_DELTA_MAX = "RecvPauseDeltaMax"
	RECV_PAUSE_DELTA_MIN = "RecvPauseDeltaMin"
	RESETS = "Resets"
	RESETS_DELTA = "ResetsDelta"
	RESETS_DELTA_AVG = "ResetsDeltaAvg"
	RESETS_DELTA_MAX = "ResetsDeltaMax"
	RESETS_DELTA_MIN = "ResetsDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"
	XMIT_PAUSE = "XmitPause"
	XMIT_PAUSE_DELTA = "XmitPauseDelta"
	XMIT_PAUSE_DELTA_AVG = "XmitPauseDeltaAvg"
	XMIT_PAUSE_DELTA_MAX = "XmitPauseDeltaMax"
	XMIT_PAUSE_DELTA_MIN = "XmitPauseDeltaMin"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
