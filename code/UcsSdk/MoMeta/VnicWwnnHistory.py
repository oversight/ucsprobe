import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicWwnnHistory(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicWwnnHistory")

	@staticmethod
	def ClassId():
		return "vnicWwnnHistory"

	DN = "Dn"
	OLDWWNN = "Oldwwnn"
	RN = "Rn"
	STATUS = "Status"

