import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InClientConnectorDn":UcsFactoryMeta("InClientConnectorDn", "inClientConnectorDn", "ReferenceObject", "Version142b", "Input", False),
	"InContext":UcsFactoryMeta("InContext", "inContext", "ReferenceObject", "Version142b", "Input", False),
	"InFilter":UcsFactoryMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
	"InPolicyType":UcsFactoryMeta("InPolicyType", "inPolicyType", "Xs:string", "Version142b", "Input", False),
	"OutPolicyNames":UcsFactoryMeta("OutPolicyNames", "outPolicyNames", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("PolicyResolveNames","policyResolveNames", "Version142b")
}

