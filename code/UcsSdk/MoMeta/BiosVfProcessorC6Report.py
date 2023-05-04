import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfProcessorC6Report(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfProcessorC6Report")

	@staticmethod
	def ClassId():
		return "biosVfProcessorC6Report"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PROCESSOR_C6_REPORT = "VpProcessorC6Report"

	CONST_VP_PROCESSOR_C6_REPORT_DISABLED = "disabled"
	CONST_VP_PROCESSOR_C6_REPORT_ENABLED = "enabled"
	CONST_VP_PROCESSOR_C6_REPORT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PROCESSOR_C6_REPORT_PLATFORM_RECOMMENDED = "platform-recommended"
