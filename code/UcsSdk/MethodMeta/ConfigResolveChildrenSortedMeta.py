import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ClassId":UcsFactoryMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InDn":UcsFactoryMeta("InDn", "inDn", "ReferenceObject", "Version142b", "Input", False),
	"InFilter":UcsFactoryMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"InSize":UcsFactoryMeta("InSize", "inSize", "Xs:unsignedShort", "Version142b", "Input", False),
	"OutContext":UcsFactoryMeta("OutContext", "outContext", "Xs:unsignedLong", "Version142b", "Output", False),
	"OutTotalSize":UcsFactoryMeta("OutTotalSize", "outTotalSize", "Xs:unsignedInt", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("ConfigResolveChildrenSorted","configResolveChildrenSorted", "Version142b")
}

