import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePCIeFatalProtocolStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePCIeFatalProtocolStats")

	@staticmethod
	def ClassId():
		return "computePCIeFatalProtocolStats"

	DLLP_ERRORS = "DllpErrors"
	DLLP_ERRORS15_MIN = "DllpErrors15Min"
	DLLP_ERRORS15_MIN_H = "DllpErrors15MinH"
	DLLP_ERRORS1_DAY = "DllpErrors1Day"
	DLLP_ERRORS1_DAY_H = "DllpErrors1DayH"
	DLLP_ERRORS1_HOUR = "DllpErrors1Hour"
	DLLP_ERRORS1_HOUR_H = "DllpErrors1HourH"
	DLLP_ERRORS1_WEEK = "DllpErrors1Week"
	DLLP_ERRORS1_WEEK_H = "DllpErrors1WeekH"
	DLLP_ERRORS2_WEEKS = "DllpErrors2Weeks"
	DLLP_ERRORS2_WEEKS_H = "DllpErrors2WeeksH"
	DN = "Dn"
	FLOW_CONTROL_ERRORS = "FlowControlErrors"
	FLOW_CONTROL_ERRORS15_MIN = "FlowControlErrors15Min"
	FLOW_CONTROL_ERRORS15_MIN_H = "FlowControlErrors15MinH"
	FLOW_CONTROL_ERRORS1_DAY = "FlowControlErrors1Day"
	FLOW_CONTROL_ERRORS1_DAY_H = "FlowControlErrors1DayH"
	FLOW_CONTROL_ERRORS1_HOUR = "FlowControlErrors1Hour"
	FLOW_CONTROL_ERRORS1_HOUR_H = "FlowControlErrors1HourH"
	FLOW_CONTROL_ERRORS1_WEEK = "FlowControlErrors1Week"
	FLOW_CONTROL_ERRORS1_WEEK_H = "FlowControlErrors1WeekH"
	FLOW_CONTROL_ERRORS2_WEEKS = "FlowControlErrors2Weeks"
	FLOW_CONTROL_ERRORS2_WEEKS_H = "FlowControlErrors2WeeksH"
	INTERVALS = "Intervals"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
