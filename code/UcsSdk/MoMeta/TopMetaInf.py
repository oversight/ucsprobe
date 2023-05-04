import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TopMetaInf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"TopMetaInf")

	@staticmethod
	def ClassId():
		return "topMetaInf"

	DN = "Dn"
	ECODE = "Ecode"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

