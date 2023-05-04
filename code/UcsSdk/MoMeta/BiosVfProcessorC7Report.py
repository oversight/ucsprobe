import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfProcessorC7Report(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfProcessorC7Report")

	@staticmethod
	def ClassId():
		return "biosVfProcessorC7Report"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PROCESSOR_C7_REPORT = "VpProcessorC7Report"

	CONST_VP_PROCESSOR_C7_REPORT_DISABLED = "disabled"
	CONST_VP_PROCESSOR_C7_REPORT_ENABLED = "enabled"
	CONST_VP_PROCESSOR_C7_REPORT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PROCESSOR_C7_REPORT_PLATFORM_RECOMMENDED = "platform-recommended"
