import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommDnsProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommDnsProvider")

	@staticmethod
	def ClassId():
		return "commDnsProvider"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	HOSTNAME = "Hostname"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
