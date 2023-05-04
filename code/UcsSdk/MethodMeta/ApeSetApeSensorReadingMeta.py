import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InChassisId":UcsFactoryMeta("InChassisId", "inChassisId", "Xs:unsignedInt", "Version142b", "Input", False),
	"InFaultLevel":UcsFactoryMeta("InFaultLevel", "inFaultLevel", "Xs:unsignedInt", "Version142b", "Input", False),
	"InOperation":UcsFactoryMeta("InOperation", "inOperation", "Xs:unsignedInt", "Version142b", "Input", False),
	"InSensorName":UcsFactoryMeta("InSensorName", "inSensorName", "Xs:unsignedInt", "Version142b", "Input", False),
	"InServerId":UcsFactoryMeta("InServerId", "inServerId", "Xs:unsignedInt", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeSetApeSensorReading","apeSetApeSensorReading", "Version142b")
}

