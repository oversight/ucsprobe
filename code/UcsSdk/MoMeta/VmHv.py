import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmHv(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmHv")

	@staticmethod
	def ClassId():
		return "vmHv"

	CL_INST_TYPE = "ClInstType"
	DESCR = "Descr"
	DN = "Dn"
	DVS_DN = "DvsDn"
	DVS_NAME = "DvsName"
	HV_TYPE = "HvType"
	LS_DN = "LsDn"
	MODEL = "Model"
	NAME = "Name"
	PN_DN = "PnDn"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	STATUS_CHANGE_TS = "StatusChangeTs"
	UUID = "Uuid"
	V_STATUS = "VStatus"
	VENDOR = "Vendor"

	CONST_CL_INST_TYPE_COMPUTE_EP = "compute-ep"
	CONST_CL_INST_TYPE_HV = "hv"
	CONST_CL_INST_TYPE_VM = "vm"
	CONST_HV_TYPE_ESX = "esx"
	CONST_HV_TYPE_HYPERV = "hyperv"
	CONST_HV_TYPE_KVM = "kvm"
	CONST_HV_TYPE_UNSPECIFIED = "unspecified"
	CONST_HV_TYPE_XEN = "xen"
	CONST_INT_ID_NONE = "none"
	CONST_MODEL_LINUX = "Linux"
	CONST_MODEL_PNU_OS = "PnuOS"
	CONST_MODEL_SOLARIS = "Solaris"
	CONST_MODEL_VMWARE_ESX = "VMWareESX"
	CONST_MODEL_WINDOWS = "Windows"
	CONST_MODEL_UNSPECIFIED = "unspecified"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_V_STATUS_OFFLINE = "offline"
	CONST_V_STATUS_ONLINE = "online"
	CONST_V_STATUS_UNKNOWN = "unknown"
	CONST_VENDOR_CITRIX = "citrix"
	CONST_VENDOR_MICROSOFT = "microsoft"
	CONST_VENDOR_NOVELL = "novell"
	CONST_VENDOR_ORACLE = "oracle"
	CONST_VENDOR_REDHAT = "redhat"
	CONST_VENDOR_UNSPECIFIED = "unspecified"
	CONST_VENDOR_VMWARE = "vmware"
