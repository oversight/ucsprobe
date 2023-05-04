import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Addr":UcsPropertyMeta("Addr", "addr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, 1, 255, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Contact":UcsPropertyMeta("Contact", "contact", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[^<>""'&]*""", [], ["0-4294967295"]),
	"Contract":UcsPropertyMeta("Contract", "contract", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, 1, 64, None, [], ["0-4294967295"]),
	"Customer":UcsPropertyMeta("Customer", "customer", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Email":UcsPropertyMeta("Email", "email", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-4294967295"]),
	"From":UcsPropertyMeta("From", "from", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-4294967295"]),
	"Phone":UcsPropertyMeta("Phone", "phone", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["0-4294967295"]),
	"ReplyTo":UcsPropertyMeta("ReplyTo", "replyTo", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Site":UcsPropertyMeta("Site", "site", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Urgency":UcsPropertyMeta("Urgency", "urgency", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, ["alert", "critical", "debug", "emergency", "error", "info", "notice", "warning"], ["0-4294967295"]),
	"Meta":UcsMoMeta("CallhomeSource", "callhomeSource", "source", _VersionMeta.Version101e, "InputOutput", 0x3fffL, [], [], ["Get", "Set"], ["admin", "operations"])
}

