import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InCookie":UcsFactoryMeta("InCookie", "inCookie", "Xs:string", "Version142b", "Input", False),
	"InName":UcsFactoryMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
	"OutChannel":UcsFactoryMeta("OutChannel", "outChannel", "Xs:string", "Version142b", "Output", False),
	"OutCookie":UcsFactoryMeta("OutCookie", "outCookie", "Xs:string", "Version142b", "Output", False),
	"OutDomains":UcsFactoryMeta("OutDomains", "outDomains", "Xs:string", "Version142b", "Output", False),
	"OutEvtChannel":UcsFactoryMeta("OutEvtChannel", "outEvtChannel", "Xs:string", "Version142b", "Output", False),
	"OutPriv":UcsFactoryMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
	"OutRefreshPeriod":UcsFactoryMeta("OutRefreshPeriod", "outRefreshPeriod", "Xs:unsignedInt", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("AaaTokenRefresh","aaaTokenRefresh", "Version142b")
}

