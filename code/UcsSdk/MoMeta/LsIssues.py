import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsIssues(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsIssues")

	@staticmethod
	def ClassId():
		return "lsIssues"

	CONFIG_WARNINGS = "ConfigWarnings"
	DN = "Dn"
	ISCSI_CONFIG_ISSUES = "IscsiConfigIssues"
	NETWORK_CONFIG_ISSUES = "NetworkConfigIssues"
	RN = "Rn"
	SERVER_CONFIG_ISSUES = "ServerConfigIssues"
	STATUS = "Status"
	STORAGE_CONFIG_ISSUES = "StorageConfigIssues"
	VNIC_CONFIG_ISSUES = "VnicConfigIssues"

