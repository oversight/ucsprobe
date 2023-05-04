import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("TopRoot", "topRoot", "", _VersionMeta.Version101e, "InputOutput", 0xfL, [], [u'aaaLog', u'apeManager', u'callhomeEp', u'capabilityCatalogue', u'clitestTypeTest', u'clitestTypeTest2', u'computeDefaults', u'dhcpInst', u'eventHolder', u'eventLog', u'extpolEp', u'fabricEp', u'faultHolder', u'fcpoolUniverse', u'gmetaEp', u'identMetaVerse', u'ippoolUniverse', u'iqnpoolUniverse', u'macpoolUniverse', u'nfsEp', u'observeObservedCont', u'orgOrg', u'policyPolicyEp', u'procManager', u'statsHolder', u'storageDomainEp', u'syntheticFileSystem', u'topMetaInf', u'topSysDefaults', u'topSystem', u'uuidpoolUniverse', u'vmEp'], ["Get"], ["read-only"])
}

