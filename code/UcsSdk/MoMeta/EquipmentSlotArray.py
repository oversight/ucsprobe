import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentSlotArray(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentSlotArray")

	@staticmethod
	def ClassId():
		return "equipmentSlotArray"

	DESCR = "Descr"
	DN = "Dn"
	FIRST_INDEX = "FirstIndex"
	HEIGHT = "Height"
	HORIZONTAL_START_OFFSET = "HorizontalStartOffset"
	INLINE_GROUP_SEPARATION = "InlineGroupSeparation"
	INLINE_GROUP_SIZE = "InlineGroupSize"
	INLINE_OFFSET = "InlineOffset"
	LOCATION = "Location"
	NAME = "Name"
	NUMBER_OF_SLOTS = "NumberOfSlots"
	ORIENTATION = "Orientation"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SELECTOR = "Selector"
	SLOTS_PER_LINE = "SlotsPerLine"
	STATUS = "Status"
	TRANSVERSE_GROUP_SEPARATION = "TransverseGroupSeparation"
	TRANSVERSE_GROUP_SIZE = "TransverseGroupSize"
	TRANSVERSE_OFFSET = "TransverseOffset"
	VERTICAL_START_OFFSET = "VerticalStartOffset"
	WIDTH = "Width"

	CONST_HEIGHT_NOT_APPLICABLE = "not-applicable"
	CONST_HORIZONTAL_START_OFFSET_NOT_APPLICABLE = "not-applicable"
	CONST_INLINE_GROUP_SEPARATION_NOT_APPLICABLE = "not-applicable"
	CONST_INLINE_OFFSET_NOT_APPLICABLE = "not-applicable"
	CONST_INT_ID_NONE = "none"
	CONST_LOCATION_BACK = "back"
	CONST_LOCATION_BOTTOM = "bottom"
	CONST_LOCATION_FRONT = "front"
	CONST_LOCATION_LEFT = "left"
	CONST_LOCATION_RIGHT = "right"
	CONST_LOCATION_TOP = "top"
	CONST_LOCATION_UNKNOWN = "unknown"
	CONST_ORIENTATION_HORIZONTAL = "horizontal"
	CONST_ORIENTATION_UNKNOWN = "unknown"
	CONST_ORIENTATION_VERTICAL = "vertical"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SELECTOR_BLADE = "blade"
	CONST_SELECTOR_COM_PORT = "com_port"
	CONST_SELECTOR_DISK_SLOT = "disk_slot"
	CONST_SELECTOR_DRIVE_SLOT = "drive_slot"
	CONST_SELECTOR_DVI_PORT = "dvi_port"
	CONST_SELECTOR_ETHERNET_PORT = "ethernet_port"
	CONST_SELECTOR_FAN = "fan"
	CONST_SELECTOR_GEM = "gem"
	CONST_SELECTOR_IOCARD = "iocard"
	CONST_SELECTOR_KEYBOARD_PORT = "keyboard_port"
	CONST_SELECTOR_MOUSE_PORT = "mouse_port"
	CONST_SELECTOR_PAR_PORT = "par_port"
	CONST_SELECTOR_PSU = "psu"
	CONST_SELECTOR_UNKNOWN = "unknown"
	CONST_SELECTOR_USB_PORT = "usb_port"
	CONST_SELECTOR_VGA_PORT = "vga_port"
	CONST_TRANSVERSE_GROUP_SEPARATION_NOT_APPLICABLE = "not-applicable"
	CONST_TRANSVERSE_OFFSET_NOT_APPLICABLE = "not-applicable"
	CONST_VERTICAL_START_OFFSET_NOT_APPLICABLE = "not-applicable"
	CONST_WIDTH_NOT_APPLICABLE = "not-applicable"