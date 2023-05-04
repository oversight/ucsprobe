import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootSanImage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootSanImage")

	@staticmethod
	def ClassId():
		return "lsbootSanImage"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VNIC_NAME = "VnicName"

	CONST_TYPE_PRIMARY = "primary"
	CONST_TYPE_SECONDARY = "secondary"
