import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"Dn":UcsFactoryMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"InNumberOf":UcsFactoryMeta("InNumberOf", "inNumberOf", "Xs:unsignedByte", "Version142b", "Input", False),
	"InServerNamePrefixOrEmpty":UcsFactoryMeta("InServerNamePrefixOrEmpty", "inServerNamePrefixOrEmpty", "Xs:string", "Version142b", "Input", False),
	"InTargetOrg":UcsFactoryMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
	"OutConfigs":UcsFactoryMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("LsInstantiateNTemplate","lsInstantiateNTemplate", "Version142b")
}

