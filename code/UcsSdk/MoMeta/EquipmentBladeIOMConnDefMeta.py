import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version203a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version203a, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"IocardType":UcsPropertyMeta("IocardType", "iocardType", "string", _VersionMeta.Version203a, UcsPropertyMeta.Naming, 0x8L, 1, 510, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"PortBandwidth":UcsPropertyMeta("PortBandwidth", "portBandwidth", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["10gbps", "1gbps", "20gbps", "40gbps", "indeterminate"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version203a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentBladeIOMConnDef", "equipmentBladeIOMConnDef", "-iom-type-[IocardType]", _VersionMeta.Version203a, "InputOutput", 0xffL, [], [u'equipmentAdaptorConnDef'], ["Get"], [""])
}

