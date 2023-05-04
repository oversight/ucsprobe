import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChassisId":UcsPropertyMeta("ChassisId", "chassisId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x1L, None, None, None, ["N/A"], ["0-255"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"ServerId":UcsPropertyMeta("ServerId", "serverId", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"SlotId":UcsPropertyMeta("SlotId", "slotId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, None, [], ["0-4294967295"]),
	"State":UcsPropertyMeta("State", "state", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["HALTING_HOSTOS", "HALTING_PNUOS", "HOSTOS", "PNUOS", "STARTING_HOSTOS", "STARTING_PNUOS", "UNKNOWN"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApeHostAgent", "apeHostAgent", "hostagent-[ChassisId]-[SlotId]", _VersionMeta.Version101e, "InputOutput", 0x7fL, [], [], [None], ["admin"])
}

