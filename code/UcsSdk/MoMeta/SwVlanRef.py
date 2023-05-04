import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwVlanRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwVlanRef")

	@staticmethod
	def ClassId():
		return "swVlanRef"

	COMPRESSION_TYPE = "CompressionType"
	CONFIG_STATUS = "ConfigStatus"
	DN = "Dn"
	ID = "Id"
	PEER_DN = "PeerDn"
	RN = "Rn"
	STATUS = "Status"

	CONST_COMPRESSION_TYPE_EXCLUDED = "excluded"
	CONST_COMPRESSION_TYPE_INCLUDED = "included"
	CONST_CONFIG_STATUS_APPLIED = "applied"
	CONST_CONFIG_STATUS_UN_APPLIED = "unApplied"
