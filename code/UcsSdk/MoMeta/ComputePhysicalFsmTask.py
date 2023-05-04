import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePhysicalFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePhysicalFsmTask")

	@staticmethod
	def ClassId():
		return "computePhysicalFsmTask"

	COMPLETION = "Completion"
	DN = "Dn"
	FLAGS = "Flags"
	ITEM = "Item"
	RN = "Rn"
	SEQ_ID = "SeqId"
	STATUS = "Status"

	CONST_COMPLETION_CANCELLED = "cancelled"
	CONST_COMPLETION_COMPLETED = "completed"
	CONST_COMPLETION_PROCESSING = "processing"
	CONST_COMPLETION_SCHEDULED = "scheduled"
	CONST_ITEM_ACTIVATE_ADAPTOR = "ActivateAdaptor"
	CONST_ITEM_ACTIVATE_BIOS = "ActivateBIOS"
	CONST_ITEM_ASSOCIATE = "Associate"
	CONST_ITEM_BIOS_RECOVERY = "BiosRecovery"
	CONST_ITEM_CIMC_SESSION_DELETE = "CimcSessionDelete"
	CONST_ITEM_CMOS_RESET = "CmosReset"
	CONST_ITEM_CONFIG_BOARD = "ConfigBoard"
	CONST_ITEM_CONFIG_SO_L = "ConfigSoL"
	CONST_ITEM_DECOMMISSION = "Decommission"
	CONST_ITEM_DIAGNOSTIC_INTERRUPT = "DiagnosticInterrupt"
	CONST_ITEM_DISASSOCIATE = "Disassociate"
	CONST_ITEM_FLASH_CONTROLLER = "FlashController"
	CONST_ITEM_FW_UPGRADE = "FwUpgrade"
	CONST_ITEM_HARD_SHUTDOWN = "HardShutdown"
	CONST_ITEM_HARDRESET = "Hardreset"
	CONST_ITEM_POWER_CAP = "PowerCap"
	CONST_ITEM_POWERCYCLE = "Powercycle"
	CONST_ITEM_RESET_BMC = "ResetBmc"
	CONST_ITEM_RESET_IPMI = "ResetIpmi"
	CONST_ITEM_RESET_KVM = "ResetKvm"
	CONST_ITEM_RESET_MEMORY_ERRORS = "ResetMemoryErrors"
	CONST_ITEM_SERVICE_INFRA_DEPLOY = "ServiceInfraDeploy"
	CONST_ITEM_SERVICE_INFRA_WITHDRAW = "ServiceInfraWithdraw"
	CONST_ITEM_SOFT_SHUTDOWN = "SoftShutdown"
	CONST_ITEM_SOFTRESET = "Softreset"
	CONST_ITEM_SW_CONN_UPD = "SwConnUpd"
	CONST_ITEM_TURNUP = "Turnup"
	CONST_ITEM_UNCONFIG_SO_L = "UnconfigSoL"
	CONST_ITEM_UPDATE_ADAPTOR = "UpdateAdaptor"
	CONST_ITEM_UPDATE_BIOS = "UpdateBIOS"
	CONST_ITEM_UPDATE_BOARD_CONTROLLER = "UpdateBoardController"
	CONST_ITEM_NOP = "nop"
	CONST_ITEM_UPDATE_EXT_USERS = "updateExtUsers"
