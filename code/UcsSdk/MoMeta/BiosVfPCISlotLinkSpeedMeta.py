import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VpPCIeSlot10LinkSpeed":UcsPropertyMeta("VpPCIeSlot10LinkSpeed", "vpPCIeSlot10LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot1LinkSpeed":UcsPropertyMeta("VpPCIeSlot1LinkSpeed", "vpPCIeSlot1LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot2LinkSpeed":UcsPropertyMeta("VpPCIeSlot2LinkSpeed", "vpPCIeSlot2LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot3LinkSpeed":UcsPropertyMeta("VpPCIeSlot3LinkSpeed", "vpPCIeSlot3LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot4LinkSpeed":UcsPropertyMeta("VpPCIeSlot4LinkSpeed", "vpPCIeSlot4LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot5LinkSpeed":UcsPropertyMeta("VpPCIeSlot5LinkSpeed", "vpPCIeSlot5LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot6LinkSpeed":UcsPropertyMeta("VpPCIeSlot6LinkSpeed", "vpPCIeSlot6LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot7LinkSpeed":UcsPropertyMeta("VpPCIeSlot7LinkSpeed", "vpPCIeSlot7LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot8LinkSpeed":UcsPropertyMeta("VpPCIeSlot8LinkSpeed", "vpPCIeSlot8LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpPCIeSlot9LinkSpeed":UcsPropertyMeta("VpPCIeSlot9LinkSpeed", "vpPCIeSlot9LinkSpeed", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosVfPCISlotLinkSpeed", "biosVfPCISlotLinkSpeed", "PCI-Slot-Link-Speed", _VersionMeta.Version222c, "InputOutput", 0x3fffL, [], [], [None], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"])
}

