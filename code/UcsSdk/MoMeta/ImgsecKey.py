import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ImgsecKey(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ImgsecKey")

	@staticmethod
	def ClassId():
		return "imgsecKey"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	VALUE = "Value"

	CONST_TYPE_PRIVATE = "private"
	CONST_TYPE_PUBLIC = "public"
	CONST_TYPE_SHARED = "shared"
