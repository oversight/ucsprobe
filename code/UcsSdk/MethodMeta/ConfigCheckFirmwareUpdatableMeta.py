import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InUpdatableDns":UcsFactoryMeta("InUpdatableDns", "inUpdatableDns", "DnSet", "Version142b", "Input", True),
	"OutFailDns":UcsFactoryMeta("OutFailDns", "outFailDns", "DnSet", "Version142b", "Output", True),
	"OutInvalidDns":UcsFactoryMeta("OutInvalidDns", "outInvalidDns", "DnSet", "Version142b", "Output", True),
	"OutPassDns":UcsFactoryMeta("OutPassDns", "outPassDns", "DnSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigCheckFirmwareUpdatable","configCheckFirmwareUpdatable", "Version142b")
}

