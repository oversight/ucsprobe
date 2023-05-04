import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsServerExtension(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsServerExtension")

	@staticmethod
	def ClassId():
		return "lsServerExtension"

	DN = "Dn"
	GUID = "Guid"
	RN = "Rn"
	STATUS = "Status"
	VERSION = "Version"

