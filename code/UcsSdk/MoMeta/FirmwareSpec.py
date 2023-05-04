import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareSpec(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareSpec")

	@staticmethod
	def ClassId():
		return "firmwareSpec"

	BUNDLE_VERSION = "BundleVersion"
	DN = "Dn"
	ETH_EFIVERSION = "EthEFIVersion"
	ETH_OPTION_ROM_VERSION = "EthOptionRomVersion"
	FC_FWVERSION = "FcFWVersion"
	FC_OPTION_ROM_VERSION = "FcOptionRomVersion"
	RN = "Rn"
	STATUS = "Status"

