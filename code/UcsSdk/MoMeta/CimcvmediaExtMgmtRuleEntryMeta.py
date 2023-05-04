import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"ExtMgmtIpAddr":UcsPropertyMeta("ExtMgmtIpAddr", "extMgmtIpAddr", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"MappingName":UcsPropertyMeta("MappingName", "mappingName", "string", _VersionMeta.Version222c, UcsPropertyMeta.Naming, 0x4L, None, None, """[a-zA-Z0-9][a-zA-Z0-9_.:-]{0,63}""", [], ["0-4294967295"]),
	"MgmtIfIpAddr":UcsPropertyMeta("MgmtIfIpAddr", "mgmtIfIpAddr", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"MountProtocol":UcsPropertyMeta("MountProtocol", "mountProtocol", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cifs", "http", "https", "nfs", "unknown"], ["0-4294967295"]),
	"RemoteIpAddr":UcsPropertyMeta("RemoteIpAddr", "remoteIpAddr", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"RemotePort":UcsPropertyMeta("RemotePort", "remotePort", "uint", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("CimcvmediaExtMgmtRuleEntry", "cimcvmediaExtMgmtRuleEntry", "ext-mgmt-rule-[MappingName]", _VersionMeta.Version222c, "InputOutput", 0x1fL, [], [], [None], ["read-only"])
}

