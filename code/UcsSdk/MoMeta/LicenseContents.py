import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseContents(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseContents")

	@staticmethod
	def ClassId():
		return "licenseContents"

	DN = "Dn"
	FEATURE_NAME = "FeatureName"
	RN = "Rn"
	STATUS = "Status"
	TOTAL_QUANT = "TotalQuant"
	VENDOR = "Vendor"
	VERSION = "Version"

