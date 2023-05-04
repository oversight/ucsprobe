import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EventLog(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EventLog")

	@staticmethod
	def ClassId():
		return "eventLog"

	DN = "Dn"
	MAX_SIZE = "MaxSize"
	PURGE_WINDOW = "PurgeWindow"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"

