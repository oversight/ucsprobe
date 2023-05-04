import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InContext":UcsFactoryMeta("InContext", "inContext", "ReferenceObject", "Version142b", "Input", False),
	"InPolicyDigests":UcsFactoryMeta("InPolicyDigests", "inPolicyDigests", "ConfigSet", "Version142b", "Input", True),
	"InStimulusId":UcsFactoryMeta("InStimulusId", "inStimulusId", "Xs:unsignedLong", "Version142b", "Input", False),
	"OutPolicies":UcsFactoryMeta("OutPolicies", "outPolicies", "ConfigSet", "Version142b", "Output", True),
	"OutStimulusId":UcsFactoryMeta("OutStimulusId", "outStimulusId", "Xs:unsignedLong", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ConfigGetRemotePolicies","configGetRemotePolicies", "Version142b")
}

