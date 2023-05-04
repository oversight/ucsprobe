import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFamilyTypeDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFamilyTypeDef")

	@staticmethod
	def ClassId():
		return "adaptorFamilyTypeDef"

	DN = "Dn"
	IS_PASSTHROUGH = "IsPassthrough"
	NUM_DCE_PORTS = "NumDcePorts"
	PORT_FAMILY = "PortFamily"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_IS_PASSTHROUGH_FALSE = "false"
	CONST_IS_PASSTHROUGH_NO = "no"
	CONST_IS_PASSTHROUGH_TRUE = "true"
	CONST_IS_PASSTHROUGH_YES = "yes"
