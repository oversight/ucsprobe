import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Address":UcsPropertyMeta("Address", "address", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CurrentTime":UcsPropertyMeta("CurrentTime", "currentTime", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Ipv6Addr":UcsPropertyMeta("Ipv6Addr", "ipv6Addr", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Mode":UcsPropertyMeta("Mode", "mode", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cluster", "stand-alone", "unspecified"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """[a-zA-Z][a-zA-Z0-9-]{0,29}""", [], ["0-4294967295"]),
	"Owner":UcsPropertyMeta("Owner", "owner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Site":UcsPropertyMeta("Site", "site", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SystemUpTime":UcsPropertyMeta("SystemUpTime", "systemUpTime", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("TopSystem", "topSystem", "sys", _VersionMeta.Version101e, "InputOutput", 0x3ffL, [], [u'aaaAuthRealm', u'aaaLdapEp', u'aaaRadiusEp', u'aaaSessionInfoTable', u'aaaTacacsPlusEp', u'aaaUserEp', u'commSvcEp', u'computeRackUnit', u'domainEnvironmentFeatureCont', u'domainNetworkFeatureCont', u'domainServerFeatureCont', u'domainStorageFeatureCont', u'equipmentChassis', u'equipmentFex', u'extmgmtIfMonPolicy', u'extvmmEp', u'firmwareCatalogue', u'firmwareStatus', u'firmwareSystem', u'firmwareUpgradeInfo', u'fsmStatus', u'initiatorRequestorEp', u'initiatorRequestorGrpEp', u'licenseEp', u'mgmtAccessPolicy', u'mgmtBackup', u'mgmtBackupPolicyConfig', u'mgmtController', u'mgmtEntity', u'mgmtImporter', u'mgmtIntAuthPolicy', u'networkElement', u'pkiEp', u'policyControlEp', u'powerEp', u'swatInjection', u'syntheticDirectory', u'syntheticFsObj', u'sysdebugCoreFileRepository', u'sysdebugEp', u'sysdebugTechSupFileRepository', u'trigLocalSched', u'trigMeta', u'trigSched', u'versionEp'], ["Get", "Set"], ["admin", "ext-lan-config"])
}

