import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"InIds":UcsFactoryMeta("InIds", "inIds", "ClassIdSet", "Version142b", "Input", True),
	"InSize":UcsFactoryMeta("InSize", "inSize", "Xs:unsignedShort", "Version142b", "Input", False),
	"OutContext":UcsFactoryMeta("OutContext", "outContext", "Xs:unsignedLong", "Version142b", "Output", False),
	"OutTotalSize":UcsFactoryMeta("OutTotalSize", "outTotalSize", "Xs:unsignedInt", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ConfigResolveClassesSorted","configResolveClassesSorted", "Version142b")
}

