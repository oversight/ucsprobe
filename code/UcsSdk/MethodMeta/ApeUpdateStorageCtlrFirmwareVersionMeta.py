import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfig":UcsFactoryMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
	"Meta":UcsFactoryMethodMeta("ApeUpdateStorageCtlrFirmwareVersion","apeUpdateStorageCtlrFirmwareVersion", "Version142b")
}

