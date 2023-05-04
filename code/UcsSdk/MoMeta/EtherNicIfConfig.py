import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherNicIfConfig(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherNicIfConfig")

	@staticmethod
	def ClassId():
		return "etherNicIfConfig"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

