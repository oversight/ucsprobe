import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CallhomeSmtp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CallhomeSmtp")

	@staticmethod
	def ClassId():
		return "callhomeSmtp"

	DN = "Dn"
	HOST = "Host"
	PORT = "Port"
	RN = "Rn"
	STATUS = "Status"

