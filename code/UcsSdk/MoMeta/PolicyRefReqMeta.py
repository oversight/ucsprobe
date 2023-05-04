import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version212a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"RefConvertedDn":UcsPropertyMeta("RefConvertedDn", "refConvertedDn", "string", _VersionMeta.Version212a, UcsPropertyMeta.Naming, 0x4L, 1, 510, None, [], ["0-4294967295"]),
	"RefPolicyDn":UcsPropertyMeta("RefPolicyDn", "refPolicyDn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("PolicyRefReq", "policyRefReq", "refreq-[RefConvertedDn]", _VersionMeta.Version212a, "InputOutput", 0x1fL, [], [], [None], ["admin"])
}

