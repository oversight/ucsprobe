import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfLocalX2Apic(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfLocalX2Apic")

	@staticmethod
	def ClassId():
		return "biosVfLocalX2Apic"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_LOCAL_X2_APIC = "VpLocalX2Apic"

	CONST_VP_LOCAL_X2_APIC_AUTO = "auto"
	CONST_VP_LOCAL_X2_APIC_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LOCAL_X2_APIC_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_LOCAL_X2_APIC_X2APIC = "x2apic"
	CONST_VP_LOCAL_X2_APIC_XAPIC = "xapic"
