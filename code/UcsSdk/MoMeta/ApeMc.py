import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeMc(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeMc")

	@staticmethod
	def ClassId():
		return "apeMc"

	DN = "Dn"
	IP = "Ip"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	UPDATE_TYPE = "UpdateType"

	CONST_UPDATE_TYPE_DELTA = "delta"
	CONST_UPDATE_TYPE_PERIODIC = "periodic"
	CONST_UPDATE_TYPE_SYNC = "sync"
