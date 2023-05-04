import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcessorQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcessorQual")

	@staticmethod
	def ClassId():
		return "processorQual"

	ARCH = "Arch"
	DN = "Dn"
	MAX_CORES = "MaxCores"
	MAX_PROCS = "MaxProcs"
	MAX_THREADS = "MaxThreads"
	MIN_CORES = "MinCores"
	MIN_PROCS = "MinProcs"
	MIN_THREADS = "MinThreads"
	MODEL = "Model"
	RN = "Rn"
	SPEED = "Speed"
	STATUS = "Status"
	STEPPING = "Stepping"

	CONST_ARCH_DUAL_CORE_OPTERON = "Dual-Core_Opteron"
	CONST_ARCH_INTEL_P4_C = "Intel_P4_C"
	CONST_ARCH_OPTERON = "Opteron"
	CONST_ARCH_PENTIUM_4 = "Pentium_4"
	CONST_ARCH_TURION_64 = "Turion_64"
	CONST_ARCH_XEON = "Xeon"
	CONST_ARCH_XEON_MP = "Xeon_MP"
	CONST_ARCH_ANY = "any"
	CONST_MAX_CORES_UNSPECIFIED = "unspecified"
	CONST_MAX_PROCS_UNSPECIFIED = "unspecified"
	CONST_MAX_THREADS_UNSPECIFIED = "unspecified"
	CONST_MIN_CORES_UNSPECIFIED = "unspecified"
	CONST_MIN_PROCS_UNSPECIFIED = "unspecified"
	CONST_MIN_THREADS_UNSPECIFIED = "unspecified"
	CONST_SPEED_UNSPECIFIED = "unspecified"
	CONST_STEPPING_UNSPECIFIED = "unspecified"
