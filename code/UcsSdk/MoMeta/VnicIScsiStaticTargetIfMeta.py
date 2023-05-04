import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AuthProfileName":UcsPropertyMeta("AuthProfileName", "authProfileName", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IpAddress":UcsPropertyMeta("IpAddress", "ipAddress", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x8L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[0-9a-zA-Z\.:-]{0,223}""", [], ["0-4294967295"]),
	"OperAuthProfileName":UcsPropertyMeta("OperAuthProfileName", "operAuthProfileName", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Port":UcsPropertyMeta("Port", "port", "uint", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["1-65535"]),
	"Priority":UcsPropertyMeta("Priority", "priority", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.Naming, 0x40L, None, None, None, [], ["1-2"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicIScsiStaticTargetIf", "vnicIScsiStaticTargetIf", "[Priority]", _VersionMeta.Version201m, "InputOutput", 0x1ffL, [], [u'faultInst', u'vnicLun'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"])
}

