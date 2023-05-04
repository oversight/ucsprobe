import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerGroupQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerGroupQual")

	@staticmethod
	def ClassId():
		return "powerGroupQual"

	DN = "Dn"
	GROUP_NAME = "GroupName"
	RN = "Rn"
	STATUS = "Status"

