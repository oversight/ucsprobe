import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PkiCertReq(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PkiCertReq")

	@staticmethod
	def ClassId():
		return "pkiCertReq"

	COUNTRY = "Country"
	DN = "Dn"
	DNS = "Dns"
	EMAIL = "Email"
	IP = "Ip"
	IP_A = "IpA"
	IP_B = "IpB"
	IPV6 = "Ipv6"
	IPV6_A = "Ipv6A"
	IPV6_B = "Ipv6B"
	LOCALITY = "Locality"
	ORG_NAME = "OrgName"
	ORG_UNIT_NAME = "OrgUnitName"
	PWD = "Pwd"
	REQ = "Req"
	RN = "Rn"
	STATE = "State"
	STATUS = "Status"
	SUBJ_NAME = "SubjName"

