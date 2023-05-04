import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"Dn":UcsFactoryMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
	"InErrorOnExisting":UcsFactoryMeta("InErrorOnExisting", "inErrorOnExisting", "Xs:string", "Version142b", "Input", False),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"InNameSet":UcsFactoryMeta("InNameSet", "inNameSet", "DnSet", "Version142b", "Input", True),
	"InTargetOrg":UcsFactoryMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
	"OutConfigs":UcsFactoryMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("LsInstantiateNNamedTemplate","lsInstantiateNNamedTemplate", "Version142b")
}

