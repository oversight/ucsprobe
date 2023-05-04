import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaLdapProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaLdapProvider")

	@staticmethod
	def ClassId():
		return "aaaLdapProvider"

	ATTRIBUTE = "Attribute"
	BASEDN = "Basedn"
	DESCR = "Descr"
	DN = "Dn"
	ENABLE_SSL = "EnableSSL"
	ENC_KEY = "EncKey"
	FILTER = "Filter"
	KEY = "Key"
	KEY_SET = "KeySet"
	NAME = "Name"
	ORDER = "Order"
	PORT = "Port"
	RETRIES = "Retries"
	RN = "Rn"
	ROOTDN = "Rootdn"
	STATUS = "Status"
	TIMEOUT = "Timeout"
	VENDOR = "Vendor"

	CONST_ENABLE_SSL_FALSE = "false"
	CONST_ENABLE_SSL_NO = "no"
	CONST_ENABLE_SSL_TRUE = "true"
	CONST_ENABLE_SSL_YES = "yes"
	CONST_KEY_SET_FALSE = "false"
	CONST_KEY_SET_NO = "no"
	CONST_KEY_SET_TRUE = "true"
	CONST_KEY_SET_YES = "yes"
	CONST_ORDER_LOWEST_AVAILABLE = "lowest-available"
	CONST_VENDOR_MS_AD = "MS-AD"
	CONST_VENDOR_OPEN_LDAP = "OpenLdap"
