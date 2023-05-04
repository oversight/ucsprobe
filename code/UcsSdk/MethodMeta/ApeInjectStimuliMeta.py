import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InFromSvc":UcsFactoryMeta("InFromSvc", "inFromSvc", "Xs:unsignedInt", "Version142b", "Input", False),
	"InStimuli":UcsFactoryMeta("InStimuli", "inStimuli", "MethodSet", "Version142b", "Input", True),
	"InToSvc":UcsFactoryMeta("InToSvc", "inToSvc", "Xs:unsignedInt", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeInjectStimuli","apeInjectStimuli", "Version142b")
}

