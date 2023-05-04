import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class HostimgPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"HostimgPolicy")

	@staticmethod
	def ClassId():
		return "hostimgPolicy"

	COMP = "Comp"
	CONF = "Conf"
	DESCR = "Descr"
	DISTRO = "Distro"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_COMP_COMPLETE = "complete"
	CONST_COMP_COMPONENTIZED = "componentized"
	CONST_DISTRO_FEDORA = "fedora"
	CONST_DISTRO_UNKNOWN = "unknown"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TYPE_ESXI = "esxi"
	CONST_TYPE_GPXE_SCRIPT = "gpxe-script"
	CONST_TYPE_KVM = "kvm"
	CONST_TYPE_LINUX = "linux"
	CONST_TYPE_UNKNOWN = "unknown"
	CONST_TYPE_WINDOWS = "windows"
	CONST_TYPE_XEN = "xen"
