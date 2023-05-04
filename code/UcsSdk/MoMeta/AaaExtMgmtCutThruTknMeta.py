import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AuthDomain":UcsPropertyMeta("AuthDomain", "authDomain", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"AuthUser":UcsPropertyMeta("AuthUser", "authUser", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version102d, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CreationTime":UcsPropertyMeta("CreationTime", "creationTime", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version102d, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Locales":UcsPropertyMeta("Locales", "locales", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version102d, UcsPropertyMeta.CreateOnly, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PnDn":UcsPropertyMeta("PnDn", "pnDn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Priv":UcsPropertyMeta("Priv", "priv", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """((ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault),){0,37}(ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault){0,1}""", [], ["0-4294967295"]),
	"Remote":UcsPropertyMeta("Remote", "remote", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Token":UcsPropertyMeta("Token", "token", "string", _VersionMeta.Version102d, UcsPropertyMeta.Naming, 0x80L, 1, 510, None, [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, None, None, None, None, ["kvm"], ["0-4294967295"]),
	"User":UcsPropertyMeta("User", "user", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaExtMgmtCutThruTkn", "aaaExtMgmtCutThruTkn", "-[Token]", _VersionMeta.Version102d, "InputOutput", 0xffL, [], [], ["Get"], ["aaa", "admin"])
}

