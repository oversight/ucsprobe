import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"NumOfCpu":UcsPropertyMeta("NumOfCpu", "numOfCpu", "byte", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"NumOfDimm":UcsPropertyMeta("NumOfDimm", "numOfDimm", "ushort", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"NumOfLocalDisk":UcsPropertyMeta("NumOfLocalDisk", "numOfLocalDisk", "byte", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"NumOfStorageController":UcsPropertyMeta("NumOfStorageController", "numOfStorageController", "byte", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"NumOfadaptor":UcsPropertyMeta("NumOfadaptor", "numOfadaptor", "byte", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentPhysDevicesPerBoard", "equipmentPhysDevicesPerBoard", "phys-dev-per-board", _VersionMeta.Version222c, "InputOutput", 0x1ffL, [], [], [None], [""])
}

