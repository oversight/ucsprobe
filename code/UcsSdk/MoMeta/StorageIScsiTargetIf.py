import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageIScsiTargetIf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageIScsiTargetIf")

	@staticmethod
	def ClassId():
		return "storageIScsiTargetIf"

	DN = "Dn"
	NAME = "Name"
	PROT = "Prot"
	RN = "Rn"
	STATUS = "Status"

	CONST_PROT_DERIVED = "derived"
	CONST_PROT_FC = "fc"
	CONST_PROT_ISCSI = "iscsi"
