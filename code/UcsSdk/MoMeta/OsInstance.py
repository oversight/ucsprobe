import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class OsInstance(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"OsInstance")

	@staticmethod
	def ClassId():
		return "osInstance"

	DN = "Dn"
	HOSTNAME = "Hostname"
	KERNEL_NAME = "KernelName"
	KERNEL_RELEASE = "KernelRelease"
	KERNEL_VERSION = "KernelVersion"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_LINUX = "Linux"
	CONST_TYPE_PNU_OS = "PnuOS"
	CONST_TYPE_SOLARIS = "Solaris"
	CONST_TYPE_VMWARE_ESX = "VMWareESX"
	CONST_TYPE_WINDOWS = "Windows"
	CONST_TYPE_UNSPECIFIED = "unspecified"
