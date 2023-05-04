import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"Level":UcsPropertyMeta("Level", "level", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["1", "2", "3", "4", "5", "root"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], ["0-4294967295"]),
	"PermAccess":UcsPropertyMeta("PermAccess", "permAccess", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("OrgOrg", "orgOrg", "org-[Name]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'aaaEpAuthProfile', u'adaptorHostEthIfProfile', u'adaptorHostFcIfProfile', u'adaptorHostIscsiIfProfile', u'biosVProfile', u'cimcvmediaMountConfigPolicy', u'computeAutoconfigPolicy', u'computeBladeDiscPolicy', u'computeBladeInheritPolicy', u'computeChassisConnPolicy', u'computeChassisDiscPolicy', u'computeKvmMgmtPolicy', u'computeMemoryConfigPolicy', u'computePool', u'computePoolingPolicy', u'computePsuPolicy', u'computeQual', u'computeScrubPolicy', u'computeServerDiscPolicy', u'computeServerMgmtPolicy', u'diagRunPolicy', u'epqosDefinition', u'epqosDefinitionDelTask', u'fabricLacpPolicy', u'fabricMulticastPolicy', u'fabricOrgVlanPolicy', u'fabricUdldPolicy', u'fabricVConProfile', u'fabricVlanGroupReq', u'fabricVlanPermit', u'fabricVlanReq', u'faultSuppressTask', u'fcpoolInitiators', u'firmwareAutoSyncPolicy', u'firmwareCatalogPack', u'firmwareComputeHostPack', u'firmwareComputeMgmtPack', u'firmwareInfraPack', u'hostimgPolicy', u'imgprovPolicy', u'imgsecPolicy', u'ippoolPool', u'iqnpoolPool', u'iscsiAuthProfile', u'lsAgentPolicy', u'lsServer', u'lsTier', u'lsbootPolicy', u'lsmaintMaintPolicy', u'macpoolPool', u'mgmtBackupExportExtPolicy', u'mgmtBackupPolicy', u'mgmtCfgExportPolicy', u'nwctrlDefinition', u'orgOrg', u'orgSourceMask', u'powerGroupAdditionPolicy', u'powerMgmtPolicy', u'powerPlacement', u'powerPolicy', u'solPolicy', u'statsThresholdPolicy', u'storageConnectionPolicy', u'storageLocalDiskConfigPolicy', u'sysdebugMEpLogPolicy', u'trigTest', u'uuidpoolPool', u'vmLifeCyclePolicy', u'vnicDynamicConPolicy', u'vnicFcGroupTempl', u'vnicLanConnPolicy', u'vnicLanConnTempl', u'vnicSanConnPolicy', u'vnicSanConnTempl', u'vnicUsnicConPolicy', u'vnicVhbaBehPolicy', u'vnicVmqConPolicy', u'vnicVnicBehPolicy'], ["Add", "Get", "Remove", "Set"], ["admin", "org-management"])
}

