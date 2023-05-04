import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherPauseStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherPauseStatsHist")

	@staticmethod
	def ClassId():
		return "etherPauseStatsHist"

	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
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
	XMIT_PAUSE = "XmitPause"
	XMIT_PAUSE_DELTA = "XmitPauseDelta"
	XMIT_PAUSE_DELTA_AVG = "XmitPauseDeltaAvg"
	XMIT_PAUSE_DELTA_MAX = "XmitPauseDeltaMax"
	XMIT_PAUSE_DELTA_MIN = "XmitPauseDeltaMin"

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
