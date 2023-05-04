import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FcpoolFormat(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FcpoolFormat")

	@staticmethod
	def ClassId():
		return "fcpoolFormat"

	DN = "Dn"
	FORMAT = "Format"
	MASK = "Mask"
	RN = "Rn"
	STATUS = "Status"

	CONST_MASK_FF_FF_FF_FF_FF_FF_FF_FX = "FF:FF:FF:FF:FF:FF:FF:Fx"
	CONST_MASK_FF_FF_FF_FF_FF_FF_FF_XX = "FF:FF:FF:FF:FF:FF:FF:xx"
	CONST_MASK_FF_FF_FF_FF_FF_FF_FX_XX = "FF:FF:FF:FF:FF:FF:Fx:xx"
	CONST_MASK_FF_FF_FF_FF_FF_FF_XX_XX = "FF:FF:FF:FF:FF:FF:xx:xx"
	CONST_MASK_FF_FF_FF_FF_FF_FX_XX_XX = "FF:FF:FF:FF:FF:Fx:xx:xx"
	CONST_MASK_FF_FF_FF_FF_FF_XX_XX_XX = "FF:FF:FF:FF:FF:xx:xx:xx"
	CONST_MASK_FF_FF_FF_FF_FX_XX_XX_XX = "FF:FF:FF:FF:Fx:xx:xx:xx"
	CONST_MASK_FF_FF_FF_FF_XX_XX_XX_XX = "FF:FF:FF:FF:xx:xx:xx:xx"
	CONST_MASK_FF_FF_FF_FX_XX_XX_XX_XX = "FF:FF:FF:Fx:xx:xx:xx:xx"
	CONST_MASK_FF_FF_FF_XX_XX_XX_XX_XX = "FF:FF:FF:xx:xx:xx:xx:xx"
	CONST_MASK_FF_FF_FX_XX_XX_XX_XX_XX = "FF:FF:Fx:xx:xx:xx:xx:xx"
	CONST_MASK_FF_FF_XX_XX_XX_XX_XX_XX = "FF:FF:xx:xx:xx:xx:xx:xx"
	CONST_MASK_FF_FX_XX_XX_XX_XX_XX_XX = "FF:Fx:xx:xx:xx:xx:xx:xx"
	CONST_MASK_FF_XX_XX_XX_XX_XX_XX_XX = "FF:xx:xx:xx:xx:xx:xx:xx"
	CONST_MASK_FX_XX_XX_XX_XX_XX_XX_XX = "Fx:xx:xx:xx:xx:xx:xx:xx"
