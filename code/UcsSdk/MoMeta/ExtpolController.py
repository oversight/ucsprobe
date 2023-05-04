import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtpolController(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtpolController")

	@staticmethod
	def ClassId():
		return "extpolController"

	CAPABILITY = "Capability"
	CONN_PROTOCOL = "ConnProtocol"
	DN = "Dn"
	HOST = "Host"
	ID = "Id"
	INTEREST = "Interest"
	IP = "Ip"
	IPV6 = "Ipv6"
	LAST_POLL_TS = "LastPollTs"
	NAME = "Name"
	OPER_STATE = "OperState"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VERSION = "Version"

	CONST_CONN_PROTOCOL_IPV4 = "ipv4"
	CONST_CONN_PROTOCOL_IPV6 = "ipv6"
	CONST_CONN_PROTOCOL_UNKNOWN = "unknown"
	CONST_OPER_STATE_LOST_VISIBILITY = "lost-visibility"
	CONST_OPER_STATE_REGISTERED = "registered"
	CONST_OPER_STATE_REGISTERING = "registering"
	CONST_OPER_STATE_REGISTRY_NOT_REACHABLE = "registry-not-reachable"
	CONST_OPER_STATE_SYNCHRONIZING = "synchronizing"
	CONST_OPER_STATE_UNREGISTERED = "unregistered"
	CONST_OPER_STATE_VERSION_MISMATCH = "version-mismatch"
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
