import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageFcTargetEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageFcTargetEp")

	@staticmethod
	def ClassId():
		return "storageFcTargetEp"

	DESCR = "Descr"
	DN = "Dn"
	PATH = "Path"
	RN = "Rn"
	STATUS = "Status"
	TARGETWWPN = "Targetwwpn"

	CONST_PATH_A = "A"
	CONST_PATH_B = "B"
	CONST_PATH_NONE = "NONE"
	CONST_PATH_DUAL = "dual"
