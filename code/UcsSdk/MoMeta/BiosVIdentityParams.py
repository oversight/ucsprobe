import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVIdentityParams(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVIdentityParams")

	@staticmethod
	def ClassId():
		return "biosVIdentityParams"

	DN = "Dn"
	LS_SERVER_NAME = "LsServerName"
	LS_SERVER_TMPL_NAME = "LsServerTmplName"
	RN = "Rn"
	STATUS = "Status"
	SYS_NAME = "SysName"

