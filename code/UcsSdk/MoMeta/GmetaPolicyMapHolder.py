import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class GmetaPolicyMapHolder(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"GmetaPolicyMapHolder")

	@staticmethod
	def ClassId():
		return "gmetaPolicyMapHolder"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

