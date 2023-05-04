import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePlatform(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePlatform")

	@staticmethod
	def ClassId():
		return "computePlatform"

	DN = "Dn"
	MODEL = "Model"
	PRODUCT_NAME = "ProductName"
	REVISION = "Revision"
	RN = "Rn"
	STATUS = "Status"
	VENDOR = "Vendor"

