import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPicture(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPicture")

	@staticmethod
	def ClassId():
		return "equipmentPicture"

	DN = "Dn"
	FILE_NAME = "FileName"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_BACK = "back"
	CONST_TYPE_BOTTOM = "bottom"
	CONST_TYPE_FRONT = "front"
	CONST_TYPE_LEFT = "left"
	CONST_TYPE_RIGHT = "right"
	CONST_TYPE_TOP = "top"
	CONST_TYPE_UNKNOWN = "unknown"
