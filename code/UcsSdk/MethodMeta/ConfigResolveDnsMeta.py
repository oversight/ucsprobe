import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InDns":UcsFactoryMeta("InDns", "inDns", "DnSet", "Version142b", "Input", True),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"OutConfigs":UcsFactoryMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
	"OutUnresolved":UcsFactoryMeta("OutUnresolved", "outUnresolved", "DnSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigResolveDns","configResolveDns", "Version142b")
}

