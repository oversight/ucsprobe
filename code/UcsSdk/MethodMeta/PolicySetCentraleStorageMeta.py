import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InData":UcsFactoryMeta("InData", "inData", "Xs:string", "Version142b", "Input", False),
	"InOper":UcsFactoryMeta("InOper", "inOper", "Xs:unsignedInt", "Version142b", "Input", False),
	"InSide":UcsFactoryMeta("InSide", "inSide", "Xs:string", "Version142b", "Input", False),
	"OutData":UcsFactoryMeta("OutData", "outData", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("PolicySetCentraleStorage","policySetCentraleStorage", "Version142b")
}

