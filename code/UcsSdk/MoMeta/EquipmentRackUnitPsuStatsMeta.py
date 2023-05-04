import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AmbientTemp":UcsPropertyMeta("AmbientTemp", "ambientTemp", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"AmbientTempAvg":UcsPropertyMeta("AmbientTempAvg", "ambientTempAvg", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"AmbientTempMax":UcsPropertyMeta("AmbientTempMax", "ambientTempMax", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"AmbientTempMin":UcsPropertyMeta("AmbientTempMin", "ambientTempMin", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"InputPower":UcsPropertyMeta("InputPower", "inputPower", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"InputPowerAvg":UcsPropertyMeta("InputPowerAvg", "inputPowerAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"InputPowerMax":UcsPropertyMeta("InputPowerMax", "inputPowerMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"InputPowerMin":UcsPropertyMeta("InputPowerMin", "inputPowerMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"InputVoltage":UcsPropertyMeta("InputVoltage", "inputVoltage", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Not-Applicable"], ["0-4294967295"]),
	"InputVoltageAvg":UcsPropertyMeta("InputVoltageAvg", "inputVoltageAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"InputVoltageMax":UcsPropertyMeta("InputVoltageMax", "inputVoltageMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"InputVoltageMin":UcsPropertyMeta("InputVoltageMin", "inputVoltageMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputCurrent":UcsPropertyMeta("OutputCurrent", "outputCurrent", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputCurrentAvg":UcsPropertyMeta("OutputCurrentAvg", "outputCurrentAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputCurrentMax":UcsPropertyMeta("OutputCurrentMax", "outputCurrentMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputCurrentMin":UcsPropertyMeta("OutputCurrentMin", "outputCurrentMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputPower":UcsPropertyMeta("OutputPower", "outputPower", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputPowerAvg":UcsPropertyMeta("OutputPowerAvg", "outputPowerAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputPowerMax":UcsPropertyMeta("OutputPowerMax", "outputPowerMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputPowerMin":UcsPropertyMeta("OutputPowerMin", "outputPowerMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputVoltage":UcsPropertyMeta("OutputVoltage", "outputVoltage", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Not-Applicable"], ["0-4294967295"]),
	"OutputVoltageAvg":UcsPropertyMeta("OutputVoltageAvg", "outputVoltageAvg", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputVoltageMax":UcsPropertyMeta("OutputVoltageMax", "outputVoltageMax", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OutputVoltageMin":UcsPropertyMeta("OutputVoltageMin", "outputVoltageMin", "float", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentRackUnitPsuStats", "equipmentRackUnitPsuStats", "rackunit-power-stats", _VersionMeta.Version141i, "OutputOnly", 0x0L, [], [u'equipmentRackUnitPsuStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

