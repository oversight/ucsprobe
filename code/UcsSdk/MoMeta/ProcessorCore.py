import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcessorCore(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcessorCore")

	@staticmethod
	def ClassId():
		return "processorCore"

	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"

