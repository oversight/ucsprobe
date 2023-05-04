import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsServerAssocCtx(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsServerAssocCtx")

	@staticmethod
	def ClassId():
		return "lsServerAssocCtx"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

