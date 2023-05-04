import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InName":UcsFactoryMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
	"InPassword":UcsFactoryMeta("InPassword", "inPassword", "Xs:string", "Version142b", "Input", False),
	"OutChannel":UcsFactoryMeta("OutChannel", "outChannel", "Xs:string", "Version142b", "Output", False),
	"OutCookie":UcsFactoryMeta("OutCookie", "outCookie", "Xs:string", "Version142b", "Output", False),
	"OutDomains":UcsFactoryMeta("OutDomains", "outDomains", "Xs:string", "Version142b", "Output", False),
	"OutEvtChannel":UcsFactoryMeta("OutEvtChannel", "outEvtChannel", "Xs:string", "Version142b", "Output", False),
	"OutName":UcsFactoryMeta("OutName", "outName", "Xs:string", "Version142b", "Output", False),
	"OutPriv":UcsFactoryMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
	"OutRefreshPeriod":UcsFactoryMeta("OutRefreshPeriod", "outRefreshPeriod", "Xs:unsignedInt", "Version142b", "Output", False),
	"OutSessionId":UcsFactoryMeta("OutSessionId", "outSessionId", "Xs:string", "Version142b", "Output", False),
	"OutVersion":UcsFactoryMeta("OutVersion", "outVersion", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("AaaLogin","aaaLogin", "Version142b")
}

