import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InFruModel":UcsFactoryMeta("InFruModel", "inFruModel", "Xs:string", "Version142b", "Input", False),
	"InFruSerial":UcsFactoryMeta("InFruSerial", "inFruSerial", "Xs:string", "Version142b", "Input", False),
	"InFruVendor":UcsFactoryMeta("InFruVendor", "inFruVendor", "Xs:string", "Version142b", "Input", False),
	"OutOutConfig":UcsFactoryMeta("OutOutConfig", "outOutConfig", "ConfigConfig", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ApeGetPnuOSInventory","apeGetPnuOSInventory", "Version142b")
}

