import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InVmSwitchDn":UcsFactoryMeta("InVmSwitchDn", "inVmSwitchDn", "ReferenceObject", "Version142b", "Input", False),
	"Meta":UcsFactoryMethodMeta("ApeDeleteSfish","apeDeleteSfish", "Version142b")
}

