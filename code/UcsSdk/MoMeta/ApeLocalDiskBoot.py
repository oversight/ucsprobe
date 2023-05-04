import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeLocalDiskBoot(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeLocalDiskBoot")

	@staticmethod
	def ClassId():
		return "apeLocalDiskBoot"

	CHASSIS_ID = "ChassisId"
	DN = "Dn"
	HOSTNAME = "Hostname"
	IS_HOST_AGENT_PRESENT = "IsHostAgentPresent"
	KERNEL_NAME = "KernelName"
	KERNEL_RELEASE = "KernelRelease"
	KERNEL_VERSION = "KernelVersion"
	NAME = "Name"
	RN = "Rn"
	SLOT_ID = "SlotId"
	STATUS = "Status"
	TARGET_LUN = "TargetLun"
	TYPE = "Type"

	CONST_CHASSIS_ID_N_A = "N/A"
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
