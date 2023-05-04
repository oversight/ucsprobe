import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"Dn":UcsFactoryMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
	"InErrorOnExisting":UcsFactoryMeta("InErrorOnExisting", "inErrorOnExisting", "Xs:string", "Version142b", "Input", False),
	"InHierarchical":UcsFactoryMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
	"InServerName":UcsFactoryMeta("InServerName", "inServerName", "Xs:string", "Version142b", "Input", False),
	"InTargetOrg":UcsFactoryMeta("InTargetOrg", "inTargetOrg", "ReferenceObject", "Version142b", "Input", False),
	"OutConfig":UcsFactoryMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("LsInstantiateTemplate","lsInstantiateTemplate", "Version142b")
}

