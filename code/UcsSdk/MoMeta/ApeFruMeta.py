import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BoardManufacturer":UcsPropertyMeta("BoardManufacturer", "boardManufacturer", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, 0, 510, None, [], ["0-4294967295"]),
	"BoardMfgTime":UcsPropertyMeta("BoardMfgTime", "boardMfgTime", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["0-4294967295"]),
	"BoardPartNo":UcsPropertyMeta("BoardPartNo", "boardPartNo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, 0, 510, None, [], ["0-4294967295"]),
	"BoardProductName":UcsPropertyMeta("BoardProductName", "boardProductName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, 0, 510, None, [], ["0-4294967295"]),
	"BoardSerialNo":UcsPropertyMeta("BoardSerialNo", "boardSerialNo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, 0, 510, None, [], ["0-4294967295"]),
	"BoardVid":UcsPropertyMeta("BoardVid", "boardVid", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadWrite, 0x20L, 0, 510, None, [], ["0-4294967295"]),
	"ChassisPartNo":UcsPropertyMeta("ChassisPartNo", "chassisPartNo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, 0, 510, None, [], ["0-4294967295"]),
	"ChassisSerialNo":UcsPropertyMeta("ChassisSerialNo", "chassisSerialNo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, 0, 510, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x100L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ControlPlaneMac1":UcsPropertyMeta("ControlPlaneMac1", "controlPlaneMac1", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"ControlPlaneMac2":UcsPropertyMeta("ControlPlaneMac2", "controlPlaneMac2", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"DataPlaneMac1":UcsPropertyMeta("DataPlaneMac1", "dataPlaneMac1", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"DataPlaneMac2":UcsPropertyMeta("DataPlaneMac2", "dataPlaneMac2", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"DataPlaneWwn1":UcsPropertyMeta("DataPlaneWwn1", "dataPlaneWwn1", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"DataPlaneWwn2":UcsPropertyMeta("DataPlaneWwn2", "dataPlaneWwn2", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8000L, 0, 256, None, [], ["0-4294967295"]),
	"EntityType":UcsPropertyMeta("EntityType", "entityType", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10000L, None, None, None, ["ADD_IN_CARD", "BACK_PANEL_BOARD", "BATTERY", "BIOS", "CABLE_INTERCONNECT", "CHASSIS_BACK_PANEL_BOARD", "CMC", "CONNECTIVITY_SWITCH", "COOLING_UNIT", "DEVICE_BAY", "DISK", "DISK_DRIVE_BAY", "DRIVE_BACKPLANE", "EXTERNAL_ENVIRONMENT", "FAN_COOLING", "FRONT_PANEL_BOARD", "GROUP", "IBMC", "IO_MODULE", "IPMI_CHANNEL", "MEMORY_DEVICE", "MEMORY_MODULE", "MGMT_CONTROLLER_FIRMWARE", "OPERATING_SYSTEM", "OTHER", "OTHER_CHASSIS_BOARD", "OTHER_SYSTEM_BOARD", "PCI_BUS", "PCI_EXPRESS_BUS", "PERIPHERAL", "PERIPHERAL_BAY", "POWER_MANAGEMENT_BOARD", "POWER_MODULE", "POWER_SUPPLY", "POWER_SYSTEM_BOARD", "POWER_UNIT", "PROCESSING_BLADE", "PROCESSOR", "PROCESSOR_BOARD", "PROCESSOR_FRONT_SIDE_BUS", "PROCESSOR_IO_MODULE", "PROCESSOR_MEMORY_MODULE", "PROCESSOR_MODULE", "REMOTE_MGMT_COMM_DEVICE", "SATA_SAS_BUS", "SCSI_BUS", "SUB_CHASSIS", "SYSTEM_BOARD", "SYSTEM_BUS", "SYSTEM_CHASSIS", "SYSTEM_INTERNAL_EXPANSION_BOARD", "SYSTEM_MANAGEMENT_MODULE", "SYSTEM_MANAGEMENT_SOFTWARE", "UNKNOWN", "UNSPECIFIED"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20000L, None, None, None, [], ["0-4294967295"]),
	"Instance":UcsPropertyMeta("Instance", "instance", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40000L, None, None, None, [], ["0-4294967295"]),
	"ProductAssetTag":UcsPropertyMeta("ProductAssetTag", "productAssetTag", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80000L, 0, 510, None, [], ["0-4294967295"]),
	"ProductManufacturer":UcsPropertyMeta("ProductManufacturer", "productManufacturer", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100000L, 0, 510, None, [], ["0-4294967295"]),
	"ProductName":UcsPropertyMeta("ProductName", "productName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200000L, 0, 510, None, [], ["0-4294967295"]),
	"ProductPartNo":UcsPropertyMeta("ProductPartNo", "productPartNo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400000L, 0, 510, None, [], ["0-4294967295"]),
	"ProductSerialNo":UcsPropertyMeta("ProductSerialNo", "productSerialNo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800000L, 0, 510, None, [], ["0-4294967295"]),
	"ProductVersionNo":UcsPropertyMeta("ProductVersionNo", "productVersionNo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000000L, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2000000L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8000000L, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApeFru", "apeFru", "fru-[Id]", _VersionMeta.Version101e, "InputOutput", 0xfffffffL, [], [], [None], ["read-only"])
}

