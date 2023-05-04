import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"Dn":UcsFactoryMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
	"InClassId":UcsFactoryMeta("InClassId", "inClassId", "NamingClassId", "Version142b", "Input", False),
	"InFilter":UcsFactoryMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"OutConfigSet":UcsFactoryMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigFindPermitted","configFindPermitted", "Version142b")
}

