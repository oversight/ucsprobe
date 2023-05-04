import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosBootDev(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosBootDev")

	@staticmethod
	def ClassId():
		return "biosBootDev"

	DESCR = "Descr"
	DEVICE_NAME = "DeviceName"
	DN = "Dn"
	ERR_VALUE = "ErrValue"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"

	CONST_ERR_VALUE_FAILURE = "FAILURE"
	CONST_ERR_VALUE_SUCCESS = "SUCCESS"
	CONST_ORDER_1 = "1"
	CONST_ORDER_2 = "2"
	CONST_ORDER_3 = "3"
	CONST_ORDER_4 = "4"
	CONST_ORDER_5 = "5"
	CONST_ORDER_6 = "6"
	CONST_ORDER_7 = "7"
