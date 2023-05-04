import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfPackageCStateLimit(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfPackageCStateLimit")

	@staticmethod
	def ClassId():
		return "biosVfPackageCStateLimit"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PACKAGE_CSTATE_LIMIT = "VpPackageCStateLimit"

	CONST_VP_PACKAGE_CSTATE_LIMIT_C0 = "c0"
	CONST_VP_PACKAGE_CSTATE_LIMIT_C1 = "c1"
	CONST_VP_PACKAGE_CSTATE_LIMIT_C3 = "c3"
	CONST_VP_PACKAGE_CSTATE_LIMIT_C6 = "c6"
	CONST_VP_PACKAGE_CSTATE_LIMIT_NO_LIMIT = "no-limit"
	CONST_VP_PACKAGE_CSTATE_LIMIT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PACKAGE_CSTATE_LIMIT_PLATFORM_RECOMMENDED = "platform-recommended"
