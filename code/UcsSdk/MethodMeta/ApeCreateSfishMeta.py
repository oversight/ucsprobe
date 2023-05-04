import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InBladeSlotId":UcsFactoryMeta("InBladeSlotId", "inBladeSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InChassisId":UcsFactoryMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InConfig":UcsFactoryMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
	"InSwId":UcsFactoryMeta("InSwId", "inSwId", "Xs:string", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeCreateSfish","apeCreateSfish", "Version142b")
}

