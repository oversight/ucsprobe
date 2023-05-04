import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InFilePath":UcsFactoryMeta("InFilePath", "inFilePath", "Xs:string", "Version142b", "Input", False),
	"OutConfig":UcsFactoryMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigGetXmlFile","configGetXmlFile", "Version142b")
}

