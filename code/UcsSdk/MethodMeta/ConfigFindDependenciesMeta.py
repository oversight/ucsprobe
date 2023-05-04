import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"Dn":UcsFactoryMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
	"InReturnConfigs":UcsFactoryMeta("InReturnConfigs", "inReturnConfigs", "Xs:string", "Version142b", "Input", False),
	"OutConfigs":UcsFactoryMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
	"OutHasDep":UcsFactoryMeta("OutHasDep", "outHasDep", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ConfigFindDependencies","configFindDependencies", "Version142b")
}

