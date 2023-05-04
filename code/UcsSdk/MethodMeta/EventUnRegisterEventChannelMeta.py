import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InDn":UcsFactoryMeta("InDn", "inDn", "Xs:string", "Version142b", "Input", False),
	"InReqID":UcsFactoryMeta("InReqID", "inReqID", "Xs:unsignedInt", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("EventUnRegisterEventChannel","eventUnRegisterEventChannel", "Version142b")
}

