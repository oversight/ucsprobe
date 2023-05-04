import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CapabilityUpdate(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CapabilityUpdate")

	@staticmethod
	def ClassId():
		return "capabilityUpdate"

	DN = "Dn"
	IMAGE_NAME = "ImageName"
	RN = "Rn"
	STATUS = "Status"
	UPDATE_TS = "UpdateTs"
	VERSION = "Version"

