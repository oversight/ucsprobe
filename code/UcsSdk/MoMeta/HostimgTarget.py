import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class HostimgTarget(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"HostimgTarget")

	@staticmethod
	def ClassId():
		return "hostimgTarget"

	DN = "Dn"
	NAME = "Name"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	URI = "Uri"

	CONST_ORDER_UNSPECIFIED = "unspecified"
	CONST_TYPE_COMPLETE = "complete"
	CONST_TYPE_FILE_SYSTEM = "file-system"
	CONST_TYPE_GPXE_SCRIPT = "gpxe-script"
	CONST_TYPE_KERNEL = "kernel"
	CONST_TYPE_MODULE = "module"
