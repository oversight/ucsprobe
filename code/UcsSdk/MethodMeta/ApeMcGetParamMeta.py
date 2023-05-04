import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InMcAddress":UcsFactoryMeta("InMcAddress", "inMcAddress", "AddressIPv4", "Version142b", "Input", False),
	"InParam":UcsFactoryMeta("InParam", "inParam", "Xs:unsignedInt", "Version142b", "Input", False),
	"OutConfigs":UcsFactoryMeta("OutConfigs", "outConfigs", "ConfigConfig", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ApeMcGetParam","apeMcGetParam", "Version142b")
}

