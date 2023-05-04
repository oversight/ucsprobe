import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DiagBladeTest(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DiagBladeTest")

	@staticmethod
	def ClassId():
		return "diagBladeTest"

	DN = "Dn"
	LENGTH = "Length"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_DISK = "disk"
	CONST_TYPE_MEMORY = "memory"
	CONST_TYPE_MEMTEST = "memtest"
	CONST_TYPE_PCI = "pci"
	CONST_TYPE_PROCESSOR = "processor"
	CONST_TYPE_STRESS = "stress"
