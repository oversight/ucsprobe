import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ImgprovTarget(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ImgprovTarget")

	@staticmethod
	def ClassId():
		return "imgprovTarget"

	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

