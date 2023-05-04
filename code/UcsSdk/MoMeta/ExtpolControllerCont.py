import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtpolControllerCont(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtpolControllerCont")

	@staticmethod
	def ClassId():
		return "extpolControllerCont"

	DN = "Dn"
	GEN_NUM = "GenNum"
	RN = "Rn"
	STATUS = "Status"

