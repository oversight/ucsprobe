import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicWwpnHistory(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicWwpnHistory")

	@staticmethod
	def ClassId():
		return "vnicWwpnHistory"

	DN = "Dn"
	OLDADDR = "Oldaddr"
	RN = "Rn"
	STATUS = "Status"

