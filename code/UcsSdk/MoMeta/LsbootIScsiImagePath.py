import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootIScsiImagePath(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootIScsiImagePath")

	@staticmethod
	def ClassId():
		return "lsbootIScsiImagePath"

	DN = "Dn"
	I_SCSIVNIC_NAME = "ISCSIVnicName"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VNIC_NAME = "VnicName"

	CONST_TYPE_PRIMARY = "primary"
	CONST_TYPE_SECONDARY = "secondary"
