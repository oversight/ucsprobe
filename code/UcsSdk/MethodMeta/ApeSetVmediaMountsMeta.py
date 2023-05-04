import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InChassisId":UcsFactoryMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InCount":UcsFactoryMeta("InCount", "inCount", "Xs:unsignedInt", "Version142b", "Input", False),
	"InSlotId":UcsFactoryMeta("InSlotId", "inSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InVMediaSet":UcsFactoryMeta("InVMediaSet", "inVMediaSet", "ConfigSet", "Version142b", "Input", True),
	"Meta":UcsFactoryMethodMeta("ApeSetVmediaMounts","apeSetVmediaMounts", "Version142b")
}

