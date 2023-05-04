import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version202m, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VpPCIeSlotSASOptionROM":UcsPropertyMeta("VpPCIeSlotSASOptionROM", "vpPCIeSlotSASOptionROM", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], ["0-4294967295"]),
	"VpSlot10State":UcsPropertyMeta("VpSlot10State", "vpSlot10State", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], ["0-4294967295"]),
	"VpSlot1State":UcsPropertyMeta("VpSlot1State", "vpSlot1State", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpSlot2State":UcsPropertyMeta("VpSlot2State", "vpSlot2State", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpSlot3State":UcsPropertyMeta("VpSlot3State", "vpSlot3State", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpSlot4State":UcsPropertyMeta("VpSlot4State", "vpSlot4State", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpSlot5State":UcsPropertyMeta("VpSlot5State", "vpSlot5State", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpSlot6State":UcsPropertyMeta("VpSlot6State", "vpSlot6State", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpSlot7State":UcsPropertyMeta("VpSlot7State", "vpSlot7State", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpSlot8State":UcsPropertyMeta("VpSlot8State", "vpSlot8State", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], ["0-4294967295"]),
	"VpSlot9State":UcsPropertyMeta("VpSlot9State", "vpSlot9State", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], ["0-4294967295"]),
	"VpSlotMezzState":UcsPropertyMeta("VpSlotMezzState", "vpSlotMezzState", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosVfPCISlotOptionROMEnable", "biosVfPCISlotOptionROMEnable", "PCI-Slot-OptionROM-Enable", _VersionMeta.Version202m, "InputOutput", 0x1fL, [], [], ["Get"], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"])
}

