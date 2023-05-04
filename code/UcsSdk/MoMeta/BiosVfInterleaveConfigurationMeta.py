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
	"VpChannelInterleaving":UcsPropertyMeta("VpChannelInterleaving", "vpChannelInterleaving", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["1-way", "2-way", "3-way", "4-way", "auto", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpMemoryInterleaving":UcsPropertyMeta("VpMemoryInterleaving", "vpMemoryInterleaving", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["2-way-node-interleave", "4-way-node-interleave", "8-way-interleaving-inter-socket", "numa---1-way-node-interleave", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"VpRankInterleaving":UcsPropertyMeta("VpRankInterleaving", "vpRankInterleaving", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["1-way", "2-way", "4-way", "8-way", "auto", "platform-default", "platform-recommended"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosVfInterleaveConfiguration", "biosVfInterleaveConfiguration", "Interleave-Configuration", _VersionMeta.Version222c, "InputOutput", 0x7fL, [], [], [None], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"])
}

