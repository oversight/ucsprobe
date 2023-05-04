import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InDn":UcsFactoryMeta("InDn", "inDn", "Xs:string", "Version142b", "Input", False),
	"OutReqID":UcsFactoryMeta("OutReqID", "outReqID", "Xs:unsignedInt", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("EventRegisterEventChannel","eventRegisterEventChannel", "Version142b")
}

