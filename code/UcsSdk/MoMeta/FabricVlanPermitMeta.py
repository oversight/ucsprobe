import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Cloud":UcsPropertyMeta("Cloud", "cloud", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x2L, None, None, """((defaultValue|unknown|fcsanmon|ethlan|ethestclan|fcestc|ethlanmon|fcsan),){0,7}(defaultValue|unknown|fcsanmon|ethlan|ethestclan|fcestc|ethlanmon|fcsan){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,32}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x40L, None, None, None, ["A", "B", "NONE", "dual"], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricVlanPermit", "fabricVlanPermit", "perm-[Cloud]sw-[SwitchId]net-[Name]", _VersionMeta.Version211a, "InputOutput", 0x7fL, [], [], [None], [""])
}

