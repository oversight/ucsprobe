import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosUnit(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosUnit")

	@staticmethod
	def ClassId():
		return "biosUnit"

	DN = "Dn"
	INIT_SEQ = "InitSeq"
	INIT_TS = "InitTs"
	MODEL = "Model"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	VENDOR = "Vendor"

	CONST_INIT_TS_NEVER = "never"
