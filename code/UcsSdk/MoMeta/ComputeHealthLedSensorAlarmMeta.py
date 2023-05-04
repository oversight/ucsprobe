import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AlarmDesc":UcsPropertyMeta("AlarmDesc", "alarmDesc", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"AlarmSeverity":UcsPropertyMeta("AlarmSeverity", "alarmSeverity", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["minor", "severe"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version212a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"SensorId":UcsPropertyMeta("SensorId", "sensorId", "ushort", _VersionMeta.Version212a, UcsPropertyMeta.Naming, 0x8L, None, None, None, [], ["0-4294967295"]),
	"SensorName":UcsPropertyMeta("SensorName", "sensorName", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ComputeHealthLedSensorAlarm", "computeHealthLedSensorAlarm", "sensor-alarm-[SensorId]", _VersionMeta.Version212a, "InputOutput", 0x1fL, [], [], ["Get"], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"])
}

