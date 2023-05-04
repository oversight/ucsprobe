import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfInterleaveConfiguration(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfInterleaveConfiguration")

	@staticmethod
	def ClassId():
		return "biosVfInterleaveConfiguration"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_CHANNEL_INTERLEAVING = "VpChannelInterleaving"
	VP_MEMORY_INTERLEAVING = "VpMemoryInterleaving"
	VP_RANK_INTERLEAVING = "VpRankInterleaving"

	CONST_VP_CHANNEL_INTERLEAVING_1_WAY = "1-way"
	CONST_VP_CHANNEL_INTERLEAVING_2_WAY = "2-way"
	CONST_VP_CHANNEL_INTERLEAVING_3_WAY = "3-way"
	CONST_VP_CHANNEL_INTERLEAVING_4_WAY = "4-way"
	CONST_VP_CHANNEL_INTERLEAVING_AUTO = "auto"
	CONST_VP_CHANNEL_INTERLEAVING_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_CHANNEL_INTERLEAVING_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_MEMORY_INTERLEAVING_2_WAY_NODE_INTERLEAVE = "2-way-node-interleave"
	CONST_VP_MEMORY_INTERLEAVING_4_WAY_NODE_INTERLEAVE = "4-way-node-interleave"
	CONST_VP_MEMORY_INTERLEAVING_8_WAY_INTERLEAVING_INTER_SOCKET = "8-way-interleaving-inter-socket"
	CONST_VP_MEMORY_INTERLEAVING_NUMA_1_WAY_NODE_INTERLEAVE = "numa---1-way-node-interleave"
	CONST_VP_MEMORY_INTERLEAVING_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_MEMORY_INTERLEAVING_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_RANK_INTERLEAVING_1_WAY = "1-way"
	CONST_VP_RANK_INTERLEAVING_2_WAY = "2-way"
	CONST_VP_RANK_INTERLEAVING_4_WAY = "4-way"
	CONST_VP_RANK_INTERLEAVING_8_WAY = "8-way"
	CONST_VP_RANK_INTERLEAVING_AUTO = "auto"
	CONST_VP_RANK_INTERLEAVING_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_RANK_INTERLEAVING_PLATFORM_RECOMMENDED = "platform-recommended"
