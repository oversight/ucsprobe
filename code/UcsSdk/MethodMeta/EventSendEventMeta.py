import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InDn":UcsFactoryMeta("InDn", "inDn", "Xs:string", "Version142b", "Input", False),
	"InEvent":UcsFactoryMeta("InEvent", "inEvent", "Method", "Version142b", "Input", True),
	"InReqId":UcsFactoryMeta("InReqId", "inReqId", "Xs:unsignedInt", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("EventSendEvent","eventSendEvent", "Version142b")
}

