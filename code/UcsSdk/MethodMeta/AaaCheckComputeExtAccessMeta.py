import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InDn":UcsFactoryMeta("InDn", "inDn", "ReferenceObject", "Version142b", "Input", False),
	"InUser":UcsFactoryMeta("InUser", "inUser", "Xs:string", "Version142b", "Input", False),
	"OutAllow":UcsFactoryMeta("OutAllow", "outAllow", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("AaaCheckComputeExtAccess","aaaCheckComputeExtAccess", "Version142b")
}

