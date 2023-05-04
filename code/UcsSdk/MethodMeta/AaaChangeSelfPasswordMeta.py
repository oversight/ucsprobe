import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsFactoryMeta, UcsFactoryMethodMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Cookie":UcsFactoryMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
	"InConfirmNewPassword":UcsFactoryMeta("InConfirmNewPassword", "inConfirmNewPassword", "Xs:string", "Version142b", "Input", False),
	"InNewPassword":UcsFactoryMeta("InNewPassword", "inNewPassword", "Xs:string", "Version142b", "Input", False),
	"InOldPassword":UcsFactoryMeta("InOldPassword", "inOldPassword", "Xs:string", "Version142b", "Input", False),
	"InUserName":UcsFactoryMeta("InUserName", "inUserName", "Xs:string", "Version142b", "Input", False),
	"OutStatus":UcsFactoryMeta("OutStatus", "outStatus", "Xs:string", "Version142b", "Output", False),
	"Meta":UcsFactoryMethodMeta("AaaChangeSelfPassword","aaaChangeSelfPassword", "Version142b")
}

