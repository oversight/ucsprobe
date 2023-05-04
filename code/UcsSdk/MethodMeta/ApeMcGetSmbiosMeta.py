import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InChassisId":UcsFactoryMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InSlotId":UcsFactoryMeta("InSlotId", "inSlotId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InUpdateCnt":UcsFactoryMeta("InUpdateCnt", "inUpdateCnt", "Xs:int", "Version142b", "Input", False),
	"OutFilePath":UcsFactoryMeta("OutFilePath", "outFilePath", "Xs:string", "Version142b", "Output", False),
	"OutUpdateCnt":UcsFactoryMeta("OutUpdateCnt", "outUpdateCnt", "Xs:int", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ApeMcGetSmbios","apeMcGetSmbios", "Version142b")
}

