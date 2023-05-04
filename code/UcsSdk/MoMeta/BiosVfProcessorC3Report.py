import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfProcessorC3Report(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfProcessorC3Report")

	@staticmethod
	def ClassId():
		return "biosVfProcessorC3Report"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PROCESSOR_C3_REPORT = "VpProcessorC3Report"

	CONST_VP_PROCESSOR_C3_REPORT_ACPI_C2 = "acpi-c2"
	CONST_VP_PROCESSOR_C3_REPORT_ACPI_C3 = "acpi-c3"
	CONST_VP_PROCESSOR_C3_REPORT_DISABLED = "disabled"
	CONST_VP_PROCESSOR_C3_REPORT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PROCESSOR_C3_REPORT_PLATFORM_RECOMMENDED = "platform-recommended"
