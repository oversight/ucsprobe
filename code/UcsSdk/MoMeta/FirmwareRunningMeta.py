import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Deployment":UcsPropertyMeta("Deployment", "deployment", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x2L, None, None, None, ["boot-loader", "kernel", "system", "unspecified"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"PackageVersion":UcsPropertyMeta("PackageVersion", "packageVersion", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "catalog", "debug-plug-in", "diag", "fex", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "iocard", "local-disk", "mgmt-ext", "storage-controller", "switch", "switch-kernel", "switch-software", "system", "unspecified"], ["0-4294967295"]),
	"Version":UcsPropertyMeta("Version", "version", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FirmwareRunning", "firmwareRunning", "fw-[Deployment]", _VersionMeta.Version101e, "InputOutput", 0x1fL, [], [], ["Get"], ["read-only"])
}

