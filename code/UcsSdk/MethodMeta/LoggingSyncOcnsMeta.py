import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InFromOrZero":UcsFactoryMeta("InFromOrZero", "inFromOrZero", "Xs:unsignedLong", "Version142b", "Input", False),
	"InToOrZero":UcsFactoryMeta("InToOrZero", "inToOrZero", "Xs:unsignedLong", "Version142b", "Input", False),
	"OutStimuli":UcsFactoryMeta("OutStimuli", "outStimuli", "MethodSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("LoggingSyncOcns","loggingSyncOcns", "Version142b")
}

