import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PkiKeyRing(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PkiKeyRing")

	@staticmethod
	def ClassId():
		return "pkiKeyRing"

	ADMIN_STATE = "AdminState"
	CERT = "Cert"
	CERT_STATUS = "CertStatus"
	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DESCR = "Descr"
	DN = "Dn"
	KEY = "Key"
	MODULUS = "Modulus"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REGEN = "Regen"
	RN = "Rn"
	STATUS = "Status"
	TP = "Tp"

	CONST_ADMIN_STATE_COMPLETED = "completed"
	CONST_ADMIN_STATE_CREATED = "created"
	CONST_ADMIN_STATE_REQ_CREATED = "reqCreated"
	CONST_ADMIN_STATE_STARTED = "started"
	CONST_ADMIN_STATE_TP_SET = "tpSet"
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
	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
	CONST_INT_ID_NONE = "none"
	CONST_MODULUS_MOD1024 = "mod1024"
	CONST_MODULUS_MOD1536 = "mod1536"
	CONST_MODULUS_MOD2048 = "mod2048"
	CONST_MODULUS_MOD2560 = "mod2560"
	CONST_MODULUS_MOD3072 = "mod3072"
	CONST_MODULUS_MOD3584 = "mod3584"
	CONST_MODULUS_MOD4096 = "mod4096"
	CONST_MODULUS_MOD512 = "mod512"
	CONST_MODULUS_MODINVALID = "modinvalid"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REGEN_FALSE = "false"
	CONST_REGEN_NO = "no"
	CONST_REGEN_TRUE = "true"
	CONST_REGEN_YES = "yes"
