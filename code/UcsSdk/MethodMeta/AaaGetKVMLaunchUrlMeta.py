import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InCookie":UcsFactoryMeta("InCookie", "inCookie", "Xs:string", "Version142b", "Input", False),
	"InIpv4":UcsFactoryMeta("InIpv4", "inIpv4", "Xs:string", "Version142b", "Input", False),
	"OutUrl":UcsFactoryMeta("OutUrl", "outUrl", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("AaaGetKVMLaunchUrl","aaaGetKVMLaunchUrl", "Version142b")
}

