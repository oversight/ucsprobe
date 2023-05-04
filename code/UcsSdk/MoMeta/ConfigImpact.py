import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ConfigImpact(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ConfigImpact")

	@staticmethod
	def ClassId():
		return "configImpact"

	AFFECTED_OBJ = "AffectedObj"
	AFFECTED_SERVER = "AffectedServer"
	CHANGES = "Changes"
	CONFIG_ISSUES = "ConfigIssues"
	CONFIG_QUALIFIER = "ConfigQualifier"
	CONFIG_STATE = "ConfigState"
	DEPLOYMENT_MODE = "DeploymentMode"
	DN = "Dn"
	NAME = "Name"
	REBOOT_REQUIRED = "RebootRequired"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIG_STATE_APPLIED = "applied"
	CONST_CONFIG_STATE_APPLYING = "applying"
	CONST_CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_DEPLOYMENT_MODE_IMMEDIATE = "immediate"
	CONST_DEPLOYMENT_MODE_TIMER_AUTOMATIC = "timer-automatic"
	CONST_DEPLOYMENT_MODE_USER_ACK = "user-ack"
	CONST_REBOOT_REQUIRED_FALSE = "false"
	CONST_REBOOT_REQUIRED_NO = "no"
	CONST_REBOOT_REQUIRED_TRUE = "true"
	CONST_REBOOT_REQUIRED_YES = "yes"
