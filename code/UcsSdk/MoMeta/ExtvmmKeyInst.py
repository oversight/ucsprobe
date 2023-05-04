import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtvmmKeyInst(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtvmmKeyInst")

	@staticmethod
	def ClassId():
		return "extvmmKeyInst"

	DN = "Dn"
	INST = "Inst"
	KEY = "Key"
	RN = "Rn"
	STATUS = "Status"

