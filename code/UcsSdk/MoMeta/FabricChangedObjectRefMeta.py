import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"CentraleVnetEpDn":UcsPropertyMeta("CentraleVnetEpDn", "centraleVnetEpDn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version212a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version212a, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["0-4294967295"]),
	"OldCentraleVnetEpDn":UcsPropertyMeta("OldCentraleVnetEpDn", "oldCentraleVnetEpDn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"RefObjStatus":UcsPropertyMeta("RefObjStatus", "refObjStatus", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["created", "deleted", "intent-deletion", "modified"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"UcsmVnetEpDn":UcsPropertyMeta("UcsmVnetEpDn", "ucsmVnetEpDn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricChangedObjectRef", "fabricChangedObjectRef", "ChangedObjectRef[Id]", _VersionMeta.Version212a, "InputOutput", 0x1fL, [], [], [None], ["read-only"])
}

