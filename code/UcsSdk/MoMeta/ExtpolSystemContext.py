import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtpolSystemContext(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtpolSystemContext")

	@staticmethod
	def ClassId():
		return "extpolSystemContext"

	CAPABILITY = "Capability"
	DESCR = "Descr"
	DN = "Dn"
	GUID = "Guid"
	ID = "Id"
	INTEREST = "Interest"
	IP = "Ip"
	IPV6ADDR = "Ipv6addr"
	NAME = "Name"
	OWNER = "Owner"
	RN = "Rn"
	SITE = "Site"
	STATUS = "Status"
	TYPE = "Type"
	VERSION = "Version"

	CONST_TYPE_APE = "ape"
	CONST_TYPE_BOOT_MGR = "boot-mgr"
	CONST_TYPE_IDENTIFIER_MGR = "identifier-mgr"
	CONST_TYPE_MANAGED_ENDPOINT = "managed-endpoint"
	CONST_TYPE_MGMT_CONTROLLER = "mgmt-controller"
	CONST_TYPE_OPERATION_MGR = "operation-mgr"
	CONST_TYPE_POLICY_MGR = "policy-mgr"
	CONST_TYPE_RESOURCE_AGGR = "resource-aggr"
	CONST_TYPE_RESOURCE_MGR = "resource-mgr"
	CONST_TYPE_SERVICE_REG = "service-reg"
	CONST_TYPE_STATS_MGR = "stats-mgr"
	CONST_TYPE_STORAGE_BROKER = "storage-broker"
	CONST_TYPE_VIRTUAL_SWITCHING_MGR = "virtual-switching-mgr"
	CONST_TYPE_VM_MGR = "vm-mgr"
