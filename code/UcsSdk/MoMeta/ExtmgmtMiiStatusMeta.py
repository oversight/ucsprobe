import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"MaxRetryCount":UcsPropertyMeta("MaxRetryCount", "maxRetryCount", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["1-3"]),
	"RetryInterval":UcsPropertyMeta("RetryInterval", "retryInterval", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["3-10"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ExtmgmtMiiStatus", "extmgmtMiiStatus", "mii-status-policy", _VersionMeta.Version141i, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "ext-lan-config"])
}

