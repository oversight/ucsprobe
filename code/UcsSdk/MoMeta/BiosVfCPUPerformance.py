import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfCPUPerformance(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfCPUPerformance")

	@staticmethod
	def ClassId():
		return "biosVfCPUPerformance"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_CPUPERFORMANCE = "VpCPUPerformance"

	CONST_VP_CPUPERFORMANCE_ENTERPRISE = "enterprise"
	CONST_VP_CPUPERFORMANCE_HIGH_THROUGHPUT = "high-throughput"
	CONST_VP_CPUPERFORMANCE_HPC = "hpc"
	CONST_VP_CPUPERFORMANCE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_CPUPERFORMANCE_PLATFORM_RECOMMENDED = "platform-recommended"
