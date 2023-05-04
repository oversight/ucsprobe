import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootSanImagePath(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootSanImagePath")

	@staticmethod
	def ClassId():
		return "lsbootSanImagePath"

	DN = "Dn"
	LUN = "Lun"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VNIC_NAME = "VnicName"
	WWN = "Wwn"

	CONST_TYPE_PRIMARY = "primary"
	CONST_TYPE_SECONDARY = "secondary"
