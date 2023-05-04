import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigQualifier":UcsPropertyMeta("ConfigQualifier", "configQualifier", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|pinned-target-misconfig),){0,37}(defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|pinned-target-misconfig){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{0,32}""", [], ["0-4294967295"]),
	"OperVnetDn":UcsPropertyMeta("OperVnetDn", "operVnetDn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperVnetName":UcsPropertyMeta("OperVnetName", "operVnetName", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE", "dual"], ["0-4294967295"]),
	"Vnet":UcsPropertyMeta("Vnet", "vnet", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["1-4093"]),
	"ZoningState":UcsPropertyMeta("ZoningState", "zoningState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"Meta":UcsMoMeta("StorageVsanRef", "storageVsanRef", "vsan-ref", _VersionMeta.Version211a, "InputOutput", 0x1fL, [], [u'faultInst'], ["Add", "Get", "Set"], ["admin", "ext-san-config", "ext-san-policy", "ls-storage", "ls-storage-policy"])
}

