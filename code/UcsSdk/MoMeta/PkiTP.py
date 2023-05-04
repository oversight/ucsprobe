import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PkiTP(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PkiTP")

	@staticmethod
	def ClassId():
		return "pkiTP"

	CERT_CHAIN = "CertChain"
	CERT_STATUS = "CertStatus"
	DESCR = "Descr"
	DN = "Dn"
	FP = "Fp"
	NAME = "Name"
	NUM_CERTS = "NumCerts"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_CERT_STATUS_CERT_CHAIN_TOO_LONG = "certChainTooLong"
	CONST_CERT_STATUS_EMPTY_CERT = "emptyCert"
	CONST_CERT_STATUS_EXPIRED = "expired"
	CONST_CERT_STATUS_FAILED_TO_VERIFY_WITH_PRIVATE_KEY = "failedToVerifyWithPrivateKey"
	CONST_CERT_STATUS_FAILED_TO_VERIFY_WITH_TP = "failedToVerifyWithTp"
	CONST_CERT_STATUS_NOT_YET_VALID = "notYetValid"
	CONST_CERT_STATUS_REVOKED = "revoked"
	CONST_CERT_STATUS_SELF_SIGNED_CERTIFICATE = "selfSignedCertificate"
	CONST_CERT_STATUS_UNKNOWN = "unknown"
	CONST_CERT_STATUS_VALID = "valid"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
