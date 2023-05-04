import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Description":UcsPropertyMeta("Description", "description", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x2L, 0, 510, None, [], ["0-4294967295"]),
	"DeviceType":UcsPropertyMeta("DeviceType", "deviceType", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["cdd", "hdd", "unknown"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"EncPwd":UcsPropertyMeta("EncPwd", "encPwd", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"ImageFileName":UcsPropertyMeta("ImageFileName", "imageFileName", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"ImagePath":UcsPropertyMeta("ImagePath", "imagePath", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"MappingName":UcsPropertyMeta("MappingName", "mappingName", "string", _VersionMeta.Version222c, UcsPropertyMeta.Naming, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"MountProtocol":UcsPropertyMeta("MountProtocol", "mountProtocol", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["cifs", "http", "https", "nfs", "unknown"], ["0-4294967295"]),
	"Password":UcsPropertyMeta("Password", "password", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,128}""", [], ["0-4294967295"]),
	"PwdSet":UcsPropertyMeta("PwdSet", "pwdSet", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"RemoteHost":UcsPropertyMeta("RemoteHost", "remoteHost", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], ["0-4294967295"]),
	"RemoteIpAddress":UcsPropertyMeta("RemoteIpAddress", "remoteIpAddress", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], ["0-4294967295"]),
	"RemotePort":UcsPropertyMeta("RemotePort", "remotePort", "uint", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x1000L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"UserId":UcsPropertyMeta("UserId", "userId", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, """[\-\.:_a-zA-Z0-9]{0,63}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("CimcvmediaConfigMountEntry", "cimcvmediaConfigMountEntry", "cfg-mnt-entry-[MappingName]", _VersionMeta.Version222c, "InputOutput", 0x7fffL, [], [], [None], ["admin", "read-only"])
}

