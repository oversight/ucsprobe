import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"Protocol":UcsPropertyMeta("Protocol", "protocol", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["netflow"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Session":UcsPropertyMeta("Session", "session", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["1-255"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Transport":UcsPropertyMeta("Transport", "transport", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricNetflowMonSrcEp", "fabricNetflowMonSrcEp", "flow-mon-src-[Name]", _VersionMeta.Version221b, "InputOutput", 0x3fL, [], [], [None], ["admin", "ext-lan-config", "ext-lan-policy"])
}

