import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"Dn":UcsFactoryMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
	"OutConfDns":UcsFactoryMeta("OutConfDns", "outConfDns", "DnSet", "Version142b", "Output", True),
	"OutInProgressDns":UcsFactoryMeta("OutInProgressDns", "outInProgressDns", "DnSet", "Version142b", "Output", True),
	"OutNonConfDns":UcsFactoryMeta("OutNonConfDns", "outNonConfDns", "DnSet", "Version142b", "Output", True),
	"OutNonUpgradableDns":UcsFactoryMeta("OutNonUpgradableDns", "outNonUpgradableDns", "DnSet", "Version142b", "Output", True),
	"OutToResetDns":UcsFactoryMeta("OutToResetDns", "outToResetDns", "DnSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ConfigCheckConformance","configCheckConformance", "Version142b")
}

