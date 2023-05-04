import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfig":UcsFactoryMeta("InConfig", "inConfig", "ConfigSet", "Version142b", "Input", True),
	"InTest":UcsFactoryMeta("InTest", "inTest", "Xs:string", "Version142b", "Input", False),
	"InWhat":UcsFactoryMeta("InWhat", "inWhat", "Xs:string", "Version142b", "Input", False),
	"OutConfig":UcsFactoryMeta("OutConfig", "outConfig", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("SyntheticTestTx","syntheticTestTx", "Version142b")
}

