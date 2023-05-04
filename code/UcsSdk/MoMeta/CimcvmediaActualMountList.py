import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CimcvmediaActualMountList(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CimcvmediaActualMountList")

	@staticmethod
	def ClassId():
		return "cimcvmediaActualMountList"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

