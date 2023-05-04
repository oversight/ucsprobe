import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ModulePower":UcsPropertyMeta("ModulePower", "ModulePower", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ModulePowerAvg":UcsPropertyMeta("ModulePowerAvg", "ModulePowerAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ModulePowerMax":UcsPropertyMeta("ModulePowerMax", "ModulePowerMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ModulePowerMin":UcsPropertyMeta("ModulePowerMin", "ModulePowerMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AvailablePower":UcsPropertyMeta("AvailablePower", "availablePower", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AvailablePowerAvg":UcsPropertyMeta("AvailablePowerAvg", "availablePowerAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AvailablePowerMax":UcsPropertyMeta("AvailablePowerMax", "availablePowerMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"AvailablePowerMin":UcsPropertyMeta("AvailablePowerMin", "availablePowerMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"ReservedPower":UcsPropertyMeta("ReservedPower", "reservedPower", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ReservedPowerAvg":UcsPropertyMeta("ReservedPowerAvg", "reservedPowerAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ReservedPowerMax":UcsPropertyMeta("ReservedPowerMax", "reservedPowerMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ReservedPowerMin":UcsPropertyMeta("ReservedPowerMin", "reservedPowerMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"TotalPower":UcsPropertyMeta("TotalPower", "totalPower", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TotalPowerAvg":UcsPropertyMeta("TotalPowerAvg", "totalPowerAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TotalPowerMax":UcsPropertyMeta("TotalPowerMax", "totalPowerMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TotalPowerMin":UcsPropertyMeta("TotalPowerMin", "totalPowerMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentFexPowerSummaryHist", "equipmentFexPowerSummaryHist", "[Id]", _VersionMeta.Version141i, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

