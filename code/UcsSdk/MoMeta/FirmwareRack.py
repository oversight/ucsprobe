import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareRack(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareRack")

	@staticmethod
	def ClassId():
		return "firmwareRack"

	DN = "Dn"
	OPER_VERSION = "OperVersion"
	RN = "Rn"
	STATUS = "Status"

