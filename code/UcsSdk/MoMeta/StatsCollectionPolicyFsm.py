import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StatsCollectionPolicyFsm(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StatsCollectionPolicyFsm")

	@staticmethod
	def ClassId():
		return "statsCollectionPolicyFsm"

	COMPLETION_TIME = "CompletionTime"
	CURRENT_FSM = "CurrentFsm"
	DESCR = "Descr"
	DN = "Dn"
	INSTANCE_ID = "InstanceId"
	PROGRESS = "Progress"
	RMT_ERR_CODE = "RmtErrCode"
	RMT_ERR_DESCR = "RmtErrDescr"
	RMT_RSLT = "RmtRslt"
	RN = "Rn"
	STATUS = "Status"

	CONST_COMPLETION_TIME_ = ""
	CONST_CURRENT_FSM_NOP = "nop"
	CONST_CURRENT_FSM_UPDATE_EP = "updateEp"
	CONST_FSM_STATUS_FAIL = "fail"
	CONST_FSM_STATUS_IN_PROGRESS = "inProgress"
	CONST_FSM_STATUS_NOP = "nop"
	CONST_FSM_STATUS_PENDING = "pending"
	CONST_FSM_STATUS_SKIP = "skip"
	CONST_FSM_STATUS_SUCCESS = "success"
	CONST_FSM_STATUS_THROTTLED = "throttled"
	CONST_RMT_ERR_CODE_ERR_2FA_AUTH_RETRY = "ERR-2fa-auth-retry"
	CONST_RMT_ERR_CODE_ERR_ACTIVATE_FAILED = "ERR-ACTIVATE-failed"
	CONST_RMT_ERR_CODE_ERR_ACTIVATE_IN_PROGRESS = "ERR-ACTIVATE-in-progress"
	CONST_RMT_ERR_CODE_ERR_ACTIVATE_RETRY = "ERR-ACTIVATE-retry"
	CONST_RMT_ERR_CODE_ERR_BIOS_TOKENS_OLD_BIOS = "ERR-BIOS-TOKENS-OLD-BIOS"
	CONST_RMT_ERR_CODE_ERR_BIOS_TOKENS_OLD_CIMC = "ERR-BIOS-TOKENS-OLD-CIMC"
	CONST_RMT_ERR_CODE_ERR_BIOS_NETWORK_BOOT_ORDER_NOT_FOUND = "ERR-BIOS-network-boot-order-not-found"
	CONST_RMT_ERR_CODE_ERR_BOARDCTRLUPDATE_IGNORE = "ERR-BOARDCTRLUPDATE-ignore"
	CONST_RMT_ERR_CODE_ERR_DIAG_CANCELLED = "ERR-DIAG-cancelled"
	CONST_RMT_ERR_CODE_ERR_DIAG_FSM_RESTARTED = "ERR-DIAG-fsm-restarted"
	CONST_RMT_ERR_CODE_ERR_DIAG_TEST_FAILED = "ERR-DIAG-test-failed"
	CONST_RMT_ERR_CODE_ERR_DNLD_AUTHENTICATION_FAILURE = "ERR-DNLD-authentication-failure"
	CONST_RMT_ERR_CODE_ERR_DNLD_HOSTKEY_MISMATCH = "ERR-DNLD-hostkey-mismatch"
	CONST_RMT_ERR_CODE_ERR_DNLD_INVALID_IMAGE = "ERR-DNLD-invalid-image"
	CONST_RMT_ERR_CODE_ERR_DNLD_NO_FILE = "ERR-DNLD-no-file"
	CONST_RMT_ERR_CODE_ERR_DNLD_NO_SPACE = "ERR-DNLD-no-space"
	CONST_RMT_ERR_CODE_ERR_DNS_DELETE_ERROR = "ERR-DNS-delete-error"
	CONST_RMT_ERR_CODE_ERR_DNS_GET_ERROR = "ERR-DNS-get-error"
	CONST_RMT_ERR_CODE_ERR_DNS_SET_ERROR = "ERR-DNS-set-error"
	CONST_RMT_ERR_CODE_ERR_DIAGNOSTICS_IN_PROGRESS = "ERR-Diagnostics-in-progress"
	CONST_RMT_ERR_CODE_ERR_DIAGNOSTICS_MEMTEST_IN_PROGRESS = "ERR-Diagnostics-memtest-in-progress"
	CONST_RMT_ERR_CODE_ERR_DIAGNOSTICS_NETWORK_IN_PROGRESS = "ERR-Diagnostics-network-in-progress"
	CONST_RMT_ERR_CODE_ERR_FILTER_ILLEGAL_FORMAT = "ERR-FILTER-illegal-format"
	CONST_RMT_ERR_CODE_ERR_FSM_NO_SUCH_STATE = "ERR-FSM-no-such-state"
	CONST_RMT_ERR_CODE_ERR_HOST_FRU_IDENTITY_MISMATCH = "ERR-HOST-fru-identity-mismatch"
	CONST_RMT_ERR_CODE_ERR_HTTP_SET_ERROR = "ERR-HTTP-set-error"
	CONST_RMT_ERR_CODE_ERR_HTTPS_SET_ERROR = "ERR-HTTPS-set-error"
	CONST_RMT_ERR_CODE_ERR_IBMC_ANALYZE_RESULTS = "ERR-IBMC-analyze-results"
	CONST_RMT_ERR_CODE_ERR_IBMC_CONNECT_ERROR = "ERR-IBMC-connect-error"
	CONST_RMT_ERR_CODE_ERR_IBMC_CONNECTOR_INFO_RETRIEVAL_ERROR = "ERR-IBMC-connector-info-retrieval-error"
	CONST_RMT_ERR_CODE_ERR_IBMC_FRU_RETRIEVAL_ERROR = "ERR-IBMC-fru-retrieval-error"
	CONST_RMT_ERR_CODE_ERR_IBMC_INVALID_END_POINT_CONFIG = "ERR-IBMC-invalid-end-point-config"
	CONST_RMT_ERR_CODE_ERR_IBMC_RESULTS_NOT_READY = "ERR-IBMC-results-not-ready"
	CONST_RMT_ERR_CODE_ERR_MAX_SUBSCRIPTIONS_ALLOWED_ERROR = "ERR-MAX-subscriptions-allowed-error"
	CONST_RMT_ERR_CODE_ERR_MO_CONFIG_CHILD_OBJECT_CANT_BE_CONFIGURED = "ERR-MO-CONFIG-child-object-cant-be-configured"
	CONST_RMT_ERR_CODE_ERR_MO_META_NO_SUCH_OBJECT_CLASS = "ERR-MO-META-no-such-object-class"
	CONST_RMT_ERR_CODE_ERR_MO_PROPERTY_NO_SUCH_PROPERTY = "ERR-MO-PROPERTY-no-such-property"
	CONST_RMT_ERR_CODE_ERR_MO_PROPERTY_VALUE_OUT_OF_RANGE = "ERR-MO-PROPERTY-value-out-of-range"
	CONST_RMT_ERR_CODE_ERR_MO_ACCESS_DENIED = "ERR-MO-access-denied"
	CONST_RMT_ERR_CODE_ERR_MO_DELETION_RULE_VIOLATION = "ERR-MO-deletion-rule-violation"
	CONST_RMT_ERR_CODE_ERR_MO_DUPLICATE_OBJECT = "ERR-MO-duplicate-object"
	CONST_RMT_ERR_CODE_ERR_MO_ILLEGAL_CONTAINMENT = "ERR-MO-illegal-containment"
	CONST_RMT_ERR_CODE_ERR_MO_ILLEGAL_CREATION = "ERR-MO-illegal-creation"
	CONST_RMT_ERR_CODE_ERR_MO_ILLEGAL_ITERATOR_STATE = "ERR-MO-illegal-iterator-state"
	CONST_RMT_ERR_CODE_ERR_MO_ILLEGAL_OBJECT_LIFECYCLE_TRANSITION = "ERR-MO-illegal-object-lifecycle-transition"
	CONST_RMT_ERR_CODE_ERR_MO_NAMING_RULE_VIOLATION = "ERR-MO-naming-rule-violation"
	CONST_RMT_ERR_CODE_ERR_MO_OBJECT_NOT_FOUND = "ERR-MO-object-not-found"
	CONST_RMT_ERR_CODE_ERR_MO_RESOURCE_ALLOCATION = "ERR-MO-resource-allocation"
	CONST_RMT_ERR_CODE_ERR_NTP_DELETE_ERROR = "ERR-NTP-delete-error"
	CONST_RMT_ERR_CODE_ERR_NTP_GET_ERROR = "ERR-NTP-get-error"
	CONST_RMT_ERR_CODE_ERR_NTP_SET_ERROR = "ERR-NTP-set-error"
	CONST_RMT_ERR_CODE_ERR_POWER_CAP_UNSUPPORTED = "ERR-POWER-CAP-UNSUPPORTED"
	CONST_RMT_ERR_CODE_ERR_SERVER_MIS_CONNECT = "ERR-SERVER-mis-connect"
	CONST_RMT_ERR_CODE_ERR_SWITCH_INVALID_IF_CONFIG = "ERR-SWITCH-invalid-if-config"
	CONST_RMT_ERR_CODE_ERR_TOKEN_REQUEST_DENIED = "ERR-TOKEN-request-denied"
	CONST_RMT_ERR_CODE_ERR_UNABLE_TO_FETCH_BIOS_SETTINGS = "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS"
	CONST_RMT_ERR_CODE_ERR_UPDATE_FAILED = "ERR-UPDATE-failed"
	CONST_RMT_ERR_CODE_ERR_UPDATE_IN_PROGRESS = "ERR-UPDATE-in-progress"
	CONST_RMT_ERR_CODE_ERR_UPDATE_RETRY = "ERR-UPDATE-retry"
	CONST_RMT_ERR_CODE_ERR_AAA_CONFIG_MODIFY_ERROR = "ERR-aaa-config-modify-error"
	CONST_RMT_ERR_CODE_ERR_ACCT_REALM_SET_ERROR = "ERR-acct-realm-set-error"
	CONST_RMT_ERR_CODE_ERR_ADMIN_PASSWD_SET = "ERR-admin-passwd-set"
	CONST_RMT_ERR_CODE_ERR_AUTH_ISSUE = "ERR-auth-issue"
	CONST_RMT_ERR_CODE_ERR_AUTH_REALM_GET_ERROR = "ERR-auth-realm-get-error"
	CONST_RMT_ERR_CODE_ERR_AUTH_REALM_SET_ERROR = "ERR-auth-realm-set-error"
	CONST_RMT_ERR_CODE_ERR_AUTHENTICATION = "ERR-authentication"
	CONST_RMT_ERR_CODE_ERR_AUTHORIZATION_REQUIRED = "ERR-authorization-required"
	CONST_RMT_ERR_CODE_ERR_CLI_SESSION_LIMIT_REACHED = "ERR-cli-session-limit-reached"
	CONST_RMT_ERR_CODE_ERR_CREATE_KEYRING = "ERR-create-keyring"
	CONST_RMT_ERR_CODE_ERR_CREATE_LOCALE = "ERR-create-locale"
	CONST_RMT_ERR_CODE_ERR_CREATE_ROLE = "ERR-create-role"
	CONST_RMT_ERR_CODE_ERR_CREATE_USER = "ERR-create-user"
	CONST_RMT_ERR_CODE_ERR_DELETE_LOCALE = "ERR-delete-locale"
	CONST_RMT_ERR_CODE_ERR_DELETE_ROLE = "ERR-delete-role"
	CONST_RMT_ERR_CODE_ERR_DELETE_SESSION = "ERR-delete-session"
	CONST_RMT_ERR_CODE_ERR_DELETE_USER = "ERR-delete-user"
	CONST_RMT_ERR_CODE_ERR_EFI_DIAGNOSTICS_IN_PROGRESS = "ERR-efi-Diagnostics--in-progress"
	CONST_RMT_ERR_CODE_ERR_ENABLE_MGMT_CONN = "ERR-enable-mgmt-conn"
	CONST_RMT_ERR_CODE_ERR_EP_SET_ERROR = "ERR-ep-set-error"
	CONST_RMT_ERR_CODE_ERR_GET_MAX_HTTP_USER_SESSIONS = "ERR-get-max-http-user-sessions"
	CONST_RMT_ERR_CODE_ERR_HTTP_INITIALIZING = "ERR-http-initializing"
	CONST_RMT_ERR_CODE_ERR_INSUFFICIENTLY_EQUIPPED = "ERR-insufficiently-equipped"
	CONST_RMT_ERR_CODE_ERR_INTERNAL_ERROR = "ERR-internal-error"
	CONST_RMT_ERR_CODE_ERR_LDAP_DELETE_ERROR = "ERR-ldap-delete-error"
	CONST_RMT_ERR_CODE_ERR_LDAP_GET_ERROR = "ERR-ldap-get-error"
	CONST_RMT_ERR_CODE_ERR_LDAP_GROUP_MODIFY_ERROR = "ERR-ldap-group-modify-error"
	CONST_RMT_ERR_CODE_ERR_LDAP_GROUP_SET_ERROR = "ERR-ldap-group-set-error"
	CONST_RMT_ERR_CODE_ERR_LDAP_SET_ERROR = "ERR-ldap-set-error"
	CONST_RMT_ERR_CODE_ERR_LOCALE_SET_ERROR = "ERR-locale-set-error"
	CONST_RMT_ERR_CODE_ERR_MAX_USERID_SESSIONS_REACHED = "ERR-max-userid-sessions-reached"
	CONST_RMT_ERR_CODE_ERR_MISSING_METHOD = "ERR-missing-method"
	CONST_RMT_ERR_CODE_ERR_MODIFY_LOCALE = "ERR-modify-locale"
	CONST_RMT_ERR_CODE_ERR_MODIFY_ROLE = "ERR-modify-role"
	CONST_RMT_ERR_CODE_ERR_MODIFY_USER = "ERR-modify-user"
	CONST_RMT_ERR_CODE_ERR_MODIFY_USER_LOCALE = "ERR-modify-user-locale"
	CONST_RMT_ERR_CODE_ERR_MODIFY_USER_ROLE = "ERR-modify-user-role"
	CONST_RMT_ERR_CODE_ERR_PROVIDER_GROUP_MODIFY_ERROR = "ERR-provider-group-modify-error"
	CONST_RMT_ERR_CODE_ERR_PROVIDER_GROUP_SET_ERROR = "ERR-provider-group-set-error"
	CONST_RMT_ERR_CODE_ERR_RADIUS_GET_ERROR = "ERR-radius-get-error"
	CONST_RMT_ERR_CODE_ERR_RADIUS_GLOBAL_SET_ERROR = "ERR-radius-global-set-error"
	CONST_RMT_ERR_CODE_ERR_RADIUS_GROUP_SET_ERROR = "ERR-radius-group-set-error"
	CONST_RMT_ERR_CODE_ERR_RADIUS_SET_ERROR = "ERR-radius-set-error"
	CONST_RMT_ERR_CODE_ERR_REQUEST_TIMEOUT = "ERR-request-timeout"
	CONST_RMT_ERR_CODE_ERR_RESET_ADAPTER = "ERR-reset-adapter"
	CONST_RMT_ERR_CODE_ERR_ROLE_SET_ERROR = "ERR-role-set-error"
	CONST_RMT_ERR_CODE_ERR_SECONDARY_NODE = "ERR-secondary-node"
	CONST_RMT_ERR_CODE_ERR_SERVICE_NOT_READY = "ERR-service-not-ready"
	CONST_RMT_ERR_CODE_ERR_SESSION_CACHE_FULL = "ERR-session-cache-full"
	CONST_RMT_ERR_CODE_ERR_SESSION_NOT_FOUND = "ERR-session-not-found"
	CONST_RMT_ERR_CODE_ERR_SET_NETWORK = "ERR-set-network"
	CONST_RMT_ERR_CODE_ERR_SET_PASSWORD_STRENGTH_CHECK = "ERR-set-password-strength-check"
	CONST_RMT_ERR_CODE_ERR_SET_PORT_CHANNEL = "ERR-set-port-channel"
	CONST_RMT_ERR_CODE_ERR_STORE_PRE_LOGIN_BANNER_MSG = "ERR-store-pre-login-banner-msg"
	CONST_RMT_ERR_CODE_ERR_TACACS_ENABLE_ERROR = "ERR-tacacs-enable-error"
	CONST_RMT_ERR_CODE_ERR_TACACS_GLOBAL_SET_ERROR = "ERR-tacacs-global-set-error"
	CONST_RMT_ERR_CODE_ERR_TACACS_GROUP_SET_ERROR = "ERR-tacacs-group-set-error"
	CONST_RMT_ERR_CODE_ERR_TACACS_PLUS_GET_ERROR = "ERR-tacacs-plus-get-error"
	CONST_RMT_ERR_CODE_ERR_TACACS_SET_ERROR = "ERR-tacacs-set-error"
	CONST_RMT_ERR_CODE_ERR_TEST_ERROR_1 = "ERR-test-error-1"
	CONST_RMT_ERR_CODE_ERR_TEST_ERROR_2 = "ERR-test-error-2"
	CONST_RMT_ERR_CODE_ERR_TIMEZONE_SET_ERROR = "ERR-timezone-set-error"
	CONST_RMT_ERR_CODE_ERR_USER_ACCOUNT_EXPIRED = "ERR-user-account-expired"
	CONST_RMT_ERR_CODE_ERR_USER_SET_ERROR = "ERR-user-set-error"
	CONST_RMT_ERR_CODE_ERR_XML_PARSE_ERROR = "ERR-xml-parse-error"
	CONST_RMT_ERR_CODE_NONE = "none"
