import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootLanImagePath(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootLanImagePath")

	@staticmethod
	def ClassId():
		return "lsbootLanImagePath"

	BOOT_IP_POLICY_NAME = "BootIpPolicyName"
	DN = "Dn"
	I_SCSIVNIC_NAME = "ISCSIVnicName"
	IMG_POLICY_NAME = "ImgPolicyName"
	IMG_SEC_POLICY_NAME = "ImgSecPolicyName"
	PROV_SRV_POLICY_NAME = "ProvSrvPolicyName"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VNIC_NAME = "VnicName"

	CONST_TYPE_PRIMARY = "primary"
	CONST_TYPE_SECONDARY = "secondary"
