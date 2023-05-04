import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicOProfileAlias(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicOProfileAlias")

	@staticmethod
	def ClassId():
		return "vnicOProfileAlias"

	ALIAS = "Alias"
	DN = "Dn"
	MGMT_PLANE = "MgmtPlane"
	RN = "Rn"
	STATUS = "Status"
	V_SWITCH_ID = "VSwitchId"
	V_SWITCH_NAME = "VSwitchName"

	CONST_MGMT_PLANE_RHEV_M = "rhev-m"
	CONST_MGMT_PLANE_SCVMM = "scvmm"
	CONST_MGMT_PLANE_UNMANAGED = "unmanaged"
	CONST_MGMT_PLANE_VCENTER = "vcenter"
