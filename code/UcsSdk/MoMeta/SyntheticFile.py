import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SyntheticFile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SyntheticFile")

	@staticmethod
	def ClassId():
		return "syntheticFile"

	ATIME = "Atime"
	BLKSIZE = "Blksize"
	BLOCKS = "Blocks"
	CTIME = "Ctime"
	DEV = "Dev"
	DN = "Dn"
	GID = "Gid"
	INO = "Ino"
	MODE = "Mode"
	MTIME = "Mtime"
	NAME = "Name"
	NLINK = "Nlink"
	PATH = "Path"
	RDEV = "Rdev"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"
	UID = "Uid"

