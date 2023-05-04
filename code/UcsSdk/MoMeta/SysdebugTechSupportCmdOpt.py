import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugTechSupportCmdOpt(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugTechSupportCmdOpt")

	@staticmethod
	def ClassId():
		return "sysdebugTechSupportCmdOpt"

	CHASSIS_CIMC_ID = "ChassisCimcId"
	CHASSIS_ID = "ChassisId"
	CHASSIS_IOM_ID = "ChassisIomId"
	CIMC_ADAPTER_ID = "CimcAdapterId"
	DN = "Dn"
	FAB_EXT_ID = "FabExtId"
	MAJOR_OPT_TYPE = "MajorOptType"
	RACK_SERVER_ADAPTER_ID = "RackServerAdapterId"
	RACK_SERVER_ID = "RackServerId"
	RN = "Rn"
	STATUS = "Status"

	CONST_CHASSIS_CIMC_ID_ALL = "all"
	CONST_CHASSIS_IOM_ID_ALL = "all"
	CONST_CIMC_ADAPTER_ID_ALL = "all"
	CONST_MAJOR_OPT_TYPE_CHASSIS = "chassis"
	CONST_MAJOR_OPT_TYPE_FEX = "fex"
	CONST_MAJOR_OPT_TYPE_SERVER = "server"
	CONST_MAJOR_OPT_TYPE_UCSM = "ucsm"
	CONST_MAJOR_OPT_TYPE_UCSM_MGMT = "ucsm-mgmt"
	CONST_RACK_SERVER_ADAPTER_ID_ALL = "all"
