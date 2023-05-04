import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InFaultsOnly":UcsFactoryMeta("InFaultsOnly", "inFaultsOnly", "Xs:string", "Version142b", "Input", False),
	"OutBladeCapProviderConfig":UcsFactoryMeta("OutBladeCapProviderConfig", "outBladeCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutChassisCapProviderConfig":UcsFactoryMeta("OutChassisCapProviderConfig", "outChassisCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutChassisConfig":UcsFactoryMeta("OutChassisConfig", "outChassisConfig", "ConfigSet", "Version142b", "Output", True),
	"OutFIConfig":UcsFactoryMeta("OutFIConfig", "outFIConfig", "ConfigSet", "Version142b", "Output", True),
	"OutFaultsOnly":UcsFactoryMeta("OutFaultsOnly", "outFaultsOnly", "Xs:string", "Version142b", "Output", False),
	"OutFexCapProviderConfig":UcsFactoryMeta("OutFexCapProviderConfig", "outFexCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutFexConfig":UcsFactoryMeta("OutFexConfig", "outFexConfig", "ConfigSet", "Version142b", "Output", True),
	"OutGemCapProviderConfig":UcsFactoryMeta("OutGemCapProviderConfig", "outGemCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutIOCardCapProviderConfig":UcsFactoryMeta("OutIOCardCapProviderConfig", "outIOCardCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutLogicalConfig":UcsFactoryMeta("OutLogicalConfig", "outLogicalConfig", "ConfigSet", "Version142b", "Output", True),
	"OutMgmtIfConfig":UcsFactoryMeta("OutMgmtIfConfig", "outMgmtIfConfig", "ConfigSet", "Version142b", "Output", True),
	"OutPhysicalConfig":UcsFactoryMeta("OutPhysicalConfig", "outPhysicalConfig", "ConfigSet", "Version142b", "Output", True),
	"OutRackUnitCapProviderConfig":UcsFactoryMeta("OutRackUnitCapProviderConfig", "outRackUnitCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutSwitchCapProviderConfig":UcsFactoryMeta("OutSwitchCapProviderConfig", "outSwitchCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutTopSystemConfig":UcsFactoryMeta("OutTopSystemConfig", "outTopSystemConfig", "ConfigConfig", "Version142b", "Output", True),
	"OutTotalFaults":UcsFactoryMeta("OutTotalFaults", "outTotalFaults", "Xs:unsignedLong", "Version142b", "Output", False),
	"OutTypedFaultHolderConfig":UcsFactoryMeta("OutTypedFaultHolderConfig", "outTypedFaultHolderConfig", "ConfigSet", "Version142b", "Output", True),
	"OutVnicIpv4PooledAddrConfig":UcsFactoryMeta("OutVnicIpv4PooledAddrConfig", "outVnicIpv4PooledAddrConfig", "ConfigSet", "Version142b", "Output", True),
	"OutVnicIpv4ProfDerivedAddrConfig":UcsFactoryMeta("OutVnicIpv4ProfDerivedAddrConfig", "outVnicIpv4ProfDerivedAddrConfig", "ConfigSet", "Version142b", "Output", True),
	"Meta":UcsFactoryMethodMeta("ComputeGetInventory","computeGetInventory", "Version142b")
}

