import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentDimmEntry(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentDimmEntry")

	@staticmethod
	def ClassId():
		return "equipmentDimmEntry"

	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	SMBIOSNAME = "Smbiosname"
	STATUS = "Status"

