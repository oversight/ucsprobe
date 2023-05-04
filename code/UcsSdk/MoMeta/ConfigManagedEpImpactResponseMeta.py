import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AffectedServers":UcsPropertyMeta("AffectedServers", "affectedServers", "ushort", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AppConnectorId":UcsPropertyMeta("AppConnectorId", "appConnectorId", "uint", _VersionMeta.Version212a, UcsPropertyMeta.Naming, 0x1L, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version212a, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"EpName":UcsPropertyMeta("EpName", "epName", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"ImpactAnalyzerId":UcsPropertyMeta("ImpactAnalyzerId", "impactAnalyzerId", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"RebootRequired":UcsPropertyMeta("RebootRequired", "rebootRequired", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"SourceConnectorId":UcsPropertyMeta("SourceConnectorId", "sourceConnectorId", "uint", _VersionMeta.Version212a, UcsPropertyMeta.Naming, 0x20L, None, None, None, [], ["0-4294967295"]),
	"State":UcsPropertyMeta("State", "state", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["complete", "not-started", "waiting"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ConfigManagedEpImpactResponse", "configManagedEpImpactResponse", "ManagedEpapp-id-[AppConnectorId]src-id-[SourceConnectorId]", _VersionMeta.Version212a, "InputOutput", 0xffL, [], [u'configImpact'], [None], ["read-only"])
}

