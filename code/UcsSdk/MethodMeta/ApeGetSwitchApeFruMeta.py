import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InSwId":UcsFactoryMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
	"OutControllerId":UcsFactoryMeta("OutControllerId", "outControllerId", "Xs:string", "Version142b", "Output", False),
	"OutControllerType":UcsFactoryMeta("OutControllerType", "outControllerType", "Xs:string", "Version142b", "Output", False),
	"OutControllerVendor":UcsFactoryMeta("OutControllerVendor", "outControllerVendor", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ApeGetSwitchApeFru","apeGetSwitchApeFru", "Version142b")
}

