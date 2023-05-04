import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InContext":UcsFactoryMeta("InContext", "inContext", "Xs:unsignedLong", "Version142b", "Input", False),
	"InSize":UcsFactoryMeta("InSize", "inSize", "Xs:unsignedShort", "Version142b", "Input", False),
	"OutContext":UcsFactoryMeta("OutContext", "outContext", "Xs:unsignedLong", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ConfigResolveContext","configResolveContext", "Version142b")
}

