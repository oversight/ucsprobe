import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"DvsGenPortId":UcsPropertyMeta("DvsGenPortId", "dvsGenPortId", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"DvsPortId":UcsPropertyMeta("DvsPortId", "dvsPortId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DvsSwitchId":UcsPropertyMeta("DvsSwitchId", "dvsSwitchId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"HostIfDn":UcsPropertyMeta("HostIfDn", "hostIfDn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"MacAddr":UcsPropertyMeta("MacAddr", "macAddr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, 1, 31, None, [], ["0-4294967295"]),
	"Owner":UcsPropertyMeta("Owner", "owner", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["conn_policy", "logical", "physical", "policy", "unknown"], ["0-4294967295"]),
	"PhSwitchId":UcsPropertyMeta("PhSwitchId", "phSwitchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"ProfileId":UcsPropertyMeta("ProfileId", "profileId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ProfileName":UcsPropertyMeta("ProfileName", "profileName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"StatusChangeTs":UcsPropertyMeta("StatusChangeTs", "statusChangeTs", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], ["0-4294967295"]),
	"Uuid":UcsPropertyMeta("Uuid", "uuid", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
	"VStatus":UcsPropertyMeta("VStatus", "vStatus", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["offline", "online", "unknown"], ["0-4294967295"]),
	"VcDn":UcsPropertyMeta("VcDn", "vcDn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"VifId":UcsPropertyMeta("VifId", "vifId", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"VmndGuid":UcsPropertyMeta("VmndGuid", "vmndGuid", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
	"VmndName":UcsPropertyMeta("VmndName", "vmndName", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"VnicDn":UcsPropertyMeta("VnicDn", "vnicDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VmNic", "vmNic", "nic-[Name]", _VersionMeta.Version101e, "InputOutput", 0x1fL, [], [u'adaptorEthPortBySizeLargeStats', u'adaptorEthPortBySizeSmallStats', u'adaptorEthPortErrStats', u'adaptorEthPortMcastStats', u'adaptorEthPortOutsizedStats', u'adaptorEthPortStats', u'adaptorFcPortStats', u'adaptorVnicStats', u'fabricEthMonSrcEp', u'fabricFcMonSrcEp', u'faultInst', u'vmVif', u'vmVlan'], ["Get"], ["admin", "read-only"])
}

