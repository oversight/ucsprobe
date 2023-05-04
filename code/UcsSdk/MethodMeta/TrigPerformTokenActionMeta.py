import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InContext":UcsFactoryMeta("InContext", "inContext", "ReferenceObject", "Version142b", "Input", False),
	"InOwnership":UcsFactoryMeta("InOwnership", "inOwnership", "Xs:string", "Version142b", "Input", False),
	"InSchedName":UcsFactoryMeta("InSchedName", "inSchedName", "Xs:string", "Version142b", "Input", False),
	"InTokenAction":UcsFactoryMeta("InTokenAction", "inTokenAction", "Xs:string", "Version142b", "Input", False),
	"InTokenId":UcsFactoryMeta("InTokenId", "inTokenId", "Xs:unsignedLong", "Version142b", "Input", False),
	"InTriggerableDn":UcsFactoryMeta("InTriggerableDn", "inTriggerableDn", "ReferenceObject", "Version142b", "Input", False),
	"InWindowName":UcsFactoryMeta("InWindowName", "inWindowName", "Xs:string", "Version142b", "Input", False),
	"InWindowType":UcsFactoryMeta("InWindowType", "inWindowType", "Xs:string", "Version142b", "Input", False),
	"OutLastTokenOperation":UcsFactoryMeta("OutLastTokenOperation", "outLastTokenOperation", "Xs:string", "Version142b", "Output", False),
	"OutNewTokenId":UcsFactoryMeta("OutNewTokenId", "outNewTokenId", "Xs:unsignedLong", "Version142b", "Output", False),
	"OutOldTokenId":UcsFactoryMeta("OutOldTokenId", "outOldTokenId", "Xs:unsignedLong", "Version142b", "Output", False),
	"OutOldTriggerableDn":UcsFactoryMeta("OutOldTriggerableDn", "outOldTriggerableDn", "ReferenceObject", "Version142b", "Output", False),
	"OutOwnership":UcsFactoryMeta("OutOwnership", "outOwnership", "Xs:string", "Version142b", "Output", False),
	"OutWindowName":UcsFactoryMeta("OutWindowName", "outWindowName", "Xs:string", "Version142b", "Output", False),
	"OutWindowType":UcsFactoryMeta("OutWindowType", "outWindowType", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("TrigPerformTokenAction","trigPerformTokenAction", "Version142b")
}

