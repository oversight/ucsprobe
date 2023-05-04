import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InBackupSource":UcsFactoryMeta("InBackupSource", "inBackupSource", "Xs:string", "Version142b", "Input", False),
	"InType":UcsFactoryMeta("InType", "inType", "Xs:string", "Version142b", "Input", False),
	"OutBackups":UcsFactoryMeta("OutBackups", "outBackups", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("MgmtResolveBackupFilenames","mgmtResolveBackupFilenames", "Version142b")
}

