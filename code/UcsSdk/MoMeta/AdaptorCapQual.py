import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorCapQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorCapQual")

	@staticmethod
	def ClassId():
		return "adaptorCapQual"

	DN = "Dn"
	FW_VERSION_HI = "FwVersionHi"
	FW_VERSION_LO = "FwVersionLo"
	FW_VERSION_OPR = "FwVersionOpr"
	MAXIMUM = "Maximum"
	MODEL = "Model"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_FW_VERSION_OPR_GT = "gt"
	CONST_FW_VERSION_OPR_LT = "lt"
	CONST_FW_VERSION_OPR_NONE = "none"
	CONST_FW_VERSION_OPR_RANGE = "range"
	CONST_MAXIMUM_UNSPECIFIED = "unspecified"
	CONST_TYPE_ETH_FLOW_MONITORING_NETFLOW = "eth-flow-monitoring-netflow"
	CONST_TYPE_FCOE = "fcoe"
	CONST_TYPE_NON_VIRTUALIZED_ETH_IF = "non-virtualized-eth-if"
	CONST_TYPE_NON_VIRTUALIZED_FC_IF = "non-virtualized-fc-if"
	CONST_TYPE_PATH_ENCAP_CONSOLIDATED = "path-encap-consolidated"
	CONST_TYPE_PATH_ENCAP_VIRTUAL = "path-encap-virtual"
	CONST_TYPE_PROTECTED_ETH_IF = "protected-eth-if"
	CONST_TYPE_PROTECTED_FC_IF = "protected-fc-if"
	CONST_TYPE_PROTECTED_FCOE = "protected-fcoe"
	CONST_TYPE_UPLINK_AGGREGATION = "uplink-aggregation"
	CONST_TYPE_VIRTUALIZED_ETH_IF = "virtualized-eth-if"
	CONST_TYPE_VIRTUALIZED_ETH_SRIOV = "virtualized-eth-sriov"
	CONST_TYPE_VIRTUALIZED_ETH_SRIOV_USNIC = "virtualized-eth-sriov-usnic"
	CONST_TYPE_VIRTUALIZED_ETH_VMQ = "virtualized-eth-vmq"
	CONST_TYPE_VIRTUALIZED_FC_IF = "virtualized-fc-if"
	CONST_TYPE_VIRTUALIZED_FC_SRIOV = "virtualized-fc-sriov"
	CONST_TYPE_VIRTUALIZED_SCSI_IF = "virtualized-scsi-if"
