import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ConfigManagedEpImpactResponse(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ConfigManagedEpImpactResponse")

	@staticmethod
	def ClassId():
		return "configManagedEpImpactResponse"

	AFFECTED_SERVERS = "AffectedServers"
	APP_CONNECTOR_ID = "AppConnectorId"
	DN = "Dn"
	EP_NAME = "EpName"
	IMPACT_ANALYZER_ID = "ImpactAnalyzerId"
	REBOOT_REQUIRED = "RebootRequired"
	RN = "Rn"
	SOURCE_CONNECTOR_ID = "SourceConnectorId"
	STATE = "State"
	STATUS = "Status"

	CONST_REBOOT_REQUIRED_FALSE = "false"
	CONST_REBOOT_REQUIRED_NO = "no"
	CONST_REBOOT_REQUIRED_TRUE = "true"
	CONST_REBOOT_REQUIRED_YES = "yes"
	CONST_STATE_COMPLETE = "complete"
	CONST_STATE_NOT_STARTED = "not-started"
	CONST_STATE_WAITING = "waiting"
