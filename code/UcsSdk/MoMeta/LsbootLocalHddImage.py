import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootLocalHddImage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootLocalHddImage")

	@staticmethod
	def ClassId():
		return "lsbootLocalHddImage"

	DN = "Dn"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_LOCAL_ANY = "local-any"
	CONST_TYPE_LOCAL_LUN = "local-lun"
	CONST_TYPE_SD_CARD = "sd-card"
	CONST_TYPE_USB_EXTERN = "usb-extern"
	CONST_TYPE_USB_INTERN = "usb-intern"
