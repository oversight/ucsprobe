import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InFieldName":UcsFactoryMeta("InFieldName", "inFieldName", "Xs:unsignedInt", "Version142b", "Input", False),
	"InIpAddr":UcsFactoryMeta("InIpAddr", "inIpAddr", "AddressIPv4", "Version142b", "Input", False),
	"InVersion":UcsFactoryMeta("InVersion", "inVersion", "Xs:string", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeUpdateApeFirmwareParamTable","apeUpdateApeFirmwareParamTable", "Version142b")
}

