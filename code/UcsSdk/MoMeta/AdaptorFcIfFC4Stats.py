import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcIfFC4Stats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcIfFC4Stats")

	@staticmethod
	def ClassId():
		return "adaptorFcIfFC4Stats"

	CONTROL_REQUESTS = "ControlRequests"
	CONTROL_REQUESTS_DELTA = "ControlRequestsDelta"
	CONTROL_REQUESTS_DELTA_AVG = "ControlRequestsDeltaAvg"
	CONTROL_REQUESTS_DELTA_MAX = "ControlRequestsDeltaMax"
	CONTROL_REQUESTS_DELTA_MIN = "ControlRequestsDeltaMin"
	DN = "Dn"
	INPUT_MEGABYTES = "InputMegabytes"
	INPUT_MEGABYTES_DELTA = "InputMegabytesDelta"
	INPUT_MEGABYTES_DELTA_AVG = "InputMegabytesDeltaAvg"
	INPUT_MEGABYTES_DELTA_MAX = "InputMegabytesDeltaMax"
	INPUT_MEGABYTES_DELTA_MIN = "InputMegabytesDeltaMin"
	INPUT_REQUESTS = "InputRequests"
	INPUT_REQUESTS_DELTA = "InputRequestsDelta"
	INPUT_REQUESTS_DELTA_AVG = "InputRequestsDeltaAvg"
	INPUT_REQUESTS_DELTA_MAX = "InputRequestsDeltaMax"
	INPUT_REQUESTS_DELTA_MIN = "InputRequestsDeltaMin"
	INTERVALS = "Intervals"
	OUTPUT_MEGABYTES = "OutputMegabytes"
	OUTPUT_MEGABYTES_DELTA = "OutputMegabytesDelta"
	OUTPUT_MEGABYTES_DELTA_AVG = "OutputMegabytesDeltaAvg"
	OUTPUT_MEGABYTES_DELTA_MAX = "OutputMegabytesDeltaMax"
	OUTPUT_MEGABYTES_DELTA_MIN = "OutputMegabytesDeltaMin"
	OUTPUT_REQUESTS = "OutputRequests"
	OUTPUT_REQUESTS_DELTA = "OutputRequestsDelta"
	OUTPUT_REQUESTS_DELTA_AVG = "OutputRequestsDeltaAvg"
	OUTPUT_REQUESTS_DELTA_MAX = "OutputRequestsDeltaMax"
	OUTPUT_REQUESTS_DELTA_MIN = "OutputRequestsDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_CONTROL_REQUESTS_NA = "NA"
	CONST_CONTROL_REQUESTS_DELTA_NA = "NA"
	CONST_CONTROL_REQUESTS_DELTA_AVG_NA = "NA"
	CONST_CONTROL_REQUESTS_DELTA_MAX_NA = "NA"
	CONST_CONTROL_REQUESTS_DELTA_MIN_NA = "NA"
	CONST_INPUT_MEGABYTES_NA = "NA"
	CONST_INPUT_MEGABYTES_DELTA_NA = "NA"
	CONST_INPUT_MEGABYTES_DELTA_AVG_NA = "NA"
	CONST_INPUT_MEGABYTES_DELTA_MAX_NA = "NA"
	CONST_INPUT_MEGABYTES_DELTA_MIN_NA = "NA"
	CONST_INPUT_REQUESTS_NA = "NA"
	CONST_INPUT_REQUESTS_DELTA_NA = "NA"
	CONST_INPUT_REQUESTS_DELTA_AVG_NA = "NA"
	CONST_INPUT_REQUESTS_DELTA_MAX_NA = "NA"
	CONST_INPUT_REQUESTS_DELTA_MIN_NA = "NA"
	CONST_OUTPUT_MEGABYTES_NA = "NA"
	CONST_OUTPUT_MEGABYTES_DELTA_NA = "NA"
	CONST_OUTPUT_MEGABYTES_DELTA_AVG_NA = "NA"
	CONST_OUTPUT_MEGABYTES_DELTA_MAX_NA = "NA"
	CONST_OUTPUT_MEGABYTES_DELTA_MIN_NA = "NA"
	CONST_OUTPUT_REQUESTS_NA = "NA"
	CONST_OUTPUT_REQUESTS_DELTA_NA = "NA"
	CONST_OUTPUT_REQUESTS_DELTA_AVG_NA = "NA"
	CONST_OUTPUT_REQUESTS_DELTA_MAX_NA = "NA"
	CONST_OUTPUT_REQUESTS_DELTA_MIN_NA = "NA"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
