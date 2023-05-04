import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfLOMPortsConfiguration(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfLOMPortsConfiguration")

	@staticmethod
	def ClassId():
		return "biosVfLOMPortsConfiguration"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ALL_ONBOARD_LOMPORTS = "VpAllOnboardLOMPorts"
	VP_LOMPORT0_OPTION_ROM = "VpLOMPort0OptionROM"
	VP_LOMPORT1_OPTION_ROM = "VpLOMPort1OptionROM"
	VP_LOMPORT2_OPTION_ROM = "VpLOMPort2OptionROM"
	VP_LOMPORT3_OPTION_ROM = "VpLOMPort3OptionROM"

	CONST_VP_ALL_ONBOARD_LOMPORTS_DISABLED = "disabled"
	CONST_VP_ALL_ONBOARD_LOMPORTS_ENABLED = "enabled"
	CONST_VP_ALL_ONBOARD_LOMPORTS_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ALL_ONBOARD_LOMPORTS_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_LOMPORT0_OPTION_ROM_DISABLED = "disabled"
	CONST_VP_LOMPORT0_OPTION_ROM_ENABLED = "enabled"
	CONST_VP_LOMPORT0_OPTION_ROM_LEGACY_ONLY = "legacy-only"
	CONST_VP_LOMPORT0_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LOMPORT0_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_LOMPORT0_OPTION_ROM_UEFI_ONLY = "uefi-only"
	CONST_VP_LOMPORT1_OPTION_ROM_DISABLED = "disabled"
	CONST_VP_LOMPORT1_OPTION_ROM_ENABLED = "enabled"
	CONST_VP_LOMPORT1_OPTION_ROM_LEGACY_ONLY = "legacy-only"
	CONST_VP_LOMPORT1_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LOMPORT1_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_LOMPORT1_OPTION_ROM_UEFI_ONLY = "uefi-only"
	CONST_VP_LOMPORT2_OPTION_ROM_DISABLED = "disabled"
	CONST_VP_LOMPORT2_OPTION_ROM_ENABLED = "enabled"
	CONST_VP_LOMPORT2_OPTION_ROM_LEGACY_ONLY = "legacy-only"
	CONST_VP_LOMPORT2_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LOMPORT2_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_LOMPORT2_OPTION_ROM_UEFI_ONLY = "uefi-only"
	CONST_VP_LOMPORT3_OPTION_ROM_DISABLED = "disabled"
	CONST_VP_LOMPORT3_OPTION_ROM_ENABLED = "enabled"
	CONST_VP_LOMPORT3_OPTION_ROM_LEGACY_ONLY = "legacy-only"
	CONST_VP_LOMPORT3_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LOMPORT3_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_LOMPORT3_OPTION_ROM_UEFI_ONLY = "uefi-only"
