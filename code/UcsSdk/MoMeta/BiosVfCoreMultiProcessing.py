import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfCoreMultiProcessing(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfCoreMultiProcessing")

	@staticmethod
	def ClassId():
		return "biosVfCoreMultiProcessing"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_CORE_MULTI_PROCESSING = "VpCoreMultiProcessing"

	CONST_VP_CORE_MULTI_PROCESSING_1 = "1"
	CONST_VP_CORE_MULTI_PROCESSING_10 = "10"
	CONST_VP_CORE_MULTI_PROCESSING_11 = "11"
	CONST_VP_CORE_MULTI_PROCESSING_12 = "12"
	CONST_VP_CORE_MULTI_PROCESSING_13 = "13"
	CONST_VP_CORE_MULTI_PROCESSING_14 = "14"
	CONST_VP_CORE_MULTI_PROCESSING_15 = "15"
	CONST_VP_CORE_MULTI_PROCESSING_2 = "2"
	CONST_VP_CORE_MULTI_PROCESSING_3 = "3"
	CONST_VP_CORE_MULTI_PROCESSING_4 = "4"
	CONST_VP_CORE_MULTI_PROCESSING_5 = "5"
	CONST_VP_CORE_MULTI_PROCESSING_6 = "6"
	CONST_VP_CORE_MULTI_PROCESSING_7 = "7"
	CONST_VP_CORE_MULTI_PROCESSING_8 = "8"
	CONST_VP_CORE_MULTI_PROCESSING_9 = "9"
	CONST_VP_CORE_MULTI_PROCESSING_ALL = "all"
	CONST_VP_CORE_MULTI_PROCESSING_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_CORE_MULTI_PROCESSING_PLATFORM_RECOMMENDED = "platform-recommended"
