import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ClassId":UcsFactoryMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfig":UcsFactoryMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
	"InFilter":UcsFactoryMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"OutConfigs":UcsFactoryMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigConfFiltered","configConfFiltered", "Version142b")
}

