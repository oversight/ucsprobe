import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfigs":UcsFactoryMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
	"OutAckables":UcsFactoryMeta("OutAckables", "outAckables", "ConfigMap", "Version142b", "Output", True),
	"OutAffected":UcsFactoryMeta("OutAffected", "outAffected", "ConfigMap", "Version142b", "Output", True),
	"OutOldAckables":UcsFactoryMeta("OutOldAckables", "outOldAckables", "ConfigMap", "Version142b", "Output", True),
	"OutOldAffected":UcsFactoryMeta("OutOldAffected", "outOldAffected", "ConfigMap", "Version142b", "Output", True),
	"OutRetry":UcsFactoryMeta("OutRetry", "outRetry", "Xs:unsignedShort", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ConfigEstimateImpact","configEstimateImpact", "Version142b")
}

