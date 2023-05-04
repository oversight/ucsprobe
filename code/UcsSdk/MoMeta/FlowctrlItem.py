import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FlowctrlItem(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FlowctrlItem")

	@staticmethod
	def ClassId():
		return "flowctrlItem"

	DN = "Dn"
	NAME = "Name"
	PRIO = "Prio"
	RCV = "Rcv"
	RN = "Rn"
	SND = "Snd"
	STATUS = "Status"

	CONST_PRIO_AUTO = "auto"
	CONST_PRIO_ON = "on"
	CONST_RCV_OFF = "off"
	CONST_RCV_ON = "on"
	CONST_SND_OFF = "off"
	CONST_SND_ON = "on"
