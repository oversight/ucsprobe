import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareImageLock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareImageLock")

	@staticmethod
	def ClassId():
		return "firmwareImageLock"

	_IMAGE_NAME_DN = "ImageNameDn"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

