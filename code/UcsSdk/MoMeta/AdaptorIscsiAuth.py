import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorIscsiAuth(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorIscsiAuth")

	@staticmethod
	def ClassId():
		return "adaptorIscsiAuth"

	DN = "Dn"
	PASSWORD = "Password"
	RN = "Rn"
	STATUS = "Status"
	USER_ID = "UserId"

