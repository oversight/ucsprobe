import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosSettingRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosSettingRef")

	@staticmethod
	def ClassId():
		return "biosSettingRef"

	CONSTANT_NAME = "ConstantName"
	DN = "Dn"
	IS_DEFAULT = "IsDefault"
	IS_SUPPORTED = "IsSupported"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_DEFAULT_NO = "no"
	CONST_IS_DEFAULT_YES = "yes"
	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_YES = "yes"
