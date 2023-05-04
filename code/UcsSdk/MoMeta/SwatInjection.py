import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwatInjection(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwatInjection")

	@staticmethod
	def ClassId():
		return "swatInjection"

	DN = "Dn"
	MODEL = "Model"
	NAME = "Name"
	POOL_DN = "PoolDn"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	VENDOR = "Vendor"

