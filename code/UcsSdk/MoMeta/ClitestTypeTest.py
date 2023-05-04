import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ClitestTypeTest(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ClitestTypeTest")

	@staticmethod
	def ClassId():
		return "clitestTypeTest"

	ACHAR = "Achar"
	ADATE = "Adate"
	ADATETIME = "Adatetime"
	AFLOAT = "Afloat"
	AMAC = "Amac"
	ANENUM = "Anenum"
	ANIPV4 = "Anipv4"
	ANIPV6 = "Anipv6"
	ANSBYTE = "Ansbyte"
	ANSINT16 = "Ansint16"
	ANSINT32 = "Ansint32"
	ANSINT64 = "Ansint64"
	APASSWORD = "Apassword"
	ARANGE = "Arange"
	ARCSTRING = "Arcstring"
	ARXSTRING = "Arxstring"
	ASTRING = "Astring"
	ATIME = "Atime"
	AUBYTE = "Aubyte"
	AUINT16 = "Auint16"
	AUINT32 = "Auint32"
	AUINT64 = "Auint64"
	AWWN = "Awwn"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

	CONST_ANENUM_DOWN = "down"
	CONST_ANENUM_KIND_OF_UP = "kindOfUp"
	CONST_ANENUM_SORT_OF_DOWN = "sortOfDown"
	CONST_ANENUM_UP = "up"
