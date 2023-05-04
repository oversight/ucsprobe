import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InToken":UcsFactoryMeta("InToken", "inToken", "Xs:string", "Version142b", "Input", False),
	"InUser":UcsFactoryMeta("InUser", "inUser", "Xs:string", "Version142b", "Input", False),
	"OutAllow":UcsFactoryMeta("OutAllow", "outAllow", "Xs:string", "Version142b", "Output", False),
	"OutAuthDomain":UcsFactoryMeta("OutAuthDomain", "outAuthDomain", "Xs:string", "Version142b", "Output", False),
	"OutAuthUser":UcsFactoryMeta("OutAuthUser", "outAuthUser", "Xs:string", "Version142b", "Output", False),
	"OutLocales":UcsFactoryMeta("OutLocales", "outLocales", "Xs:string", "Version142b", "Output", False),
	"OutPriv":UcsFactoryMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
	"OutRemote":UcsFactoryMeta("OutRemote", "outRemote", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("AaaCheckComputeAuthToken","aaaCheckComputeAuthToken", "Version142b")
}

