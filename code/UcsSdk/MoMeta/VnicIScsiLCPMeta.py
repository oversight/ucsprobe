import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdaptorProfileName":UcsPropertyMeta("AdaptorProfileName", "adaptorProfileName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x1L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Addr":UcsPropertyMeta("Addr", "addr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["derived"], ["0-4294967295"]),
	"AdminVcon":UcsPropertyMeta("AdminVcon", "adminVcon", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["1", "2", "3", "4", "any"], ["0-4294967295"]),
	"BootDev":UcsPropertyMeta("BootDev", "bootDev", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x8L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigQualifier":UcsPropertyMeta("ConfigQualifier", "configQualifier", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|pinned-target-misconfig),){0,37}(defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|pinned-target-misconfig){0,1}""", [], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"EquipmentDn":UcsPropertyMeta("EquipmentDn", "equipmentDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"IdentPoolName":UcsPropertyMeta("IdentPoolName", "identPoolName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"InstType":UcsPropertyMeta("InstType", "instType", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"NwTemplName":UcsPropertyMeta("NwTemplName", "nwTemplName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperAdaptorProfileName":UcsPropertyMeta("OperAdaptorProfileName", "operAdaptorProfileName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperIdentPoolName":UcsPropertyMeta("OperIdentPoolName", "operIdentPoolName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperOrder":UcsPropertyMeta("OperOrder", "operOrder", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"OperSpeed":UcsPropertyMeta("OperSpeed", "operSpeed", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["line-rate"], ["8-40000000"]),
	"OperStatsPolicyName":UcsPropertyMeta("OperStatsPolicyName", "operStatsPolicyName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperVcon":UcsPropertyMeta("OperVcon", "operVcon", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["1", "2", "3", "4", "any"], ["0-4294967295"]),
	"Order":UcsPropertyMeta("Order", "order", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["unspecified"], ["0-256"]),
	"Owner":UcsPropertyMeta("Owner", "owner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["conn_policy", "logical", "physical", "policy", "unknown"], ["0-4294967295"]),
	"PinToGroupName":UcsPropertyMeta("PinToGroupName", "pinToGroupName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"QosPolicyName":UcsPropertyMeta("QosPolicyName", "qosPolicyName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x800L, 0, 256, None, [], ["0-4294967295"]),
	"StatsPolicyName":UcsPropertyMeta("StatsPolicyName", "statsPolicyName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], ["0-4294967295"]),
	"VnicName":UcsPropertyMeta("VnicName", "vnicName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x8000L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicIScsiLCP", "vnicIScsiLCP", "iscsi-[Name]", _VersionMeta.Version211a, "InputOutput", 0xffffL, [], [u'fabricEthMonSrcEp', u'fabricFcMonSrcEp', u'fabricNetflowMonSrcEp', u'faultInst', u'vnicVlan'], ["Add", "Get", "Remove", "Set"], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"])
}

