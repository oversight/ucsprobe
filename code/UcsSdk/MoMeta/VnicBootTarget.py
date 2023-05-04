import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicBootTarget(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicBootTarget")

	@staticmethod
	def ClassId():
		return "vnicBootTarget"

	DN = "Dn"
	LUN = "Lun"
	RN = "Rn"
	STATUS = "Status"
	WWN = "Wwn"

