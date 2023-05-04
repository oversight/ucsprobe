import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicProfileAlias(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicProfileAlias")

	@staticmethod
	def ClassId():
		return "vnicProfileAlias"

	ALIAS = "Alias"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	SW_UUID = "SwUuid"

