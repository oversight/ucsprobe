import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MemoryErrorStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MemoryErrorStats")

	@staticmethod
	def ClassId():
		return "memoryErrorStats"

	ADDRESS_PARITY_ERRORS = "AddressParityErrors"
	ADDRESS_PARITY_ERRORS15_MIN = "AddressParityErrors15Min"
	ADDRESS_PARITY_ERRORS15_MIN_H = "AddressParityErrors15MinH"
	ADDRESS_PARITY_ERRORS1_DAY = "AddressParityErrors1Day"
	ADDRESS_PARITY_ERRORS1_DAY_H = "AddressParityErrors1DayH"
	ADDRESS_PARITY_ERRORS1_HOUR = "AddressParityErrors1Hour"
	ADDRESS_PARITY_ERRORS1_HOUR_H = "AddressParityErrors1HourH"
	ADDRESS_PARITY_ERRORS1_WEEK = "AddressParityErrors1Week"
	ADDRESS_PARITY_ERRORS1_WEEK_H = "AddressParityErrors1WeekH"
	ADDRESS_PARITY_ERRORS2_WEEKS = "AddressParityErrors2Weeks"
	ADDRESS_PARITY_ERRORS2_WEEKS_H = "AddressParityErrors2WeeksH"
	DN = "Dn"
	ECC_MULTIBIT_ERRORS = "EccMultibitErrors"
	ECC_MULTIBIT_ERRORS15_MIN = "EccMultibitErrors15Min"
	ECC_MULTIBIT_ERRORS15_MIN_H = "EccMultibitErrors15MinH"
	ECC_MULTIBIT_ERRORS1_DAY = "EccMultibitErrors1Day"
	ECC_MULTIBIT_ERRORS1_DAY_H = "EccMultibitErrors1DayH"
	ECC_MULTIBIT_ERRORS1_HOUR = "EccMultibitErrors1Hour"
	ECC_MULTIBIT_ERRORS1_HOUR_H = "EccMultibitErrors1HourH"
	ECC_MULTIBIT_ERRORS1_WEEK = "EccMultibitErrors1Week"
	ECC_MULTIBIT_ERRORS1_WEEK_H = "EccMultibitErrors1WeekH"
	ECC_MULTIBIT_ERRORS2_WEEKS = "EccMultibitErrors2Weeks"
	ECC_MULTIBIT_ERRORS2_WEEKS_H = "EccMultibitErrors2WeeksH"
	ECC_SINGLEBIT_ERRORS = "EccSinglebitErrors"
	ECC_SINGLEBIT_ERRORS15_MIN = "EccSinglebitErrors15Min"
	ECC_SINGLEBIT_ERRORS15_MIN_H = "EccSinglebitErrors15MinH"
	ECC_SINGLEBIT_ERRORS1_DAY = "EccSinglebitErrors1Day"
	ECC_SINGLEBIT_ERRORS1_DAY_H = "EccSinglebitErrors1DayH"
	ECC_SINGLEBIT_ERRORS1_HOUR = "EccSinglebitErrors1Hour"
	ECC_SINGLEBIT_ERRORS1_HOUR_H = "EccSinglebitErrors1HourH"
	ECC_SINGLEBIT_ERRORS1_WEEK = "EccSinglebitErrors1Week"
	ECC_SINGLEBIT_ERRORS1_WEEK_H = "EccSinglebitErrors1WeekH"
	ECC_SINGLEBIT_ERRORS2_WEEKS = "EccSinglebitErrors2Weeks"
	ECC_SINGLEBIT_ERRORS2_WEEKS_H = "EccSinglebitErrors2WeeksH"
	INTERVALS = "Intervals"
	MISMATCH_ERRORS = "MismatchErrors"
	MISMATCH_ERRORS15_MIN = "MismatchErrors15Min"
	MISMATCH_ERRORS15_MIN_H = "MismatchErrors15MinH"
	MISMATCH_ERRORS1_DAY = "MismatchErrors1Day"
	MISMATCH_ERRORS1_DAY_H = "MismatchErrors1DayH"
	MISMATCH_ERRORS1_HOUR = "MismatchErrors1Hour"
	MISMATCH_ERRORS1_HOUR_H = "MismatchErrors1HourH"
	MISMATCH_ERRORS1_WEEK = "MismatchErrors1Week"
	MISMATCH_ERRORS1_WEEK_H = "MismatchErrors1WeekH"
	MISMATCH_ERRORS2_WEEKS = "MismatchErrors2Weeks"
	MISMATCH_ERRORS2_WEEKS_H = "MismatchErrors2WeeksH"
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
