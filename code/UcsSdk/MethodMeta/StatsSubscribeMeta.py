import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InCategory":UcsFactoryMeta("InCategory", "inCategory", "Xs:string", "Version142b", "Input", False),
	"InProvider":UcsFactoryMeta("InProvider", "inProvider", "Xs:string", "Version142b", "Input", False),
	"InSchemaInfo":UcsFactoryMeta("InSchemaInfo", "inSchemaInfo", "ConfigSet", "Version142b", "Input", True),
	"InTimeInterval":UcsFactoryMeta("InTimeInterval", "inTimeInterval", "Xs:string", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("StatsSubscribe","statsSubscribe", "Version142b")
}

