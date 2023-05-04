import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InChId":UcsFactoryMeta("InChId", "inChId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InMuxSlotId":UcsFactoryMeta("InMuxSlotId", "inMuxSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeMuxOffline","apeMuxOffline", "Version142b")
}

