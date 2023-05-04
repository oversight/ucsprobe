import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfig":UcsFactoryMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
	"InIsRefresh":UcsFactoryMeta("InIsRefresh", "inIsRefresh", "Xs:unsignedInt", "Version142b", "Input", False),
	"InSwId":UcsFactoryMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
	"InSwPortId":UcsFactoryMeta("InSwPortId", "inSwPortId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InSwSlotId":UcsFactoryMeta("InSwSlotId", "inSwSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeInsertNewFex","apeInsertNewFex", "Version142b")
}

