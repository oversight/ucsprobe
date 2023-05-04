import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Acked":UcsPropertyMeta("Acked", "acked", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"AckedBy":UcsPropertyMeta("AckedBy", "ackedBy", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 32, None, [], ["0-4294967295"]),
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack", "user-discard"], ["0-4294967295"]),
	"AutoDelete":UcsPropertyMeta("AutoDelete", "autoDelete", "string", _VersionMeta.Version211a, UcsPropertyMeta.CreateOnly, 0x2L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"ChangeBy":UcsPropertyMeta("ChangeBy", "changeBy", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 32, None, [], ["0-4294967295"]),
	"ChangeDetails":UcsPropertyMeta("ChangeDetails", "changeDetails", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|bootmode-config|bmc-update-bios-fw|host-eth-if-qos-host-control|checkpoint|pin|adaptor-host-fw|blade-identity|boot-local-storage|ip|host-fcoe-if|host-virt-fc-if-pers-bind|host-eth-if-qos|binding|secureboot-config|host-if-pcie|local-disk-fw|implicit-reboot|sol|adaptor-nw-fw|agent-policy|boot-virt-pxe|boot-order|vif|host-nonvirt-fc-if-pers-bind|host-eth-if-nw-ctrl|host-virt-eth-if|vmedia-config|flexflash-config|implicit-host-eth-if-profile-redeploy|implicit-host-fc-if-profile-redeploy|ep-auth|mgmt-controller-fw|bios-fw|boot-nonvirt-pxe|boot-virt-vnic|vlan|host-fc-if-profile|host-virt-fc-if|host-nonvirt-eth-if|flexflash-reboot|storage-path|board-controller-fw|bios-profile|local-disk-policy|storage-controller-fw|boot-nonvirt-vnic|vsan|host-fc-if-qos|host-nonvirt-fc-if|host-eth-if-profile|graphics-card-fw),){0,51}(defaultValue|bootmode-config|bmc-update-bios-fw|host-eth-if-qos-host-control|checkpoint|pin|adaptor-host-fw|blade-identity|boot-local-storage|ip|host-fcoe-if|host-virt-fc-if-pers-bind|host-eth-if-qos|binding|secureboot-config|host-if-pcie|local-disk-fw|implicit-reboot|sol|adaptor-nw-fw|agent-policy|boot-virt-pxe|boot-order|vif|host-nonvirt-fc-if-pers-bind|host-eth-if-nw-ctrl|host-virt-eth-if|vmedia-config|flexflash-config|implicit-host-eth-if-profile-redeploy|implicit-host-fc-if-profile-redeploy|ep-auth|mgmt-controller-fw|bios-fw|boot-nonvirt-pxe|boot-virt-vnic|vlan|host-fc-if-profile|host-virt-fc-if|host-nonvirt-eth-if|flexflash-reboot|storage-path|board-controller-fw|bios-profile|local-disk-policy|storage-controller-fw|boot-nonvirt-vnic|vsan|host-fc-if-qos|host-nonvirt-fc-if|host-eth-if-profile|graphics-card-fw){0,1}""", [], ["0-4294967295"]),
	"ChangeMode":UcsPropertyMeta("ChangeMode", "changeMode", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["config", "diag", "diag-config", "diag-unconfig", "force-unconfig", "no-change", "rediscover", "remove-config", "unconfig"], ["0-4294967295"]),
	"Changes":UcsPropertyMeta("Changes", "changes", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|boot-order|server-assignment|operational-policies|server-identity|storage|networking|vnic-vhba-placement),){0,7}(defaultValue|boot-order|server-assignment|operational-policies|server-identity|storage|networking|vnic-vhba-placement){0,1}""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x4L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigIssues":UcsPropertyMeta("ConfigIssues", "configIssues", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic),){0,65}(defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic){0,1}""", [], ["0-4294967295"]),
	"DeploymentMode":UcsPropertyMeta("DeploymentMode", "deploymentMode", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["immediate", "timer-automatic", "user-ack"], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Disr":UcsPropertyMeta("Disr", "disr", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|ac-power-cycle|up-time),){0,2}(defaultValue|ac-power-cycle|up-time){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"IgnoreCap":UcsPropertyMeta("IgnoreCap", "ignoreCap", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Modified":UcsPropertyMeta("Modified", "modified", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OldPnDn":UcsPropertyMeta("OldPnDn", "oldPnDn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperScheduler":UcsPropertyMeta("OperScheduler", "operScheduler", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"PrevOperState":UcsPropertyMeta("PrevOperState", "prevOperState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Scheduler":UcsPropertyMeta("Scheduler", "scheduler", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("LsmaintAck", "lsmaintAck", "ack", _VersionMeta.Version141i, "InputOutput", 0x1ffL, [], [u'faultInst', u'trigLocalSched'], ["Get", "Set"], ["admin", "ls-compute", "ls-config", "ls-server"])
}

