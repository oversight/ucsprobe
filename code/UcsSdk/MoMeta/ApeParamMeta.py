import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Key":UcsPropertyMeta("Key", "key", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, None, ["ACTIVE_IMAGE", "BIOS_ACTIVE_IMAGE", "BIOS_ALTERNATE_IMAGE", "BIOS_STARTUP_IMAGE", "BLADE_POWER_BUDGET", "BOOT_INSTANCE_ID", "CHASSIS_POWER_BUDGET", "CMC_MODEL", "COMM_STATUS", "HEALTH_STATUS", "IMAGE1_STATUS", "IMAGE2_STATUS", "LOCATE_LED_STATE", "MEZZ_POST", "PECI_TCONTROL", "PEER_POST_STATUS", "PLD_UPDATE_STATUS", "PLD_VER", "POST_STATUS", "POWER_POLICY", "POWER_POLICY_PEER", "POWER_STATUS", "RUNNING_IMAGE", "SEL_CNTRS", "SW_BOOT_ORDER", "SW_UPDATE_STATUS", "SW_VER_IMAGE_1", "SW_VER_IMAGE_2", "THERMAL_INFO", "UBOOT_VERSION", "UNKNOWN"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Value":UcsPropertyMeta("Value", "value", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApeParam", "apeParam", "param-[Key]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [], [None], ["read-only"])
}

