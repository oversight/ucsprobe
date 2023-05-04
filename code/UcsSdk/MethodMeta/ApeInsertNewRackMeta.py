import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfig":UcsFactoryMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
	"InFxId":UcsFactoryMeta("InFxId", "inFxId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InFxPortId":UcsFactoryMeta("InFxPortId", "inFxPortId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InFxSlotId":UcsFactoryMeta("InFxSlotId", "inFxSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InIsRefresh":UcsFactoryMeta("InIsRefresh", "inIsRefresh", "Xs:unsignedInt", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeInsertNewRack","apeInsertNewRack", "Version142b")
}

