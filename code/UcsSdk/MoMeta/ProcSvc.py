import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcSvc(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcSvc")

	@staticmethod
	def ClassId():
		return "procSvc"

	DN = "Dn"
	ID = "Id"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

