import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"EvaluationMethod":UcsPropertyMeta("EvaluationMethod", "evaluationMethod", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["Deterministic", "Random"], ["0-4294967295"]),
	"InstanceMod":UcsPropertyMeta("InstanceMod", "instanceMod", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["CREATE", "DELETE"], ["0-4294967295"]),
	"Interval":UcsPropertyMeta("Interval", "interval", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"MaxHits":UcsPropertyMeta("MaxHits", "maxHits", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"SleepDelay":UcsPropertyMeta("SleepDelay", "sleepDelay", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["CRASH", "MOD", "RETURN", "SLEEP"], ["0-4294967295"]),
	"Meta":UcsMoMeta("SwatAction", "swatAction", "action-[Name]", _VersionMeta.Version101e, "InputOutput", 0x7ffL, [], [u'swatCondition', u'swatTarget', u'swatTrigger'], ["Get"], ["admin"])
}

