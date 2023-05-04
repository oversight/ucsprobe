import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class NfsMountInstFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"NfsMountInstFsmStage")

	@staticmethod
	def ClassId():
		return "nfsMountInstFsmStage"

	DESCR = "Descr"
	DN = "Dn"
	LAST_UPDATE_TIME = "LastUpdateTime"
	NAME = "Name"
	ORDER = "Order"
	RETRY = "Retry"
	RN = "Rn"
	STAGE_STATUS = "StageStatus"
	STATUS = "Status"

	CONST_LAST_UPDATE_TIME_ = ""
	CONST_NAME_MOUNT_BEGIN = "MountBegin"
	CONST_NAME_MOUNT_FAIL = "MountFail"
	CONST_NAME_MOUNT_MOUNT_LOCAL = "MountMountLocal"
	CONST_NAME_MOUNT_MOUNT_PEER = "MountMountPeer"
	CONST_NAME_MOUNT_REGISTER_CLIENT = "MountRegisterClient"
	CONST_NAME_MOUNT_SUCCESS = "MountSuccess"
	CONST_NAME_MOUNT_VERIFY_REGISTRATION = "MountVerifyRegistration"
	CONST_NAME_UNMOUNT_BEGIN = "UnmountBegin"
	CONST_NAME_UNMOUNT_FAIL = "UnmountFail"
	CONST_NAME_UNMOUNT_SUCCESS = "UnmountSuccess"
	CONST_NAME_UNMOUNT_UNMOUNT_LOCAL = "UnmountUnmountLocal"
	CONST_NAME_UNMOUNT_UNMOUNT_PEER = "UnmountUnmountPeer"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
