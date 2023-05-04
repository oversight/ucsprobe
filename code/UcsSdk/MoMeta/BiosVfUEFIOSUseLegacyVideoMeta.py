import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VpUEFIOSUseLegacyVideo":UcsPropertyMeta("VpUEFIOSUseLegacyVideo", "vpUEFIOSUseLegacyVideo", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosVfUEFIOSUseLegacyVideo", "biosVfUEFIOSUseLegacyVideo", "UEFI-OS-use-legacy-video", _VersionMeta.Version141i, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"])
}
