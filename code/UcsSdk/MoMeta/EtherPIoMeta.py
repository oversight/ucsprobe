import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"AdminTransport":UcsPropertyMeta("AdminTransport", "adminTransport", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"ChassisId":UcsPropertyMeta("ChassisId", "chassisId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-255"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Encap":UcsPropertyMeta("Encap", "encap", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["dot1q", "isl", "negotiate", "proprietary", "unknown"], ["0-4294967295"]),
	"EpDn":UcsPropertyMeta("EpDn", "epDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"FsmDescr":UcsPropertyMeta("FsmDescr", "fsmDescr", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"FsmPrev":UcsPropertyMeta("FsmPrev", "fsmPrev", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, ["InCompatSfpPresenceBegin", "InCompatSfpPresenceFail", "InCompatSfpPresenceShutdown", "InCompatSfpPresenceSuccess", "InCompatSfpReplacedBegin", "InCompatSfpReplacedEnablePort", "InCompatSfpReplacedFail", "InCompatSfpReplacedSuccess", "nop"], ["0-4294967295"]),
	"FsmProgr":UcsPropertyMeta("FsmProgr", "fsmProgr", "byte", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-100"]),
	"FsmRmtInvErrCode":UcsPropertyMeta("FsmRmtInvErrCode", "fsmRmtInvErrCode", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]),
	"FsmRmtInvErrDescr":UcsPropertyMeta("FsmRmtInvErrDescr", "fsmRmtInvErrDescr", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, 0, 510, None, [], ["0-4294967295"]),
	"FsmRmtInvRslt":UcsPropertyMeta("FsmRmtInvRslt", "fsmRmtInvRslt", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, """((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], ["0-4294967295"]),
	"FsmStageDescr":UcsPropertyMeta("FsmStageDescr", "fsmStageDescr", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"FsmStamp":UcsPropertyMeta("FsmStamp", "fsmStamp", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"FsmStatus":UcsPropertyMeta("FsmStatus", "fsmStatus", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, ["InCompatSfpPresenceBegin", "InCompatSfpPresenceFail", "InCompatSfpPresenceShutdown", "InCompatSfpPresenceSuccess", "InCompatSfpReplacedBegin", "InCompatSfpReplacedEnablePort", "InCompatSfpReplacedFail", "InCompatSfpReplacedSuccess", "nop"], ["0-4294967295"]),
	"FsmTry":UcsPropertyMeta("FsmTry", "fsmTry", "byte", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"IfRole":UcsPropertyMeta("IfRole", "ifRole", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], ["0-4294967295"]),
	"IfType":UcsPropertyMeta("IfType", "ifType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], ["0-4294967295"]),
	"IsPortChannelMember":UcsPropertyMeta("IsPortChannelMember", "isPortChannelMember", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Lc":UcsPropertyMeta("Lc", "lc", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], ["0-4294967295"]),
	"LicGP":UcsPropertyMeta("LicGP", "licGP", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LicState":UcsPropertyMeta("LicState", "licState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], ["0-4294967295"]),
	"Locale":UcsPropertyMeta("Locale", "locale", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], ["0-4294967295"]),
	"Mac":UcsPropertyMeta("Mac", "mac", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"Mode":UcsPropertyMeta("Mode", "mode", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["E", "F", "SD", "access", "fabric", "n_proxy", "trunk", "unknown"], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperSpeed":UcsPropertyMeta("OperSpeed", "operSpeed", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["10gbps", "1gbps", "20gbps", "40gbps", "indeterminate"], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["admin-down", "error-disabled", "failed", "hardware-failure", "indeterminate", "link-down", "link-up", "no-license", "sfp-not-present", "software-failure", "udld-aggr-down", "up"], ["0-4294967295"]),
	"PeerChassisId":UcsPropertyMeta("PeerChassisId", "peerChassisId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["N/A"], ["0-255"]),
	"PeerDn":UcsPropertyMeta("PeerDn", "peerDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PeerPortId":UcsPropertyMeta("PeerPortId", "peerPortId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PeerSlotId":UcsPropertyMeta("PeerSlotId", "peerSlotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PortId":UcsPropertyMeta("PortId", "portId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, None, None, None, [], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"SlotId":UcsPropertyMeta("SlotId", "slotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"StateQual":UcsPropertyMeta("StateQual", "stateQual", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"Ts":UcsPropertyMeta("Ts", "ts", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"UnifiedPort":UcsPropertyMeta("UnifiedPort", "unifiedPort", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"UsrLbl":UcsPropertyMeta("UsrLbl", "usrLbl", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"XcvrType":UcsPropertyMeta("XcvrType", "xcvrType", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["10gbaseer", "10gbaselr", "10gbaselrm", "10gbasesr", "cwdm1471", "cwdm1531", "cwdm1551", "fet", "h10gcu1m", "h10gcu3m", "h10gcu5m", "h10gcu7m", "h10glrmsm", "h10gusr", "sfp", "unknown", "x2"], ["0-4294967295"]),
	"Meta":UcsMoMeta("EtherPIo", "etherPIo", "port-[PortId]", _VersionMeta.Version101e, "InputOutput", 0x7fL, [], [u'equipmentXcvr', u'etherErrStats', u'etherLossStats', u'etherPIoEndPoint', u'etherPIoFsm', u'etherPauseStats', u'etherRxStats', u'etherTxStats', u'eventInst', u'faultInst', u'lldpAcquired', u'networkIfStats', u'portDomainEp', u'portPIoFsm', u'portPIoFsmTask'], ["Get"], ["read-only"])
}

