import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfigs":UcsFactoryMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"OutConfigs":UcsFactoryMeta("OutConfigs", "outConfigs", "ConfigMap", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigConfMos","configConfMos", "Version142b")
}

