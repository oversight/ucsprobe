import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeLANBoot(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeLANBoot")

	@staticmethod
	def ClassId():
		return "apeLANBoot"

	DN = "Dn"
	HOSTNAME = "Hostname"
	IS_HOST_AGENT_PRESENT = "IsHostAgentPresent"
	KERNEL_NAME = "KernelName"
	KERNEL_RELEASE = "KernelRelease"
	KERNEL_VERSION = "KernelVersion"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VNIC_NAME = "VnicName"

	CONST_IS_HOST_AGENT_PRESENT_FALSE = "false"
	CONST_IS_HOST_AGENT_PRESENT_NO = "no"
	CONST_IS_HOST_AGENT_PRESENT_TRUE = "true"
	CONST_IS_HOST_AGENT_PRESENT_YES = "yes"
	CONST_TYPE_LINUX = "Linux"
	CONST_TYPE_PNU_OS = "PnuOS"
	CONST_TYPE_SOLARIS = "Solaris"
	CONST_TYPE_VMWARE_ESX = "VMWareESX"
	CONST_TYPE_WINDOWS = "Windows"
	CONST_TYPE_UNSPECIFIED = "unspecified"
