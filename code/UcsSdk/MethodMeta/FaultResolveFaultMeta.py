import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InId":UcsFactoryMeta("InId", "inId", "Xs:unsignedLong", "Version142b", "Input", False),
	"OutFault":UcsFactoryMeta("OutFault", "outFault", "ConfigConfig", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("FaultResolveFault","faultResolveFault", "Version142b")
}

