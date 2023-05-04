import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtControllerFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtControllerFsmStage")

	@staticmethod
	def ClassId():
		return "mgmtControllerFsmStage"

	DESCR = "Descr"
	DN = "Dn"
	LAST_UPDATE_TIME = "LastUpdateTime"
	NAME = "Name"
	ORDER = "Order"
	RETRY = "Retry"
	RN = "Rn"
	STAGE_STATUS = "StageStatus"
	STATUS = "Status"

	CONST_LAST_UPDATE_TIME_ = ""
	CONST_NAME_ACTIVATE_BMCACTIVATE = "ActivateBMCActivate"
	CONST_NAME_ACTIVATE_BMCBEGIN = "ActivateBMCBegin"
	CONST_NAME_ACTIVATE_BMCFAIL = "ActivateBMCFail"
	CONST_NAME_ACTIVATE_BMCRESET = "ActivateBMCReset"
	CONST_NAME_ACTIVATE_BMCSUCCESS = "ActivateBMCSuccess"
	CONST_NAME_ACTIVATE_IOMACTIVATE = "ActivateIOMActivate"
	CONST_NAME_ACTIVATE_IOMBEGIN = "ActivateIOMBegin"
	CONST_NAME_ACTIVATE_IOMFAIL = "ActivateIOMFail"
	CONST_NAME_ACTIVATE_IOMRESET = "ActivateIOMReset"
	CONST_NAME_ACTIVATE_IOMSUCCESS = "ActivateIOMSuccess"
	CONST_NAME_EXT_MGMT_IF_CONFIG_BEGIN = "ExtMgmtIfConfigBegin"
	CONST_NAME_EXT_MGMT_IF_CONFIG_FAIL = "ExtMgmtIfConfigFail"
	CONST_NAME_EXT_MGMT_IF_CONFIG_PRIMARY = "ExtMgmtIfConfigPrimary"
	CONST_NAME_EXT_MGMT_IF_CONFIG_SECONDARY = "ExtMgmtIfConfigSecondary"
	CONST_NAME_EXT_MGMT_IF_CONFIG_SUCCESS = "ExtMgmtIfConfigSuccess"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_ACTIVE = "ExtMgmtInterfaceConfigActive"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_BEGIN = "ExtMgmtInterfaceConfigBegin"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_CIMCVLAN_CFG_LOCAL = "ExtMgmtInterfaceConfigCIMCVlanCfgLocal"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_CIMCVLAN_CFG_PEER = "ExtMgmtInterfaceConfigCIMCVlanCfgPeer"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_CMCVLAN_CFG = "ExtMgmtInterfaceConfigCMCVlanCfg"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_CMCVLAN_CFG_PEER = "ExtMgmtInterfaceConfigCMCVlanCfgPeer"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_FAIL = "ExtMgmtInterfaceConfigFail"
	CONST_NAME_EXT_MGMT_INTERFACE_CONFIG_SUCCESS = "ExtMgmtInterfaceConfigSuccess"
	CONST_NAME_ONLINE_BEGIN = "OnlineBegin"
	CONST_NAME_ONLINE_BMC_CONFIGURE_CONN_LOCAL = "OnlineBmcConfigureConnLocal"
	CONST_NAME_ONLINE_BMC_CONFIGURE_CONN_PEER = "OnlineBmcConfigureConnPeer"
	CONST_NAME_ONLINE_FAIL = "OnlineFail"
	CONST_NAME_ONLINE_SUCCESS = "OnlineSuccess"
	CONST_NAME_ONLINE_SW_CONFIGURE_CONN_LOCAL = "OnlineSwConfigureConnLocal"
	CONST_NAME_ONLINE_SW_CONFIGURE_CONN_PEER = "OnlineSwConfigureConnPeer"
	CONST_NAME_REGISTRY_CONFIG_BEGIN = "RegistryConfigBegin"
	CONST_NAME_REGISTRY_CONFIG_FAIL = "RegistryConfigFail"
	CONST_NAME_REGISTRY_CONFIG_REMOVE = "RegistryConfigRemove"
	CONST_NAME_REGISTRY_CONFIG_SUCCESS = "RegistryConfigSuccess"
	CONST_NAME_SYS_CONFIG_BEGIN = "SysConfigBegin"
	CONST_NAME_SYS_CONFIG_FAIL = "SysConfigFail"
	CONST_NAME_SYS_CONFIG_PRIMARY = "SysConfigPrimary"
	CONST_NAME_SYS_CONFIG_SECONDARY = "SysConfigSecondary"
	CONST_NAME_SYS_CONFIG_SUCCESS = "SysConfigSuccess"
	CONST_NAME_UPDATE_BMCBEGIN = "UpdateBMCBegin"
	CONST_NAME_UPDATE_BMCFAIL = "UpdateBMCFail"
	CONST_NAME_UPDATE_BMCPOLL_UPDATE_STATUS = "UpdateBMCPollUpdateStatus"
	CONST_NAME_UPDATE_BMCSUCCESS = "UpdateBMCSuccess"
	CONST_NAME_UPDATE_BMCUPDATE_REQUEST = "UpdateBMCUpdateRequest"
	CONST_NAME_UPDATE_IOMBEGIN = "UpdateIOMBegin"
	CONST_NAME_UPDATE_IOMCOPY_IOMIMG_TO_SUB = "UpdateIOMCopyIOMImgToSub"
	CONST_NAME_UPDATE_IOMCOPY_IMG_FROM_REP = "UpdateIOMCopyImgFromRep"
	CONST_NAME_UPDATE_IOMFAIL = "UpdateIOMFail"
	CONST_NAME_UPDATE_IOMPOLL_UPDATE_STATUS = "UpdateIOMPollUpdateStatus"
	CONST_NAME_UPDATE_IOMSUCCESS = "UpdateIOMSuccess"
	CONST_NAME_UPDATE_IOMUPDATE_REQUEST = "UpdateIOMUpdateRequest"
	CONST_NAME_UPDATE_SWITCH_BEGIN = "UpdateSwitchBegin"
	CONST_NAME_UPDATE_SWITCH_COPY_TO_LOCAL = "UpdateSwitchCopyToLocal"
	CONST_NAME_UPDATE_SWITCH_COPY_TO_PEER = "UpdateSwitchCopyToPeer"
	CONST_NAME_UPDATE_SWITCH_FAIL = "UpdateSwitchFail"
	CONST_NAME_UPDATE_SWITCH_RESET_LOCAL = "UpdateSwitchResetLocal"
	CONST_NAME_UPDATE_SWITCH_RESET_REMOTE = "UpdateSwitchResetRemote"
	CONST_NAME_UPDATE_SWITCH_SUCCESS = "UpdateSwitchSuccess"
	CONST_NAME_UPDATE_SWITCH_UPDATE_LOCAL = "UpdateSwitchUpdateLocal"
	CONST_NAME_UPDATE_SWITCH_UPDATE_REMOTE = "UpdateSwitchUpdateRemote"
	CONST_NAME_UPDATE_SWITCH_VERIFY_LOCAL = "UpdateSwitchVerifyLocal"
	CONST_NAME_UPDATE_SWITCH_VERIFY_REMOTE = "UpdateSwitchVerifyRemote"
	CONST_NAME_UPDATE_UCSMANAGER_BEGIN = "UpdateUCSManagerBegin"
	CONST_NAME_UPDATE_UCSMANAGER_COPY_EXT_TO_LOCAL = "UpdateUCSManagerCopyExtToLocal"
	CONST_NAME_UPDATE_UCSMANAGER_COPY_EXT_TO_PEER = "UpdateUCSManagerCopyExtToPeer"
	CONST_NAME_UPDATE_UCSMANAGER_EXECUTE = "UpdateUCSManagerExecute"
	CONST_NAME_UPDATE_UCSMANAGER_FAIL = "UpdateUCSManagerFail"
	CONST_NAME_UPDATE_UCSMANAGER_START = "UpdateUCSManagerStart"
	CONST_NAME_UPDATE_UCSMANAGER_SUCCESS = "UpdateUCSManagerSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"