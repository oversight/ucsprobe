import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class GmetaPolicyMapElement(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"GmetaPolicyMapElement")

	@staticmethod
	def ClassId():
		return "gmetaPolicyMapElement"

	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

