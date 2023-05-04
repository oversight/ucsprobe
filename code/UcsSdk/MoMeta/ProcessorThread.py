import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcessorThread(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcessorThread")

	@staticmethod
	def ClassId():
		return "processorThread"

	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"

