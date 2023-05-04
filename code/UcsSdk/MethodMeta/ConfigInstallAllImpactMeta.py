import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"Dn":UcsFactoryMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
	"InBladePackVersion":UcsFactoryMeta("InBladePackVersion", "inBladePackVersion", "Xs:string", "Version142b", "Input", False),
	"InHostPackDns":UcsFactoryMeta("InHostPackDns", "inHostPackDns", "DnSet", "Version142b", "Input", True),
	"InInfraPackVersion":UcsFactoryMeta("InInfraPackVersion", "inInfraPackVersion", "Xs:string", "Version142b", "Input", False),
	"InRackPackVersion":UcsFactoryMeta("InRackPackVersion", "inRackPackVersion", "Xs:string", "Version142b", "Input", False),
	"OutConfigSet":UcsFactoryMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigInstallAllImpact","configInstallAllImpact", "Version142b")
}

