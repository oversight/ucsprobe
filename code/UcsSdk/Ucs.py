
# Copyright 2013 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is an auto-generated module.
It contains supporting classes for Filter and External Method.

ClassFactory Method: It returns the object of type ManagedObject, ExternalMethod
or supporting classes available in this module for a given className.
"""

try:
	import xml.etree.cElementTree as ET
	from xml.etree.cElementTree import Element, SubElement
except ImportError:
	import cElementTree as ET
	from cElementTree import Element, SubElement
from UcsBase import *
import UcsMeta

def BaseObject(name):
	if (name == "Method"):
		return Method()
	elif (name == "MethodSet"):
		return MethodSet()
	elif (name == "AllbitsFilter"):
		return AllbitsFilter()
	elif (name == "AndFilter"):
		return AndFilter()
	elif (name == "AnybitFilter"):
		return AnybitFilter()
	elif (name == "BwFilter"):
		return BwFilter()
	elif (name == "ClassId"):
		return ClassId()
	elif (name == "ClassIdSet"):
		return ClassIdSet()
	elif (name == "ConfigConfig"):
		return ConfigConfig()
	elif (name == "ConfigMap"):
		return ConfigMap()
	elif (name == "ConfigSet"):
		return ConfigSet()
	elif (name == "Dn"):
		return Dn()
	elif (name == "DnSet"):
		return DnSet()
	elif (name == "EqFilter"):
		return EqFilter()
	elif (name == "FilterFilter"):
		return FilterFilter()
	elif (name == "GeFilter"):
		return GeFilter()
	elif (name == "GtFilter"):
		return GtFilter()
	elif (name == "Id"):
		return Id()
	elif (name == "IdSet"):
		return IdSet()
	elif (name == "LeFilter"):
		return LeFilter()
	elif (name == "LtFilter"):
		return LtFilter()
	elif (name == "NeFilter"):
		return NeFilter()
	elif (name == "NotFilter"):
		return NotFilter()
	elif (name == "OrFilter"):
		return OrFilter()
	elif (name == "Pair"):
		return Pair()
	elif (name == "WcardFilter"):
		return WcardFilter()
	else:
		return ManagedObject(UcsUtils.WordL(name))

def ClassFactory(name):
	from UcsBase import UcsUtils
	if name in dir(UcsMeta.MoClassId):
		return ManagedObject(name)
	elif name in dir(UcsMeta.MethodClassId):
		return ExternalMethod(name)
	else:
		return BaseObject(UcsUtils.WordU(name))

class Method(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Method")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the Method object."""
		if w is None:
			x=Element("method")
		else:
			if (elementName == None):
				x = SubElement(w,"method")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the Method object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the Method object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the Method object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"aaaChangeSelfPassword",
					"aaaCheckComputeAuthToken",
					"aaaCheckComputeExtAccess",
					"aaaGetAuthTokenClient",
					"aaaGetKVMLaunchUrl",
					"aaaGetNComputeAuthTokenByDn",
					"aaaKeepAlive",
					"aaaLogin",
					"aaaLogout",
					"aaaRefresh",
					"aaaTokenLogin",
					"aaaTokenRefresh",
					"apeBootPnuOs",
					"apeConfigureCMCLIF",
					"apeCreateHVVnic",
					"apeCreateSfish",
					"apeCreateVMVnic",
					"apeDeleteHVVnic",
					"apeDeleteSfish",
					"apeDeleteVMVnic",
					"apeGetAdaptorConnectivity",
					"apeGetPnuOSInventory",
					"apeGetSwitchApeFru",
					"apeInjectStimuli",
					"apeInsertNewChassis",
					"apeInsertNewFex",
					"apeInsertNewRack",
					"apeIssueAdaptorId",
					"apeIssueChassisId",
					"apeIssueFexId",
					"apeIssueRackId",
					"apeMcGet",
					"apeMcGetBiosTokens",
					"apeMcGetParam",
					"apeMcGetSmbios",
					"apeMcSet",
					"apeMuxOffline",
					"apeSetAdaptorFirmwareVersion",
					"apeSetApeSensorReading",
					"apeSetFlexFlashControllerFirmwareVersion",
					"apeSetFlexFlashControllerState",
					"apeSetFlexFlashVirtualRaidInformation",
					"apeSetServerLifeCycle",
					"apeSetSwitchInventory",
					"apeSetVmediaMounts",
					"apeUpdateApeFirmwareParamTable",
					"apeUpdateBIOSFirmwareVersion",
					"apeUpdateStorageCtlrFirmwareVersion",
					"computeGetInventory",
					"configCheckCompatibility",
					"configCheckConformance",
					"configCheckFirmwareUpdatable",
					"configConfFiltered",
					"configConfMo",
					"configConfMoGroup",
					"configConfMos",
					"configConfRename",
					"configEstimateImpact",
					"configFindDependencies",
					"configFindDnsByClassId",
					"configFindHostPackDependencies",
					"configFindPermitted",
					"configGetEstimateImpact",
					"configGetRemotePolicies",
					"configGetXmlFile",
					"configGetXmlFileStr",
					"configInstallAllImpact",
					"configMoChangeEvent",
					"configRefreshIdentity",
					"configReleaseResolveContext",
					"configRenewResolveContext",
					"configResolveChildren",
					"configResolveChildrenSorted",
					"configResolveClass",
					"configResolveClassSorted",
					"configResolveClasses",
					"configResolveClassesSorted",
					"configResolveContext",
					"configResolveDn",
					"configResolveDns",
					"configResolveParent",
					"configScope",
					"eventRegisterEventChannel",
					"eventRegisterEventChannelResp",
					"eventSendEvent",
					"eventSendHeartbeat",
					"eventSubscribe",
					"eventUnRegisterEventChannel",
					"eventUnsubscribe",
					"externalMethod",
					"faultAckFault",
					"faultAckFaults",
					"faultResolveFault",
					"fsmDebugAction",
					"loggingSyncOcns",
					"lsClone",
					"lsInstantiateNNamedTemplate",
					"lsInstantiateNTemplate",
					"lsInstantiateTemplate",
					"lsResolveTemplates",
					"lsTemplatise",
					"methodVessel",
					"mgmtResolveBackupFilenames",
					"orgResolveElements",
					"orgResolveLogicalParents",
					"policyResolveNames",
					"policySetCentraleStorage",
					"poolResolveInScope",
					"statsClearInterval",
					"statsResolveThresholdPolicy",
					"statsSubscribe",
					"swatExample",
					"swatGetstats",
					"swatInject",
					"syntheticFSObjInventory",
					"syntheticFSObjInventoryB",
					"syntheticTestTx",
					"trigPerformTokenAction",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class MethodSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "MethodSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the MethodSet object."""
		if w is None:
			x=Element("methodSet")
		else:
			if (elementName == None):
				x = SubElement(w,"methodSet")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the MethodSet object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the MethodSet object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the MethodSet object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"aaaChangeSelfPassword",
					"aaaCheckComputeAuthToken",
					"aaaCheckComputeExtAccess",
					"aaaGetAuthTokenClient",
					"aaaGetKVMLaunchUrl",
					"aaaGetNComputeAuthTokenByDn",
					"aaaKeepAlive",
					"aaaLogin",
					"aaaLogout",
					"aaaRefresh",
					"aaaTokenLogin",
					"aaaTokenRefresh",
					"apeBootPnuOs",
					"apeConfigureCMCLIF",
					"apeCreateHVVnic",
					"apeCreateSfish",
					"apeCreateVMVnic",
					"apeDeleteHVVnic",
					"apeDeleteSfish",
					"apeDeleteVMVnic",
					"apeGetAdaptorConnectivity",
					"apeGetPnuOSInventory",
					"apeGetSwitchApeFru",
					"apeInjectStimuli",
					"apeInsertNewChassis",
					"apeInsertNewFex",
					"apeInsertNewRack",
					"apeIssueAdaptorId",
					"apeIssueChassisId",
					"apeIssueFexId",
					"apeIssueRackId",
					"apeMcGet",
					"apeMcGetBiosTokens",
					"apeMcGetParam",
					"apeMcGetSmbios",
					"apeMcSet",
					"apeMuxOffline",
					"apeSetAdaptorFirmwareVersion",
					"apeSetApeSensorReading",
					"apeSetFlexFlashControllerFirmwareVersion",
					"apeSetFlexFlashControllerState",
					"apeSetFlexFlashVirtualRaidInformation",
					"apeSetServerLifeCycle",
					"apeSetSwitchInventory",
					"apeSetVmediaMounts",
					"apeUpdateApeFirmwareParamTable",
					"apeUpdateBIOSFirmwareVersion",
					"apeUpdateStorageCtlrFirmwareVersion",
					"computeGetInventory",
					"configCheckCompatibility",
					"configCheckConformance",
					"configCheckFirmwareUpdatable",
					"configConfFiltered",
					"configConfMo",
					"configConfMoGroup",
					"configConfMos",
					"configConfRename",
					"configEstimateImpact",
					"configFindDependencies",
					"configFindDnsByClassId",
					"configFindHostPackDependencies",
					"configFindPermitted",
					"configGetEstimateImpact",
					"configGetRemotePolicies",
					"configGetXmlFile",
					"configGetXmlFileStr",
					"configInstallAllImpact",
					"configMoChangeEvent",
					"configRefreshIdentity",
					"configReleaseResolveContext",
					"configRenewResolveContext",
					"configResolveChildren",
					"configResolveChildrenSorted",
					"configResolveClass",
					"configResolveClassSorted",
					"configResolveClasses",
					"configResolveClassesSorted",
					"configResolveContext",
					"configResolveDn",
					"configResolveDns",
					"configResolveParent",
					"configScope",
					"eventRegisterEventChannel",
					"eventRegisterEventChannelResp",
					"eventSendEvent",
					"eventSendHeartbeat",
					"eventSubscribe",
					"eventUnRegisterEventChannel",
					"eventUnsubscribe",
					"externalMethod",
					"faultAckFault",
					"faultAckFaults",
					"faultResolveFault",
					"fsmDebugAction",
					"loggingSyncOcns",
					"lsClone",
					"lsInstantiateNNamedTemplate",
					"lsInstantiateNTemplate",
					"lsInstantiateTemplate",
					"lsResolveTemplates",
					"lsTemplatise",
					"methodVessel",
					"mgmtResolveBackupFilenames",
					"orgResolveElements",
					"orgResolveLogicalParents",
					"policyResolveNames",
					"policySetCentraleStorage",
					"poolResolveInScope",
					"statsClearInterval",
					"statsResolveThresholdPolicy",
					"statsSubscribe",
					"swatExample",
					"swatGetstats",
					"swatInject",
					"syntheticFSObjInventory",
					"syntheticFSObjInventoryB",
					"syntheticTestTx",
					"trigPerformTokenAction",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class AllbitsFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "AllbitsFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the AllbitsFilter object."""
		if w is None:
			x=Element("allbits")
		else:
			if (elementName == None):
				x = SubElement(w,"allbits")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the AllbitsFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the AllbitsFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the AllbitsFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class AndFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "AndFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the AndFilter object."""
		if w is None:
			x=Element("and")
		else:
			if (elementName == None):
				x = SubElement(w,"and")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the AndFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the AndFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the AndFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class AnybitFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "AnybitFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the AnybitFilter object."""
		if w is None:
			x=Element("anybit")
		else:
			if (elementName == None):
				x = SubElement(w,"anybit")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the AnybitFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the AnybitFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the AnybitFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class BwFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "BwFilter")
		self.Class = None
		self.FirstValue = None
		self.Property = None
		self.SecondValue = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the BwFilter object."""
		if w is None:
			x=Element("bw")
		else:
			if (elementName == None):
				x = SubElement(w,"bw")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("firstValue", getattr(self,"FirstValue"));
		x.set("property", getattr(self,"Property"));
		x.set("secondValue", getattr(self,"SecondValue"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the BwFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the BwFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the BwFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class ClassId(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ClassId")
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the ClassId object."""
		if w is None:
			x=Element("classId")
		else:
			if (elementName == None):
				x = SubElement(w,"classId")
			else:
				x = SubElement(w,elementName)
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the ClassId object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the ClassId object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the ClassId object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class ClassIdSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ClassIdSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the ClassIdSet object."""
		if w is None:
			x=Element("classIdSet")
		else:
			if (elementName == None):
				x = SubElement(w,"classIdSet")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the ClassIdSet object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the ClassIdSet object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the ClassIdSet object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"classId",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class ConfigConfig(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ConfigConfig")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the ConfigConfig object."""
		if w is None:
			x=Element("configConfig")
		else:
			if (elementName == None):
				x = SubElement(w,"configConfig")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the ConfigConfig object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the ConfigConfig object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the ConfigConfig object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"aaaAuthRealm",
					"aaaAuthRealmFsm",
					"aaaAuthRealmFsmStage",
					"aaaCimcSession",
					"aaaConsoleAuth",
					"aaaDefaultAuth",
					"aaaDomain",
					"aaaDomainAuth",
					"aaaEpAuthProfile",
					"aaaEpFsm",
					"aaaEpFsmStage",
					"aaaEpFsmTask",
					"aaaEpLogin",
					"aaaEpUser",
					"aaaExtMgmtCutThruTkn",
					"aaaLdapEp",
					"aaaLdapEpFsm",
					"aaaLdapEpFsmStage",
					"aaaLdapGroup",
					"aaaLdapGroupRule",
					"aaaLdapProvider",
					"aaaLocale",
					"aaaLog",
					"aaaModLR",
					"aaaOrg",
					"aaaPreLoginBanner",
					"aaaProviderGroup",
					"aaaProviderRef",
					"aaaPwdProfile",
					"aaaRadiusEp",
					"aaaRadiusEpFsm",
					"aaaRadiusEpFsmStage",
					"aaaRadiusProvider",
					"aaaRealmFsm",
					"aaaRealmFsmStage",
					"aaaRealmFsmTask",
					"aaaRemoteUser",
					"aaaRole",
					"aaaSession",
					"aaaSessionInfo",
					"aaaSessionInfoTable",
					"aaaSessionLR",
					"aaaShellLogin",
					"aaaSshAuth",
					"aaaTacacsPlusEp",
					"aaaTacacsPlusEpFsm",
					"aaaTacacsPlusEpFsmStage",
					"aaaTacacsPlusProvider",
					"aaaUser",
					"aaaUserData",
					"aaaUserEp",
					"aaaUserEpFsm",
					"aaaUserEpFsmStage",
					"aaaUserEpFsmTask",
					"aaaUserLocale",
					"aaaUserRole",
					"aaaWebLogin",
					"adaptorCapQual",
					"adaptorCapSpec",
					"adaptorDiagCap",
					"adaptorEthArfsProfile",
					"adaptorEthCompQueueProfile",
					"adaptorEthFailoverProfile",
					"adaptorEthInterruptProfile",
					"adaptorEthOffloadProfile",
					"adaptorEthPortBySizeLargeStats",
					"adaptorEthPortBySizeLargeStatsHist",
					"adaptorEthPortBySizeSmallStats",
					"adaptorEthPortBySizeSmallStatsHist",
					"adaptorEthPortErrStats",
					"adaptorEthPortErrStatsHist",
					"adaptorEthPortMcastStats",
					"adaptorEthPortMcastStatsHist",
					"adaptorEthPortOutsizedStats",
					"adaptorEthPortOutsizedStatsHist",
					"adaptorEthPortStats",
					"adaptorEthPortStatsHist",
					"adaptorEthRecvQueueProfile",
					"adaptorEthWorkQueueProfile",
					"adaptorEtherIfStats",
					"adaptorEtherIfStatsHist",
					"adaptorExtEthIf",
					"adaptorExtEthIfFsm",
					"adaptorExtEthIfFsmStage",
					"adaptorExtEthIfFsmTask",
					"adaptorExtEthIfPc",
					"adaptorExtEthIfPcEp",
					"adaptorExtIpV6RssHashProfile",
					"adaptorFamilyTypeDef",
					"adaptorFcCdbWorkQueueProfile",
					"adaptorFcErrorRecoveryProfile",
					"adaptorFcIfEventStats",
					"adaptorFcIfEventStatsHist",
					"adaptorFcIfFC4Stats",
					"adaptorFcIfFC4StatsHist",
					"adaptorFcIfFrameStats",
					"adaptorFcIfFrameStatsHist",
					"adaptorFcInterruptProfile",
					"adaptorFcOEIf",
					"adaptorFcPortFLogiProfile",
					"adaptorFcPortPLogiProfile",
					"adaptorFcPortProfile",
					"adaptorFcPortStats",
					"adaptorFcPortStatsHist",
					"adaptorFcRecvQueueProfile",
					"adaptorFcWorkQueueProfile",
					"adaptorFruCapProvider",
					"adaptorFruCapRef",
					"adaptorFwCapProvider",
					"adaptorHostEthIf",
					"adaptorHostEthIfFsm",
					"adaptorHostEthIfFsmStage",
					"adaptorHostEthIfFsmTask",
					"adaptorHostEthIfProfile",
					"adaptorHostFcIf",
					"adaptorHostFcIfFsm",
					"adaptorHostFcIfFsmStage",
					"adaptorHostFcIfFsmTask",
					"adaptorHostFcIfProfile",
					"adaptorHostIscsiIf",
					"adaptorHostIscsiIfProfile",
					"adaptorHostMgmtCap",
					"adaptorHostServiceEthIf",
					"adaptorHostethHwAddrCap",
					"adaptorHostfcHwAddrCap",
					"adaptorIScsiCap",
					"adaptorIpV4RssHashProfile",
					"adaptorIpV6RssHashProfile",
					"adaptorIscsiAuth",
					"adaptorIscsiProt",
					"adaptorIscsiTargetIf",
					"adaptorLanCap",
					"adaptorLldpCap",
					"adaptorMenloBaseErrorStats",
					"adaptorMenloBaseErrorStatsHist",
					"adaptorMenloDcePortStats",
					"adaptorMenloDcePortStatsHist",
					"adaptorMenloEthErrorStats",
					"adaptorMenloEthErrorStatsHist",
					"adaptorMenloEthStats",
					"adaptorMenloEthStatsHist",
					"adaptorMenloFcErrorStats",
					"adaptorMenloFcErrorStatsHist",
					"adaptorMenloFcStats",
					"adaptorMenloFcStatsHist",
					"adaptorMenloHostPortStats",
					"adaptorMenloHostPortStatsHist",
					"adaptorMenloMcpuErrorStats",
					"adaptorMenloMcpuErrorStatsHist",
					"adaptorMenloMcpuStats",
					"adaptorMenloMcpuStatsHist",
					"adaptorMenloNetEgStats",
					"adaptorMenloNetEgStatsHist",
					"adaptorMenloNetInStats",
					"adaptorMenloNetInStatsHist",
					"adaptorMenloQErrorStats",
					"adaptorMenloQErrorStatsHist",
					"adaptorMenloQStats",
					"adaptorMenloQStatsHist",
					"adaptorNwMgmtCap",
					"adaptorProtocolProfile",
					"adaptorQual",
					"adaptorRssProfile",
					"adaptorSanCap",
					"adaptorUnit",
					"adaptorUnitAssocCtx",
					"adaptorUnitExtn",
					"adaptorUplinkHwAddrCap",
					"adaptorUsnicConnDef",
					"adaptorVlan",
					"adaptorVnicStats",
					"adaptorVnicStatsHist",
					"adaptorVsan",
					"apeControllerChassis",
					"apeControllerEeprom",
					"apeControllerManager",
					"apeDcosAgManager",
					"apeFru",
					"apeHostAgent",
					"apeLANBoot",
					"apeLocalDiskBoot",
					"apeManager",
					"apeMc",
					"apeMcTable",
					"apeMenlo",
					"apeMenloVnic",
					"apeMenloVnicStats",
					"apeNicAgManager",
					"apePalo",
					"apePaloVnic",
					"apePaloVnicStats",
					"apeParam",
					"apeReading",
					"apeSANBoot",
					"apeSdr",
					"apeSwitchFirmwareInv",
					"apeVirtualMediaBoot",
					"biosBOT",
					"biosBootDev",
					"biosBootDevGrp",
					"biosFeatureRef",
					"biosParameterRef",
					"biosRef",
					"biosSettingRef",
					"biosSettings",
					"biosUnit",
					"biosVIdentityParams",
					"biosVProfile",
					"biosVfACPI10Support",
					"biosVfAllUSBDevices",
					"biosVfAssertNMIOnPERR",
					"biosVfAssertNMIOnSERR",
					"biosVfBootOptionRetry",
					"biosVfCPUPerformance",
					"biosVfConsoleRedirection",
					"biosVfCoreMultiProcessing",
					"biosVfDRAMClockThrottling",
					"biosVfDirectCacheAccess",
					"biosVfDramRefreshRate",
					"biosVfEnhancedIntelSpeedStepTech",
					"biosVfExecuteDisableBit",
					"biosVfFRB2Timer",
					"biosVfFrequencyFloorOverride",
					"biosVfFrontPanelLockout",
					"biosVfIntelEntrySASRAIDModule",
					"biosVfIntelHyperThreadingTech",
					"biosVfIntelTurboBoostTech",
					"biosVfIntelVTForDirectedIO",
					"biosVfIntelVirtualizationTechnology",
					"biosVfInterleaveConfiguration",
					"biosVfLOMPortsConfiguration",
					"biosVfLocalX2Apic",
					"biosVfLvDIMMSupport",
					"biosVfMaxVariableMTRRSetting",
					"biosVfMaximumMemoryBelow4GB",
					"biosVfMemoryMappedIOAbove4GB",
					"biosVfMirroringMode",
					"biosVfNUMAOptimized",
					"biosVfOSBootWatchdogTimer",
					"biosVfOSBootWatchdogTimerPolicy",
					"biosVfOSBootWatchdogTimerTimeout",
					"biosVfOnboardSATAController",
					"biosVfOnboardStorage",
					"biosVfOptionROMEnable",
					"biosVfOptionROMLoad",
					"biosVfPCISlotLinkSpeed",
					"biosVfPCISlotOptionROMEnable",
					"biosVfPOSTErrorPause",
					"biosVfPSTATECoordination",
					"biosVfPackageCStateLimit",
					"biosVfProcessorC1E",
					"biosVfProcessorC3Report",
					"biosVfProcessorC6Report",
					"biosVfProcessorC7Report",
					"biosVfProcessorCState",
					"biosVfProcessorEnergyConfiguration",
					"biosVfProcessorPrefetchConfig",
					"biosVfQPILinkFrequencySelect",
					"biosVfQuietBoot",
					"biosVfResumeOnACPowerLoss",
					"biosVfScrubPolicies",
					"biosVfSelectMemoryRASConfiguration",
					"biosVfSerialPortAEnable",
					"biosVfSparingMode",
					"biosVfSriovConfig",
					"biosVfUCSMBootModeControl",
					"biosVfUCSMBootOrderRuleControl",
					"biosVfUEFIOSUseLegacyVideo",
					"biosVfUSBBootConfig",
					"biosVfUSBFrontPanelAccessLock",
					"biosVfUSBPortConfiguration",
					"biosVfUSBSystemIdlePowerOptimizingSetting",
					"biosVfVGAPriority",
					"bmcSELCounter",
					"callhomeDest",
					"callhomeEp",
					"callhomeEpFsm",
					"callhomeEpFsmStage",
					"callhomeEpFsmTask",
					"callhomePeriodicSystemInventory",
					"callhomePolicy",
					"callhomeProfile",
					"callhomeSmtp",
					"callhomeSource",
					"callhomeTestAlert",
					"capabilityCatalogue",
					"capabilityCatalogueFsm",
					"capabilityCatalogueFsmStage",
					"capabilityCatalogueFsmTask",
					"capabilityEp",
					"capabilityFeatureLimits",
					"capabilityMgmtExtension",
					"capabilityMgmtExtensionFsm",
					"capabilityMgmtExtensionFsmStage",
					"capabilityMgmtExtensionFsmTask",
					"capabilityNetworkLimits",
					"capabilityStorageLimits",
					"capabilitySystemLimits",
					"capabilityUpdate",
					"capabilityUpdater",
					"capabilityUpdaterFsm",
					"capabilityUpdaterFsmStage",
					"capabilityUpdaterFsmTask",
					"changeChangedObjectRef",
					"cimcvmediaActualMountEntry",
					"cimcvmediaActualMountList",
					"cimcvmediaConfigMountEntry",
					"cimcvmediaExtMgmtRuleEntry",
					"cimcvmediaMountConfigDef",
					"cimcvmediaMountConfigPolicy",
					"clitestTypeTest",
					"clitestTypeTest2",
					"clitestTypeTestChild",
					"commCimcWebService",
					"commCimxml",
					"commDateTime",
					"commDns",
					"commDnsProvider",
					"commEvtChannel",
					"commHttp",
					"commHttps",
					"commNtpProvider",
					"commShellSvcLimits",
					"commSmashCLP",
					"commSnmp",
					"commSnmpTrap",
					"commSnmpUser",
					"commSsh",
					"commSvcEp",
					"commSvcEpFsm",
					"commSvcEpFsmStage",
					"commSvcEpFsmTask",
					"commSyslog",
					"commSyslogClient",
					"commSyslogConsole",
					"commSyslogFile",
					"commSyslogMonitor",
					"commSyslogSource",
					"commTelnet",
					"commWebChannel",
					"commWebSvcLimits",
					"commWsman",
					"commXmlClConnPolicy",
					"computeAutoconfigPolicy",
					"computeBlade",
					"computeBladeDiscPolicy",
					"computeBladeFsm",
					"computeBladeFsmStage",
					"computeBladeFsmTask",
					"computeBladeInheritPolicy",
					"computeBoard",
					"computeBoardConnector",
					"computeBoardController",
					"computeChassisConnPolicy",
					"computeChassisDiscPolicy",
					"computeChassisQual",
					"computeDefaults",
					"computeExtBoard",
					"computeFwSyncAck",
					"computeHealthLedSensorAlarm",
					"computeIOHub",
					"computeIOHubEnvStats",
					"computeIOHubEnvStatsHist",
					"computeKvmMgmtPolicy",
					"computeMbPowerStats",
					"computeMbPowerStatsHist",
					"computeMbTempStats",
					"computeMbTempStatsHist",
					"computeMemoryConfigPolicy",
					"computeMemoryConfiguration",
					"computeMemoryUnitConstraintDef",
					"computePCIeFatalCompletionStats",
					"computePCIeFatalProtocolStats",
					"computePCIeFatalReceiveStats",
					"computePCIeFatalStats",
					"computePciCap",
					"computePciSlotScanDef",
					"computePhysicalAssocCtx",
					"computePhysicalFsm",
					"computePhysicalFsmStage",
					"computePhysicalFsmTask",
					"computePhysicalQual",
					"computePlatform",
					"computePnuOSImage",
					"computePool",
					"computePoolPolicyRef",
					"computePoolable",
					"computePooledRackUnit",
					"computePooledSlot",
					"computePoolingPolicy",
					"computePsuControl",
					"computePsuPolicy",
					"computeQual",
					"computeRackQual",
					"computeRackUnit",
					"computeRackUnitFsm",
					"computeRackUnitFsmStage",
					"computeRackUnitFsmTask",
					"computeRackUnitMbTempStats",
					"computeRackUnitMbTempStatsHist",
					"computeRtcBattery",
					"computeScrubPolicy",
					"computeServerDiscPolicy",
					"computeServerDiscPolicyFsm",
					"computeServerDiscPolicyFsmStage",
					"computeServerDiscPolicyFsmTask",
					"computeServerMgmtPolicy",
					"computeSlotQual",
					"configImpact",
					"configManagedEpImpactResponse",
					"configSorter",
					"dcxFcoeVifEp",
					"dcxNs",
					"dcxUniverse",
					"dcxVIf",
					"dcxVc",
					"dcxVifEp",
					"dhcpAcquired",
					"dhcpInst",
					"dhcpLease",
					"diagBladeTest",
					"diagNetworkTest",
					"diagRslt",
					"diagRunPolicy",
					"diagSrvCapProvider",
					"diagSrvCtrl",
					"domainEnvironmentFeature",
					"domainEnvironmentFeatureCont",
					"domainEnvironmentParam",
					"domainNetworkFeature",
					"domainNetworkFeatureCont",
					"domainNetworkParam",
					"domainServerFeature",
					"domainServerFeatureCont",
					"domainServerParam",
					"domainStorageFeature",
					"domainStorageFeatureCont",
					"domainStorageParam",
					"dpsecMac",
					"epqosDefinition",
					"epqosDefinitionDelTask",
					"epqosDefinitionDelTaskFsm",
					"epqosDefinitionDelTaskFsmStage",
					"epqosDefinitionDelTaskFsmTask",
					"epqosDefinitionFsm",
					"epqosDefinitionFsmStage",
					"epqosDefinitionFsmTask",
					"epqosEgress",
					"equipmentAdaptorConnDef",
					"equipmentAdaptorDef",
					"equipmentAdvancedBootOrder",
					"equipmentBaseBoardCapProvider",
					"equipmentBeaconCapProvider",
					"equipmentBeaconLed",
					"equipmentBeaconLedFsm",
					"equipmentBeaconLedFsmStage",
					"equipmentBeaconLedFsmTask",
					"equipmentBiosDef",
					"equipmentBladeAGLibrary",
					"equipmentBladeAggregationCapRef",
					"equipmentBladeBiosCapProvider",
					"equipmentBladeCapProvider",
					"equipmentBladeConnDef",
					"equipmentBladeIOMConnDef",
					"equipmentBoardControllerDef",
					"equipmentCatalogCapProvider",
					"equipmentChassis",
					"equipmentChassisCapProvider",
					"equipmentChassisFsm",
					"equipmentChassisFsmStage",
					"equipmentChassisFsmTask",
					"equipmentChassisStats",
					"equipmentChassisStatsHist",
					"equipmentCimcVmedia",
					"equipmentDbgPluginCapProvider",
					"equipmentDimmEntry",
					"equipmentDimmMapping",
					"equipmentDiscoveryCap",
					"equipmentDowngradeConstraint",
					"equipmentFan",
					"equipmentFanModule",
					"equipmentFanModuleCapProvider",
					"equipmentFanModuleDef",
					"equipmentFanModuleStats",
					"equipmentFanModuleStatsHist",
					"equipmentFanStats",
					"equipmentFanStatsHist",
					"equipmentFex",
					"equipmentFexCapProvider",
					"equipmentFexEnvStats",
					"equipmentFexEnvStatsHist",
					"equipmentFexFsm",
					"equipmentFexFsmStage",
					"equipmentFexFsmTask",
					"equipmentFexPowerSummary",
					"equipmentFexPowerSummaryHist",
					"equipmentFexPsuInputStats",
					"equipmentFexPsuInputStatsHist",
					"equipmentFirmwareConstraint",
					"equipmentFlashLife",
					"equipmentGemCapProvider",
					"equipmentGemPortCap",
					"equipmentGraphicsCardCapProvider",
					"equipmentGraphicsCardCapRef",
					"equipmentHDDFaultMonDef",
					"equipmentHealthLed",
					"equipmentHostIfCapProvider",
					"equipmentIOCard",
					"equipmentIOCardCapProvider",
					"equipmentIOCardFsm",
					"equipmentIOCardFsmStage",
					"equipmentIOCardFsmTask",
					"equipmentIOCardStats",
					"equipmentIOCardStatsHist",
					"equipmentIOCardTypeDef",
					"equipmentInbandMgmtCap",
					"equipmentIndicatorLed",
					"equipmentKvmMgmtCap",
					"equipmentLocalDiskCapProvider",
					"equipmentLocalDiskControllerCapProvider",
					"equipmentLocalDiskControllerCapRef",
					"equipmentLocalDiskControllerDef",
					"equipmentLocalDiskDef",
					"equipmentLocatorLed",
					"equipmentLocatorLedFsm",
					"equipmentLocatorLedFsmStage",
					"equipmentLocatorLedFsmTask",
					"equipmentManufacturingDef",
					"equipmentMemoryUnitCapProvider",
					"equipmentMemoryUnitDiscoveryModifierDef",
					"equipmentMgmtCapProvider",
					"equipmentMgmtExtCapProvider",
					"equipmentNetworkElementFanStats",
					"equipmentNetworkElementFanStatsHist",
					"equipmentPOST",
					"equipmentPOSTCode",
					"equipmentPOSTCodeReporter",
					"equipmentPOSTCodeTemplate",
					"equipmentPciDef",
					"equipmentPhysDevicesPerBoard",
					"equipmentPhysicalDef",
					"equipmentPicture",
					"equipmentPortGroupAggregationDef",
					"equipmentPortGroupDef",
					"equipmentPortGroupSwComplexDef",
					"equipmentPortSwComplexRef",
					"equipmentProcessorUnitCapProvider",
					"equipmentProcessorUnitDef",
					"equipmentPsu",
					"equipmentPsuCapProvider",
					"equipmentPsuDef",
					"equipmentPsuInputStats",
					"equipmentPsuInputStatsHist",
					"equipmentPsuOutputStats",
					"equipmentPsuOutputStatsHist",
					"equipmentPsuStats",
					"equipmentPsuStatsHist",
					"equipmentRackFanModuleDef",
					"equipmentRackUnitCapProvider",
					"equipmentRackUnitFanStats",
					"equipmentRackUnitFanStatsHist",
					"equipmentRackUnitPsuStats",
					"equipmentRackUnitPsuStatsHist",
					"equipmentRaidDef",
					"equipmentSecureBoot",
					"equipmentServerFeatureCap",
					"equipmentServiceDef",
					"equipmentSlotArray",
					"equipmentSlotArrayRef",
					"equipmentSwitchCap",
					"equipmentSwitchCapProvider",
					"equipmentSwitchCard",
					"equipmentTpm",
					"equipmentTpmCapProvider",
					"equipmentUnifiedPortCapProvider",
					"equipmentVersionConstraint",
					"equipmentXcvr",
					"etherErrStats",
					"etherErrStatsHist",
					"etherFcoeInterfaceStats",
					"etherFcoeInterfaceStatsHist",
					"etherLossStats",
					"etherLossStatsHist",
					"etherNicIfConfig",
					"etherPIo",
					"etherPIoEndPoint",
					"etherPIoFsm",
					"etherPIoFsmStage",
					"etherPauseStats",
					"etherPauseStatsHist",
					"etherPortChanIdElem",
					"etherPortChanIdUniverse",
					"etherRxStats",
					"etherRxStatsHist",
					"etherServerIntFIo",
					"etherServerIntFIoFsm",
					"etherServerIntFIoFsmStage",
					"etherServerIntFIoFsmTask",
					"etherServerIntFIoPc",
					"etherServerIntFIoPcEp",
					"etherSwIfConfig",
					"etherSwitchIntFIo",
					"etherSwitchIntFIoPc",
					"etherSwitchIntFIoPcEp",
					"etherTxStats",
					"etherTxStatsHist",
					"eventEpCtrl",
					"eventHolder",
					"eventInst",
					"eventLog",
					"eventPolicy",
					"eventRecord",
					"extmgmtArpTargets",
					"extmgmtGatewayPing",
					"extmgmtIf",
					"extmgmtIfMonPolicy",
					"extmgmtMiiStatus",
					"extmgmtNdiscTargets",
					"extpolClient",
					"extpolClientCont",
					"extpolController",
					"extpolControllerCont",
					"extpolEp",
					"extpolEpFsm",
					"extpolEpFsmStage",
					"extpolEpFsmTask",
					"extpolProvider",
					"extpolProviderCont",
					"extpolProviderFsm",
					"extpolProviderFsmStage",
					"extpolProviderFsmTask",
					"extpolRegistry",
					"extpolRegistryFsm",
					"extpolRegistryFsmStage",
					"extpolRegistryFsmTask",
					"extpolSystemContext",
					"extvmmEp",
					"extvmmEpFsm",
					"extvmmEpFsmStage",
					"extvmmEpFsmTask",
					"extvmmFNDReference",
					"extvmmFabricNetwork",
					"extvmmFabricNetworkDefinition",
					"extvmmKeyInst",
					"extvmmKeyRing",
					"extvmmKeyStore",
					"extvmmKeyStoreFsm",
					"extvmmKeyStoreFsmStage",
					"extvmmKeyStoreFsmTask",
					"extvmmMasterExtKey",
					"extvmmMasterExtKeyFsm",
					"extvmmMasterExtKeyFsmStage",
					"extvmmMasterExtKeyFsmTask",
					"extvmmNetworkSets",
					"extvmmNetworkSetsFsm",
					"extvmmNetworkSetsFsmStage",
					"extvmmNetworkSetsFsmTask",
					"extvmmProvider",
					"extvmmProviderFsm",
					"extvmmProviderFsmStage",
					"extvmmProviderFsmTask",
					"extvmmSwitchDelTask",
					"extvmmSwitchDelTaskFsm",
					"extvmmSwitchDelTaskFsmStage",
					"extvmmSwitchDelTaskFsmTask",
					"extvmmSwitchSet",
					"extvmmUpLinkPP",
					"extvmmVMNDRef",
					"extvmmVMNetwork",
					"extvmmVMNetworkDefinition",
					"extvmmVMNetworkSets",
					"fabricBHVlan",
					"fabricCdpLinkPolicy",
					"fabricChangedObjectRef",
					"fabricChassisEp",
					"fabricComputePhEp",
					"fabricComputeSlotEp",
					"fabricComputeSlotEpFsm",
					"fabricComputeSlotEpFsmStage",
					"fabricComputeSlotEpFsmTask",
					"fabricDceSrv",
					"fabricDceSwSrv",
					"fabricDceSwSrvEp",
					"fabricDceSwSrvPc",
					"fabricDceSwSrvPcEp",
					"fabricEp",
					"fabricEpMgr",
					"fabricEpMgrFsm",
					"fabricEpMgrFsmStage",
					"fabricEpMgrFsmTask",
					"fabricEthEstc",
					"fabricEthEstcCloud",
					"fabricEthEstcEp",
					"fabricEthEstcPc",
					"fabricEthEstcPcEp",
					"fabricEthFlowMonLan",
					"fabricEthLan",
					"fabricEthLanEp",
					"fabricEthLanFlowMonitoring",
					"fabricEthLanPc",
					"fabricEthLanPcEp",
					"fabricEthLinkProfile",
					"fabricEthMon",
					"fabricEthMonDestEp",
					"fabricEthMonFiltEp",
					"fabricEthMonFiltRef",
					"fabricEthMonLan",
					"fabricEthMonSrcEp",
					"fabricEthMonSrcRef",
					"fabricEthTargetEp",
					"fabricEthVlanPc",
					"fabricEthVlanPortEp",
					"fabricFcEstc",
					"fabricFcEstcCloud",
					"fabricFcEstcEp",
					"fabricFcMon",
					"fabricFcMonDestEp",
					"fabricFcMonFiltEp",
					"fabricFcMonFiltRef",
					"fabricFcMonSan",
					"fabricFcMonSrcEp",
					"fabricFcMonSrcRef",
					"fabricFcSan",
					"fabricFcSanEp",
					"fabricFcSanPc",
					"fabricFcSanPcEp",
					"fabricFcVsanPc",
					"fabricFcVsanPortEp",
					"fabricFcoeEstcEp",
					"fabricFcoeSanEp",
					"fabricFcoeSanPc",
					"fabricFcoeSanPcEp",
					"fabricFcoeVsanPc",
					"fabricFcoeVsanPortEp",
					"fabricFlowMonDefinition",
					"fabricFlowMonExporterProfile",
					"fabricIf",
					"fabricLacpPolicy",
					"fabricLanAccessMgr",
					"fabricLanCloud",
					"fabricLanCloudFsm",
					"fabricLanCloudFsmStage",
					"fabricLanCloudFsmTask",
					"fabricLanMonCloud",
					"fabricLanPinGroup",
					"fabricLanPinTarget",
					"fabricLastAckedSlot",
					"fabricLocale",
					"fabricMulticastPolicy",
					"fabricNetGroup",
					"fabricNetflowCollector",
					"fabricNetflowIPv4Addr",
					"fabricNetflowMonExporter",
					"fabricNetflowMonExporterRef",
					"fabricNetflowMonSession",
					"fabricNetflowMonSrcEp",
					"fabricNetflowMonSrcRef",
					"fabricNetflowMonitor",
					"fabricNetflowMonitorRef",
					"fabricNetflowTimeoutPolicy",
					"fabricOrgVlanPolicy",
					"fabricPath",
					"fabricPathConn",
					"fabricPathEp",
					"fabricPoolableVlan",
					"fabricPooledVlan",
					"fabricSanCloud",
					"fabricSanCloudFsm",
					"fabricSanCloudFsmStage",
					"fabricSanCloudFsmTask",
					"fabricSanMonCloud",
					"fabricSanPinGroup",
					"fabricSanPinTarget",
					"fabricSwChPhEp",
					"fabricUdldLinkPolicy",
					"fabricUdldPolicy",
					"fabricVCon",
					"fabricVConProfile",
					"fabricVlan",
					"fabricVlanEp",
					"fabricVlanGroupReq",
					"fabricVlanPermit",
					"fabricVlanReq",
					"fabricVnetEpSyncEp",
					"fabricVnetEpSyncEpFsm",
					"fabricVnetEpSyncEpFsmStage",
					"fabricVnetEpSyncEpFsmTask",
					"fabricVsan",
					"fabricVsanEp",
					"fabricVsanMembership",
					"fabricZoneIdUniverse",
					"faultAffectedClass",
					"faultHolder",
					"faultInst",
					"faultLocalTypedHolder",
					"faultPolicy",
					"faultSuppressPolicy",
					"faultSuppressPolicyItem",
					"faultSuppressTask",
					"fcErrStats",
					"fcErrStatsHist",
					"fcNicIfConfig",
					"fcPIo",
					"fcPIoFsm",
					"fcPIoFsmStage",
					"fcStats",
					"fcStatsHist",
					"fcSwIfConfig",
					"fcpoolAddr",
					"fcpoolBlock",
					"fcpoolBootTarget",
					"fcpoolFormat",
					"fcpoolInitiator",
					"fcpoolInitiatorEp",
					"fcpoolInitiators",
					"fcpoolPoolable",
					"fcpoolUniverse",
					"firmwareAck",
					"firmwareAutoSyncPolicy",
					"firmwareBlade",
					"firmwareBootDefinition",
					"firmwareBootUnit",
					"firmwareBundleInfo",
					"firmwareBundleInfoDigest",
					"firmwareBundleType",
					"firmwareBundleTypeCapProvider",
					"firmwareCatalogPack",
					"firmwareCatalogue",
					"firmwareCompSource",
					"firmwareCompTarget",
					"firmwareComputeHostPack",
					"firmwareComputeMgmtPack",
					"firmwareDependency",
					"firmwareDistImage",
					"firmwareDistributable",
					"firmwareDistributableFsm",
					"firmwareDistributableFsmStage",
					"firmwareDistributableFsmTask",
					"firmwareDownloader",
					"firmwareDownloaderFsm",
					"firmwareDownloaderFsmStage",
					"firmwareDownloaderFsmTask",
					"firmwareHost",
					"firmwareHostPackModImpact",
					"firmwareImage",
					"firmwareImageFsm",
					"firmwareImageFsmStage",
					"firmwareImageFsmTask",
					"firmwareImageLock",
					"firmwareInfra",
					"firmwareInfraPack",
					"firmwareInstallImpact",
					"firmwareInstallable",
					"firmwarePackItem",
					"firmwareRack",
					"firmwareRunning",
					"firmwareSpec",
					"firmwareStatus",
					"firmwareSystem",
					"firmwareSystemCompCheckResult",
					"firmwareSystemFsm",
					"firmwareSystemFsmStage",
					"firmwareSystemFsmTask",
					"firmwareType",
					"firmwareUcscInfo",
					"firmwareUpdatable",
					"firmwareUpgradeConstraint",
					"firmwareUpgradeDetail",
					"firmwareUpgradeInfo",
					"flowctrlDefinition",
					"flowctrlItem",
					"fsmStatus",
					"gmetaClass",
					"gmetaEp",
					"gmetaHolder",
					"gmetaHolderFsm",
					"gmetaHolderFsmStage",
					"gmetaHolderFsmTask",
					"gmetaPolicyMapElement",
					"gmetaPolicyMapHolder",
					"gmetaProp",
					"graphicsCard",
					"graphicsController",
					"hostimgPolicy",
					"hostimgTarget",
					"identIdentCtx",
					"identIdentRequest",
					"identIdentRequestFsm",
					"identIdentRequestFsmStage",
					"identIdentRequestFsmTask",
					"identMetaSystem",
					"identMetaSystemFsm",
					"identMetaSystemFsmStage",
					"identMetaSystemFsmTask",
					"identMetaVerse",
					"identRequestEp",
					"identSysInfo",
					"imgprovPolicy",
					"imgprovTarget",
					"imgsecKey",
					"imgsecPolicy",
					"initiatorFcInitiatorEp",
					"initiatorGroupEp",
					"initiatorIScsiInitiatorEp",
					"initiatorLunEp",
					"initiatorMemberEp",
					"initiatorRequestorEp",
					"initiatorRequestorGrpEp",
					"initiatorStoreEp",
					"initiatorUnitEp",
					"ipDnsSuffix",
					"ipIPv4Dns",
					"ipIPv4WinsServer",
					"ipIpV4StaticAddr",
					"ipIpV4StaticTargetAddr",
					"ipServiceIf",
					"ippoolAddr",
					"ippoolBlock",
					"ippoolIpV6Addr",
					"ippoolIpV6Block",
					"ippoolIpV6Pooled",
					"ippoolPool",
					"ippoolPoolable",
					"ippoolPooled",
					"ippoolUniverse",
					"iqnpoolAddr",
					"iqnpoolBlock",
					"iqnpoolFormat",
					"iqnpoolPool",
					"iqnpoolPoolable",
					"iqnpoolPooled",
					"iqnpoolTransportBlock",
					"iqnpoolUniverse",
					"iscsiAuthProfile",
					"licenseContents",
					"licenseDownloader",
					"licenseDownloaderFsm",
					"licenseDownloaderFsmStage",
					"licenseDownloaderFsmTask",
					"licenseEp",
					"licenseFeature",
					"licenseFeatureCapProvider",
					"licenseFeatureLine",
					"licenseFile",
					"licenseFileFsm",
					"licenseFileFsmStage",
					"licenseFileFsmTask",
					"licenseInstance",
					"licenseInstanceFsm",
					"licenseInstanceFsmStage",
					"licenseInstanceFsmTask",
					"licenseProp",
					"licenseServerHostId",
					"licenseSource",
					"licenseSourceFile",
					"lldpAcquired",
					"lsAgentPolicy",
					"lsBinding",
					"lsFcLocale",
					"lsFcZone",
					"lsFcZoneGroup",
					"lsIssues",
					"lsPower",
					"lsRequirement",
					"lsServer",
					"lsServerAssocCtx",
					"lsServerExtension",
					"lsServerFsm",
					"lsServerFsmStage",
					"lsServerFsmTask",
					"lsTier",
					"lsUuidHistory",
					"lsVConAssign",
					"lsVersionBeh",
					"lsZoneInitiatorMember",
					"lsZoneTargetMember",
					"lsbootBootSecurity",
					"lsbootDef",
					"lsbootDefaultLocalImage",
					"lsbootIScsi",
					"lsbootIScsiImagePath",
					"lsbootLan",
					"lsbootLanImagePath",
					"lsbootLocalHddImage",
					"lsbootLocalStorage",
					"lsbootPolicy",
					"lsbootSan",
					"lsbootSanCatSanImage",
					"lsbootSanCatSanImagePath",
					"lsbootSanImage",
					"lsbootSanImagePath",
					"lsbootStorage",
					"lsbootUsbExternalImage",
					"lsbootUsbFlashStorageImage",
					"lsbootUsbInternalImage",
					"lsbootVirtualMedia",
					"lsmaintAck",
					"lsmaintMaintPolicy",
					"macpoolAddr",
					"macpoolBlock",
					"macpoolFormat",
					"macpoolPool",
					"macpoolPoolable",
					"macpoolPooled",
					"macpoolUniverse",
					"managedObject",
					"memoryArray",
					"memoryArrayEnvStats",
					"memoryArrayEnvStatsHist",
					"memoryBufferUnit",
					"memoryBufferUnitEnvStats",
					"memoryBufferUnitEnvStatsHist",
					"memoryErrorStats",
					"memoryQual",
					"memoryRuntime",
					"memoryRuntimeHist",
					"memoryUnit",
					"memoryUnitEnvStats",
					"memoryUnitEnvStatsHist",
					"mgmtAccessPolicy",
					"mgmtAccessPolicyItem",
					"mgmtAccessPort",
					"mgmtBackup",
					"mgmtBackupExportExtPolicy",
					"mgmtBackupFsm",
					"mgmtBackupFsmStage",
					"mgmtBackupFsmTask",
					"mgmtBackupPolicy",
					"mgmtBackupPolicyConfig",
					"mgmtBackupPolicyFsm",
					"mgmtBackupPolicyFsmStage",
					"mgmtCfgExportPolicy",
					"mgmtCfgExportPolicyFsm",
					"mgmtCfgExportPolicyFsmStage",
					"mgmtConnection",
					"mgmtController",
					"mgmtControllerFsm",
					"mgmtControllerFsmStage",
					"mgmtControllerFsmTask",
					"mgmtEntity",
					"mgmtExportPolicyFsm",
					"mgmtExportPolicyFsmStage",
					"mgmtExportPolicyFsmTask",
					"mgmtIPv6IfAddr",
					"mgmtIPv6IfAddrFsm",
					"mgmtIPv6IfAddrFsmStage",
					"mgmtIPv6IfAddrFsmTask",
					"mgmtIPv6IfConfig",
					"mgmtIf",
					"mgmtIfFsm",
					"mgmtIfFsmStage",
					"mgmtIfFsmTask",
					"mgmtImporter",
					"mgmtImporterFsm",
					"mgmtImporterFsmStage",
					"mgmtImporterFsmTask",
					"mgmtInbandProfile",
					"mgmtIntAuthPolicy",
					"mgmtInterface",
					"mgmtPmonEntry",
					"mgmtProfDerivedInterface",
					"mgmtVnet",
					"networkElement",
					"networkIfStats",
					"networkOperLevel",
					"nfsEp",
					"nfsMountDef",
					"nfsMountDefFsm",
					"nfsMountDefFsmStage",
					"nfsMountDefFsmTask",
					"nfsMountInst",
					"nfsMountInstFsm",
					"nfsMountInstFsmStage",
					"nfsMountInstFsmTask",
					"nwctrlDefinition",
					"observe",
					"observeObserved",
					"observeObservedCont",
					"observeObservedFsm",
					"observeObservedFsmStage",
					"observeObservedFsmTask",
					"orgOrg",
					"orgSourceMask",
					"osAgent",
					"osInstance",
					"pciEquipSlot",
					"pciUnit",
					"pkiCertReq",
					"pkiEp",
					"pkiEpFsm",
					"pkiEpFsmStage",
					"pkiEpFsmTask",
					"pkiKeyRing",
					"pkiTP",
					"policyCentraleSync",
					"policyCommunication",
					"policyConfigBackup",
					"policyControlEp",
					"policyControlEpFsm",
					"policyControlEpFsmStage",
					"policyControlEpFsmTask",
					"policyControlledInstance",
					"policyControlledType",
					"policyControlledTypeFsm",
					"policyControlledTypeFsmStage",
					"policyControlledTypeFsmTask",
					"policyDateTime",
					"policyDigest",
					"policyDiscovery",
					"policyDns",
					"policyElement",
					"policyFault",
					"policyInfraFirmware",
					"policyLocalMap",
					"policyMEp",
					"policyMonitoring",
					"policyPolicyEp",
					"policyPolicyRequestor",
					"policyPolicyScope",
					"policyPolicyScopeCont",
					"policyPolicyScopeContext",
					"policyPolicyScopeFsm",
					"policyPolicyScopeFsmStage",
					"policyPolicyScopeFsmTask",
					"policyPowerMgmt",
					"policyPsu",
					"policyRefReq",
					"policySecurity",
					"portDomainEp",
					"portGroup",
					"portPIoFsm",
					"portPIoFsmStage",
					"portPIoFsmTask",
					"portTrustMode",
					"powerBudget",
					"powerChassisMember",
					"powerEp",
					"powerGroup",
					"powerGroupAdditionPolicy",
					"powerGroupQual",
					"powerGroupStats",
					"powerGroupStatsHist",
					"powerMgmtPolicy",
					"powerPlacement",
					"powerPolicy",
					"powerPrioWght",
					"powerRackUnitMember",
					"procDoer",
					"procManager",
					"procPrt",
					"procPrtCounts",
					"procStimulusCounts",
					"procSvc",
					"procTxCounts",
					"processorCore",
					"processorEnvStats",
					"processorEnvStatsHist",
					"processorErrorStats",
					"processorQual",
					"processorRuntime",
					"processorRuntimeHist",
					"processorThread",
					"processorUnit",
					"processorUnitAssocCtx",
					"qosclassDefinition",
					"qosclassDefinitionFsm",
					"qosclassDefinitionFsmStage",
					"qosclassDefinitionFsmTask",
					"qosclassEthBE",
					"qosclassEthClassified",
					"qosclassFc",
					"queryresultDependency",
					"queryresultUsage",
					"solConfig",
					"solIf",
					"solPolicy",
					"statsCollectionPolicy",
					"statsCollectionPolicyFsm",
					"statsCollectionPolicyFsmStage",
					"statsCollectionPolicyFsmTask",
					"statsHolder",
					"statsThr32Definition",
					"statsThr32Value",
					"statsThr64Definition",
					"statsThr64Value",
					"statsThrFloatDefinition",
					"statsThrFloatValue",
					"statsThresholdClass",
					"statsThresholdPolicy",
					"storageAuthKey",
					"storageConnectionDef",
					"storageConnectionPolicy",
					"storageController",
					"storageDomainEp",
					"storageDrive",
					"storageEnclosure",
					"storageEpUser",
					"storageEtherIf",
					"storageFcIf",
					"storageFcTargetEp",
					"storageFcTargetIf",
					"storageFlexFlashCard",
					"storageFlexFlashController",
					"storageFlexFlashDrive",
					"storageFlexFlashVirtualDrive",
					"storageIScsiTargetIf",
					"storageIniGroup",
					"storageInitiator",
					"storageItem",
					"storageLocalDisk",
					"storageLocalDiskConfigDef",
					"storageLocalDiskConfigPolicy",
					"storageLocalDiskPartition",
					"storageLocalDiskSlotEp",
					"storageLocalLun",
					"storageLunDisk",
					"storageMezzFlashLife",
					"storageNodeEp",
					"storageOperation",
					"storageQual",
					"storageRaidBattery",
					"storageSystem",
					"storageSystemFsm",
					"storageSystemFsmStage",
					"storageSystemFsmTask",
					"storageTransportableFlashModule",
					"storageVirtualDrive",
					"storageVsanRef",
					"swAccessDomain",
					"swAccessDomainFsm",
					"swAccessDomainFsmStage",
					"swAccessDomainFsmTask",
					"swAccessEp",
					"swCardEnvStats",
					"swCardEnvStatsHist",
					"swCmclan",
					"swEnvStats",
					"swEnvStatsHist",
					"swEthEstcEp",
					"swEthEstcPc",
					"swEthLanBorder",
					"swEthLanBorderFsm",
					"swEthLanBorderFsmStage",
					"swEthLanBorderFsmTask",
					"swEthLanEp",
					"swEthLanFlowMon",
					"swEthLanFlowMonFsm",
					"swEthLanFlowMonFsmStage",
					"swEthLanFlowMonFsmTask",
					"swEthLanMon",
					"swEthLanPc",
					"swEthMon",
					"swEthMonDestEp",
					"swEthMonFsm",
					"swEthMonFsmStage",
					"swEthMonFsmTask",
					"swEthMonSrcEp",
					"swEthTargetEp",
					"swFabricZoneNs",
					"swFabricZoneNsOverride",
					"swFcEstcEp",
					"swFcMon",
					"swFcMonDestEp",
					"swFcMonFsm",
					"swFcMonFsmStage",
					"swFcMonFsmTask",
					"swFcMonSrcEp",
					"swFcSanBorder",
					"swFcSanBorderFsm",
					"swFcSanBorderFsmStage",
					"swFcSanBorderFsmTask",
					"swFcSanEp",
					"swFcSanMon",
					"swFcSanPc",
					"swFcServerZoneGroup",
					"swFcZone",
					"swFcZoneSet",
					"swFcoeEstcEp",
					"swFcoeSanEp",
					"swFcoeSanPc",
					"swIpRoute",
					"swNFExporterRef",
					"swNetflowExporter",
					"swNetflowMonSession",
					"swNetflowMonitor",
					"swNetflowMonitorRef",
					"swNetflowRecordDef",
					"swPhys",
					"swPhysEtherEp",
					"swPhysFcEp",
					"swPhysFsm",
					"swPhysFsmStage",
					"swPhysFsmTask",
					"swSystemStats",
					"swSystemStatsHist",
					"swUlan",
					"swUtilityDomain",
					"swUtilityDomainFsm",
					"swUtilityDomainFsmStage",
					"swUtilityDomainFsmTask",
					"swVirtL3Intf",
					"swVlan",
					"swVlanGroup",
					"swVlanPortNs",
					"swVlanPortNsOverride",
					"swVlanRef",
					"swVsan",
					"swZoneInitiatorMember",
					"swZoneTargetMember",
					"swatAction",
					"swatCondition",
					"swatInjection",
					"swatResultstats",
					"swatTarget",
					"swatTrigger",
					"syntheticDirectory",
					"syntheticFile",
					"syntheticFileSystem",
					"syntheticFsObj",
					"syntheticFsObjFsm",
					"syntheticFsObjFsmStage",
					"syntheticFsObjFsmTask",
					"syntheticTime",
					"sysdebugAutoCoreFileExportTarget",
					"sysdebugAutoCoreFileExportTargetFsm",
					"sysdebugAutoCoreFileExportTargetFsmStage",
					"sysdebugAutoCoreFileExportTargetFsmTask",
					"sysdebugBackupBehavior",
					"sysdebugCore",
					"sysdebugCoreFileRepository",
					"sysdebugCoreFsm",
					"sysdebugCoreFsmStage",
					"sysdebugCoreFsmTask",
					"sysdebugEp",
					"sysdebugLogControlDestinationFile",
					"sysdebugLogControlDestinationSyslog",
					"sysdebugLogControlDomain",
					"sysdebugLogControlEp",
					"sysdebugLogControlEpFsm",
					"sysdebugLogControlEpFsmStage",
					"sysdebugLogControlEpFsmTask",
					"sysdebugLogControlModule",
					"sysdebugLogExportPolicy",
					"sysdebugLogExportPolicyFsm",
					"sysdebugLogExportPolicyFsmStage",
					"sysdebugLogExportPolicyFsmTask",
					"sysdebugLogExportStatus",
					"sysdebugMEpLog",
					"sysdebugMEpLogPolicy",
					"sysdebugManualCoreFileExportTarget",
					"sysdebugManualCoreFileExportTargetFsm",
					"sysdebugManualCoreFileExportTargetFsmStage",
					"sysdebugManualCoreFileExportTargetFsmTask",
					"sysdebugTechSupFileRepository",
					"sysdebugTechSupport",
					"sysdebugTechSupportCmdOpt",
					"sysdebugTechSupportFsm",
					"sysdebugTechSupportFsmStage",
					"sysdebugTechSupportFsmTask",
					"sysfileDigest",
					"sysfileMutation",
					"sysfileMutationFsm",
					"sysfileMutationFsmStage",
					"sysfileMutationFsmTask",
					"topMetaInf",
					"topRoot",
					"topSysDefaults",
					"topSystem",
					"trigAbsWindow",
					"trigClientToken",
					"trigLocalAbsWindow",
					"trigLocalSched",
					"trigMeta",
					"trigRecurrWindow",
					"trigSched",
					"trigTest",
					"trigTriggered",
					"uuidpoolAddr",
					"uuidpoolBlock",
					"uuidpoolFormat",
					"uuidpoolPool",
					"uuidpoolPoolable",
					"uuidpoolPooled",
					"uuidpoolUniverse",
					"versionApplication",
					"versionEp",
					"vmComputeEp",
					"vmDC",
					"vmDCOrg",
					"vmEp",
					"vmHba",
					"vmHv",
					"vmInstance",
					"vmLifeCyclePolicy",
					"vmLifeCyclePolicyFsm",
					"vmLifeCyclePolicyFsmStage",
					"vmLifeCyclePolicyFsmTask",
					"vmNic",
					"vmOrg",
					"vmSwitch",
					"vmVif",
					"vmVlan",
					"vmVnicProfCl",
					"vmVnicProfInst",
					"vmVsan",
					"vnicBootIpPolicy",
					"vnicBootTarget",
					"vnicConnDef",
					"vnicDefBeh",
					"vnicDynamicCon",
					"vnicDynamicConPolicy",
					"vnicDynamicConPolicyRef",
					"vnicDynamicIdUniverse",
					"vnicDynamicProvider",
					"vnicDynamicProviderEp",
					"vnicEthLif",
					"vnicEther",
					"vnicEtherIf",
					"vnicFc",
					"vnicFcGroupDef",
					"vnicFcGroupTempl",
					"vnicFcIf",
					"vnicFcLif",
					"vnicFcNode",
					"vnicFcOEIf",
					"vnicIPv4Dhcp",
					"vnicIPv4Dns",
					"vnicIPv4If",
					"vnicIPv4IscsiAddr",
					"vnicIPv4PooledIscsiAddr",
					"vnicIPv4StaticRoute",
					"vnicIScsi",
					"vnicIScsiAutoTargetIf",
					"vnicIScsiBootParams",
					"vnicIScsiBootVnic",
					"vnicIScsiLCP",
					"vnicIScsiNode",
					"vnicIScsiStaticTargetIf",
					"vnicInternalProfile",
					"vnicIpV4History",
					"vnicIpV4MgmtPooledAddr",
					"vnicIpV4PooledAddr",
					"vnicIpV4ProfDerivedAddr",
					"vnicIpV4StaticAddr",
					"vnicIpV6History",
					"vnicIpV6MgmtPooledAddr",
					"vnicIpV6StaticAddr",
					"vnicIpc",
					"vnicIpcIf",
					"vnicIqnHistory",
					"vnicLanConnPolicy",
					"vnicLanConnTempl",
					"vnicLifVlan",
					"vnicLifVsan",
					"vnicLun",
					"vnicMacHistory",
					"vnicOProfileAlias",
					"vnicProfile",
					"vnicProfileAlias",
					"vnicProfileRef",
					"vnicProfileSet",
					"vnicProfileSetFsm",
					"vnicProfileSetFsmStage",
					"vnicProfileSetFsmTask",
					"vnicRackServerDiscoveryProfile",
					"vnicSanConnPolicy",
					"vnicSanConnTempl",
					"vnicScsi",
					"vnicScsiIf",
					"vnicUsnicConPolicy",
					"vnicUsnicConPolicyRef",
					"vnicVhbaBehPolicy",
					"vnicVlan",
					"vnicVmqConPolicy",
					"vnicVmqConPolicyRef",
					"vnicVnicBehPolicy",
					"vnicWwnnHistory",
					"vnicWwpnHistory",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class ConfigMap(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ConfigMap")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the ConfigMap object."""
		if w is None:
			x=Element("configMap")
		else:
			if (elementName == None):
				x = SubElement(w,"configMap")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the ConfigMap object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the ConfigMap object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the ConfigMap object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"pair",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class ConfigSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ConfigSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the ConfigSet object."""
		if w is None:
			x=Element("configSet")
		else:
			if (elementName == None):
				x = SubElement(w,"configSet")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the ConfigSet object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the ConfigSet object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the ConfigSet object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"aaaAuthRealm",
					"aaaAuthRealmFsm",
					"aaaAuthRealmFsmStage",
					"aaaCimcSession",
					"aaaConsoleAuth",
					"aaaDefaultAuth",
					"aaaDomain",
					"aaaDomainAuth",
					"aaaEpAuthProfile",
					"aaaEpFsm",
					"aaaEpFsmStage",
					"aaaEpFsmTask",
					"aaaEpLogin",
					"aaaEpUser",
					"aaaExtMgmtCutThruTkn",
					"aaaLdapEp",
					"aaaLdapEpFsm",
					"aaaLdapEpFsmStage",
					"aaaLdapGroup",
					"aaaLdapGroupRule",
					"aaaLdapProvider",
					"aaaLocale",
					"aaaLog",
					"aaaModLR",
					"aaaOrg",
					"aaaPreLoginBanner",
					"aaaProviderGroup",
					"aaaProviderRef",
					"aaaPwdProfile",
					"aaaRadiusEp",
					"aaaRadiusEpFsm",
					"aaaRadiusEpFsmStage",
					"aaaRadiusProvider",
					"aaaRealmFsm",
					"aaaRealmFsmStage",
					"aaaRealmFsmTask",
					"aaaRemoteUser",
					"aaaRole",
					"aaaSession",
					"aaaSessionInfo",
					"aaaSessionInfoTable",
					"aaaSessionLR",
					"aaaShellLogin",
					"aaaSshAuth",
					"aaaTacacsPlusEp",
					"aaaTacacsPlusEpFsm",
					"aaaTacacsPlusEpFsmStage",
					"aaaTacacsPlusProvider",
					"aaaUser",
					"aaaUserData",
					"aaaUserEp",
					"aaaUserEpFsm",
					"aaaUserEpFsmStage",
					"aaaUserEpFsmTask",
					"aaaUserLocale",
					"aaaUserRole",
					"aaaWebLogin",
					"adaptorCapQual",
					"adaptorCapSpec",
					"adaptorDiagCap",
					"adaptorEthArfsProfile",
					"adaptorEthCompQueueProfile",
					"adaptorEthFailoverProfile",
					"adaptorEthInterruptProfile",
					"adaptorEthOffloadProfile",
					"adaptorEthPortBySizeLargeStats",
					"adaptorEthPortBySizeLargeStatsHist",
					"adaptorEthPortBySizeSmallStats",
					"adaptorEthPortBySizeSmallStatsHist",
					"adaptorEthPortErrStats",
					"adaptorEthPortErrStatsHist",
					"adaptorEthPortMcastStats",
					"adaptorEthPortMcastStatsHist",
					"adaptorEthPortOutsizedStats",
					"adaptorEthPortOutsizedStatsHist",
					"adaptorEthPortStats",
					"adaptorEthPortStatsHist",
					"adaptorEthRecvQueueProfile",
					"adaptorEthWorkQueueProfile",
					"adaptorEtherIfStats",
					"adaptorEtherIfStatsHist",
					"adaptorExtEthIf",
					"adaptorExtEthIfFsm",
					"adaptorExtEthIfFsmStage",
					"adaptorExtEthIfFsmTask",
					"adaptorExtEthIfPc",
					"adaptorExtEthIfPcEp",
					"adaptorExtIpV6RssHashProfile",
					"adaptorFamilyTypeDef",
					"adaptorFcCdbWorkQueueProfile",
					"adaptorFcErrorRecoveryProfile",
					"adaptorFcIfEventStats",
					"adaptorFcIfEventStatsHist",
					"adaptorFcIfFC4Stats",
					"adaptorFcIfFC4StatsHist",
					"adaptorFcIfFrameStats",
					"adaptorFcIfFrameStatsHist",
					"adaptorFcInterruptProfile",
					"adaptorFcOEIf",
					"adaptorFcPortFLogiProfile",
					"adaptorFcPortPLogiProfile",
					"adaptorFcPortProfile",
					"adaptorFcPortStats",
					"adaptorFcPortStatsHist",
					"adaptorFcRecvQueueProfile",
					"adaptorFcWorkQueueProfile",
					"adaptorFruCapProvider",
					"adaptorFruCapRef",
					"adaptorFwCapProvider",
					"adaptorHostEthIf",
					"adaptorHostEthIfFsm",
					"adaptorHostEthIfFsmStage",
					"adaptorHostEthIfFsmTask",
					"adaptorHostEthIfProfile",
					"adaptorHostFcIf",
					"adaptorHostFcIfFsm",
					"adaptorHostFcIfFsmStage",
					"adaptorHostFcIfFsmTask",
					"adaptorHostFcIfProfile",
					"adaptorHostIscsiIf",
					"adaptorHostIscsiIfProfile",
					"adaptorHostMgmtCap",
					"adaptorHostServiceEthIf",
					"adaptorHostethHwAddrCap",
					"adaptorHostfcHwAddrCap",
					"adaptorIScsiCap",
					"adaptorIpV4RssHashProfile",
					"adaptorIpV6RssHashProfile",
					"adaptorIscsiAuth",
					"adaptorIscsiProt",
					"adaptorIscsiTargetIf",
					"adaptorLanCap",
					"adaptorLldpCap",
					"adaptorMenloBaseErrorStats",
					"adaptorMenloBaseErrorStatsHist",
					"adaptorMenloDcePortStats",
					"adaptorMenloDcePortStatsHist",
					"adaptorMenloEthErrorStats",
					"adaptorMenloEthErrorStatsHist",
					"adaptorMenloEthStats",
					"adaptorMenloEthStatsHist",
					"adaptorMenloFcErrorStats",
					"adaptorMenloFcErrorStatsHist",
					"adaptorMenloFcStats",
					"adaptorMenloFcStatsHist",
					"adaptorMenloHostPortStats",
					"adaptorMenloHostPortStatsHist",
					"adaptorMenloMcpuErrorStats",
					"adaptorMenloMcpuErrorStatsHist",
					"adaptorMenloMcpuStats",
					"adaptorMenloMcpuStatsHist",
					"adaptorMenloNetEgStats",
					"adaptorMenloNetEgStatsHist",
					"adaptorMenloNetInStats",
					"adaptorMenloNetInStatsHist",
					"adaptorMenloQErrorStats",
					"adaptorMenloQErrorStatsHist",
					"adaptorMenloQStats",
					"adaptorMenloQStatsHist",
					"adaptorNwMgmtCap",
					"adaptorProtocolProfile",
					"adaptorQual",
					"adaptorRssProfile",
					"adaptorSanCap",
					"adaptorUnit",
					"adaptorUnitAssocCtx",
					"adaptorUnitExtn",
					"adaptorUplinkHwAddrCap",
					"adaptorUsnicConnDef",
					"adaptorVlan",
					"adaptorVnicStats",
					"adaptorVnicStatsHist",
					"adaptorVsan",
					"apeControllerChassis",
					"apeControllerEeprom",
					"apeControllerManager",
					"apeDcosAgManager",
					"apeFru",
					"apeHostAgent",
					"apeLANBoot",
					"apeLocalDiskBoot",
					"apeManager",
					"apeMc",
					"apeMcTable",
					"apeMenlo",
					"apeMenloVnic",
					"apeMenloVnicStats",
					"apeNicAgManager",
					"apePalo",
					"apePaloVnic",
					"apePaloVnicStats",
					"apeParam",
					"apeReading",
					"apeSANBoot",
					"apeSdr",
					"apeSwitchFirmwareInv",
					"apeVirtualMediaBoot",
					"biosBOT",
					"biosBootDev",
					"biosBootDevGrp",
					"biosFeatureRef",
					"biosParameterRef",
					"biosRef",
					"biosSettingRef",
					"biosSettings",
					"biosUnit",
					"biosVIdentityParams",
					"biosVProfile",
					"biosVfACPI10Support",
					"biosVfAllUSBDevices",
					"biosVfAssertNMIOnPERR",
					"biosVfAssertNMIOnSERR",
					"biosVfBootOptionRetry",
					"biosVfCPUPerformance",
					"biosVfConsoleRedirection",
					"biosVfCoreMultiProcessing",
					"biosVfDRAMClockThrottling",
					"biosVfDirectCacheAccess",
					"biosVfDramRefreshRate",
					"biosVfEnhancedIntelSpeedStepTech",
					"biosVfExecuteDisableBit",
					"biosVfFRB2Timer",
					"biosVfFrequencyFloorOverride",
					"biosVfFrontPanelLockout",
					"biosVfIntelEntrySASRAIDModule",
					"biosVfIntelHyperThreadingTech",
					"biosVfIntelTurboBoostTech",
					"biosVfIntelVTForDirectedIO",
					"biosVfIntelVirtualizationTechnology",
					"biosVfInterleaveConfiguration",
					"biosVfLOMPortsConfiguration",
					"biosVfLocalX2Apic",
					"biosVfLvDIMMSupport",
					"biosVfMaxVariableMTRRSetting",
					"biosVfMaximumMemoryBelow4GB",
					"biosVfMemoryMappedIOAbove4GB",
					"biosVfMirroringMode",
					"biosVfNUMAOptimized",
					"biosVfOSBootWatchdogTimer",
					"biosVfOSBootWatchdogTimerPolicy",
					"biosVfOSBootWatchdogTimerTimeout",
					"biosVfOnboardSATAController",
					"biosVfOnboardStorage",
					"biosVfOptionROMEnable",
					"biosVfOptionROMLoad",
					"biosVfPCISlotLinkSpeed",
					"biosVfPCISlotOptionROMEnable",
					"biosVfPOSTErrorPause",
					"biosVfPSTATECoordination",
					"biosVfPackageCStateLimit",
					"biosVfProcessorC1E",
					"biosVfProcessorC3Report",
					"biosVfProcessorC6Report",
					"biosVfProcessorC7Report",
					"biosVfProcessorCState",
					"biosVfProcessorEnergyConfiguration",
					"biosVfProcessorPrefetchConfig",
					"biosVfQPILinkFrequencySelect",
					"biosVfQuietBoot",
					"biosVfResumeOnACPowerLoss",
					"biosVfScrubPolicies",
					"biosVfSelectMemoryRASConfiguration",
					"biosVfSerialPortAEnable",
					"biosVfSparingMode",
					"biosVfSriovConfig",
					"biosVfUCSMBootModeControl",
					"biosVfUCSMBootOrderRuleControl",
					"biosVfUEFIOSUseLegacyVideo",
					"biosVfUSBBootConfig",
					"biosVfUSBFrontPanelAccessLock",
					"biosVfUSBPortConfiguration",
					"biosVfUSBSystemIdlePowerOptimizingSetting",
					"biosVfVGAPriority",
					"bmcSELCounter",
					"callhomeDest",
					"callhomeEp",
					"callhomeEpFsm",
					"callhomeEpFsmStage",
					"callhomeEpFsmTask",
					"callhomePeriodicSystemInventory",
					"callhomePolicy",
					"callhomeProfile",
					"callhomeSmtp",
					"callhomeSource",
					"callhomeTestAlert",
					"capabilityCatalogue",
					"capabilityCatalogueFsm",
					"capabilityCatalogueFsmStage",
					"capabilityCatalogueFsmTask",
					"capabilityEp",
					"capabilityFeatureLimits",
					"capabilityMgmtExtension",
					"capabilityMgmtExtensionFsm",
					"capabilityMgmtExtensionFsmStage",
					"capabilityMgmtExtensionFsmTask",
					"capabilityNetworkLimits",
					"capabilityStorageLimits",
					"capabilitySystemLimits",
					"capabilityUpdate",
					"capabilityUpdater",
					"capabilityUpdaterFsm",
					"capabilityUpdaterFsmStage",
					"capabilityUpdaterFsmTask",
					"changeChangedObjectRef",
					"cimcvmediaActualMountEntry",
					"cimcvmediaActualMountList",
					"cimcvmediaConfigMountEntry",
					"cimcvmediaExtMgmtRuleEntry",
					"cimcvmediaMountConfigDef",
					"cimcvmediaMountConfigPolicy",
					"clitestTypeTest",
					"clitestTypeTest2",
					"clitestTypeTestChild",
					"commCimcWebService",
					"commCimxml",
					"commDateTime",
					"commDns",
					"commDnsProvider",
					"commEvtChannel",
					"commHttp",
					"commHttps",
					"commNtpProvider",
					"commShellSvcLimits",
					"commSmashCLP",
					"commSnmp",
					"commSnmpTrap",
					"commSnmpUser",
					"commSsh",
					"commSvcEp",
					"commSvcEpFsm",
					"commSvcEpFsmStage",
					"commSvcEpFsmTask",
					"commSyslog",
					"commSyslogClient",
					"commSyslogConsole",
					"commSyslogFile",
					"commSyslogMonitor",
					"commSyslogSource",
					"commTelnet",
					"commWebChannel",
					"commWebSvcLimits",
					"commWsman",
					"commXmlClConnPolicy",
					"computeAutoconfigPolicy",
					"computeBlade",
					"computeBladeDiscPolicy",
					"computeBladeFsm",
					"computeBladeFsmStage",
					"computeBladeFsmTask",
					"computeBladeInheritPolicy",
					"computeBoard",
					"computeBoardConnector",
					"computeBoardController",
					"computeChassisConnPolicy",
					"computeChassisDiscPolicy",
					"computeChassisQual",
					"computeDefaults",
					"computeExtBoard",
					"computeFwSyncAck",
					"computeHealthLedSensorAlarm",
					"computeIOHub",
					"computeIOHubEnvStats",
					"computeIOHubEnvStatsHist",
					"computeKvmMgmtPolicy",
					"computeMbPowerStats",
					"computeMbPowerStatsHist",
					"computeMbTempStats",
					"computeMbTempStatsHist",
					"computeMemoryConfigPolicy",
					"computeMemoryConfiguration",
					"computeMemoryUnitConstraintDef",
					"computePCIeFatalCompletionStats",
					"computePCIeFatalProtocolStats",
					"computePCIeFatalReceiveStats",
					"computePCIeFatalStats",
					"computePciCap",
					"computePciSlotScanDef",
					"computePhysicalAssocCtx",
					"computePhysicalFsm",
					"computePhysicalFsmStage",
					"computePhysicalFsmTask",
					"computePhysicalQual",
					"computePlatform",
					"computePnuOSImage",
					"computePool",
					"computePoolPolicyRef",
					"computePoolable",
					"computePooledRackUnit",
					"computePooledSlot",
					"computePoolingPolicy",
					"computePsuControl",
					"computePsuPolicy",
					"computeQual",
					"computeRackQual",
					"computeRackUnit",
					"computeRackUnitFsm",
					"computeRackUnitFsmStage",
					"computeRackUnitFsmTask",
					"computeRackUnitMbTempStats",
					"computeRackUnitMbTempStatsHist",
					"computeRtcBattery",
					"computeScrubPolicy",
					"computeServerDiscPolicy",
					"computeServerDiscPolicyFsm",
					"computeServerDiscPolicyFsmStage",
					"computeServerDiscPolicyFsmTask",
					"computeServerMgmtPolicy",
					"computeSlotQual",
					"configImpact",
					"configManagedEpImpactResponse",
					"configSorter",
					"dcxFcoeVifEp",
					"dcxNs",
					"dcxUniverse",
					"dcxVIf",
					"dcxVc",
					"dcxVifEp",
					"dhcpAcquired",
					"dhcpInst",
					"dhcpLease",
					"diagBladeTest",
					"diagNetworkTest",
					"diagRslt",
					"diagRunPolicy",
					"diagSrvCapProvider",
					"diagSrvCtrl",
					"domainEnvironmentFeature",
					"domainEnvironmentFeatureCont",
					"domainEnvironmentParam",
					"domainNetworkFeature",
					"domainNetworkFeatureCont",
					"domainNetworkParam",
					"domainServerFeature",
					"domainServerFeatureCont",
					"domainServerParam",
					"domainStorageFeature",
					"domainStorageFeatureCont",
					"domainStorageParam",
					"dpsecMac",
					"epqosDefinition",
					"epqosDefinitionDelTask",
					"epqosDefinitionDelTaskFsm",
					"epqosDefinitionDelTaskFsmStage",
					"epqosDefinitionDelTaskFsmTask",
					"epqosDefinitionFsm",
					"epqosDefinitionFsmStage",
					"epqosDefinitionFsmTask",
					"epqosEgress",
					"equipmentAdaptorConnDef",
					"equipmentAdaptorDef",
					"equipmentAdvancedBootOrder",
					"equipmentBaseBoardCapProvider",
					"equipmentBeaconCapProvider",
					"equipmentBeaconLed",
					"equipmentBeaconLedFsm",
					"equipmentBeaconLedFsmStage",
					"equipmentBeaconLedFsmTask",
					"equipmentBiosDef",
					"equipmentBladeAGLibrary",
					"equipmentBladeAggregationCapRef",
					"equipmentBladeBiosCapProvider",
					"equipmentBladeCapProvider",
					"equipmentBladeConnDef",
					"equipmentBladeIOMConnDef",
					"equipmentBoardControllerDef",
					"equipmentCatalogCapProvider",
					"equipmentChassis",
					"equipmentChassisCapProvider",
					"equipmentChassisFsm",
					"equipmentChassisFsmStage",
					"equipmentChassisFsmTask",
					"equipmentChassisStats",
					"equipmentChassisStatsHist",
					"equipmentCimcVmedia",
					"equipmentDbgPluginCapProvider",
					"equipmentDimmEntry",
					"equipmentDimmMapping",
					"equipmentDiscoveryCap",
					"equipmentDowngradeConstraint",
					"equipmentFan",
					"equipmentFanModule",
					"equipmentFanModuleCapProvider",
					"equipmentFanModuleDef",
					"equipmentFanModuleStats",
					"equipmentFanModuleStatsHist",
					"equipmentFanStats",
					"equipmentFanStatsHist",
					"equipmentFex",
					"equipmentFexCapProvider",
					"equipmentFexEnvStats",
					"equipmentFexEnvStatsHist",
					"equipmentFexFsm",
					"equipmentFexFsmStage",
					"equipmentFexFsmTask",
					"equipmentFexPowerSummary",
					"equipmentFexPowerSummaryHist",
					"equipmentFexPsuInputStats",
					"equipmentFexPsuInputStatsHist",
					"equipmentFirmwareConstraint",
					"equipmentFlashLife",
					"equipmentGemCapProvider",
					"equipmentGemPortCap",
					"equipmentGraphicsCardCapProvider",
					"equipmentGraphicsCardCapRef",
					"equipmentHDDFaultMonDef",
					"equipmentHealthLed",
					"equipmentHostIfCapProvider",
					"equipmentIOCard",
					"equipmentIOCardCapProvider",
					"equipmentIOCardFsm",
					"equipmentIOCardFsmStage",
					"equipmentIOCardFsmTask",
					"equipmentIOCardStats",
					"equipmentIOCardStatsHist",
					"equipmentIOCardTypeDef",
					"equipmentInbandMgmtCap",
					"equipmentIndicatorLed",
					"equipmentKvmMgmtCap",
					"equipmentLocalDiskCapProvider",
					"equipmentLocalDiskControllerCapProvider",
					"equipmentLocalDiskControllerCapRef",
					"equipmentLocalDiskControllerDef",
					"equipmentLocalDiskDef",
					"equipmentLocatorLed",
					"equipmentLocatorLedFsm",
					"equipmentLocatorLedFsmStage",
					"equipmentLocatorLedFsmTask",
					"equipmentManufacturingDef",
					"equipmentMemoryUnitCapProvider",
					"equipmentMemoryUnitDiscoveryModifierDef",
					"equipmentMgmtCapProvider",
					"equipmentMgmtExtCapProvider",
					"equipmentNetworkElementFanStats",
					"equipmentNetworkElementFanStatsHist",
					"equipmentPOST",
					"equipmentPOSTCode",
					"equipmentPOSTCodeReporter",
					"equipmentPOSTCodeTemplate",
					"equipmentPciDef",
					"equipmentPhysDevicesPerBoard",
					"equipmentPhysicalDef",
					"equipmentPicture",
					"equipmentPortGroupAggregationDef",
					"equipmentPortGroupDef",
					"equipmentPortGroupSwComplexDef",
					"equipmentPortSwComplexRef",
					"equipmentProcessorUnitCapProvider",
					"equipmentProcessorUnitDef",
					"equipmentPsu",
					"equipmentPsuCapProvider",
					"equipmentPsuDef",
					"equipmentPsuInputStats",
					"equipmentPsuInputStatsHist",
					"equipmentPsuOutputStats",
					"equipmentPsuOutputStatsHist",
					"equipmentPsuStats",
					"equipmentPsuStatsHist",
					"equipmentRackFanModuleDef",
					"equipmentRackUnitCapProvider",
					"equipmentRackUnitFanStats",
					"equipmentRackUnitFanStatsHist",
					"equipmentRackUnitPsuStats",
					"equipmentRackUnitPsuStatsHist",
					"equipmentRaidDef",
					"equipmentSecureBoot",
					"equipmentServerFeatureCap",
					"equipmentServiceDef",
					"equipmentSlotArray",
					"equipmentSlotArrayRef",
					"equipmentSwitchCap",
					"equipmentSwitchCapProvider",
					"equipmentSwitchCard",
					"equipmentTpm",
					"equipmentTpmCapProvider",
					"equipmentUnifiedPortCapProvider",
					"equipmentVersionConstraint",
					"equipmentXcvr",
					"etherErrStats",
					"etherErrStatsHist",
					"etherFcoeInterfaceStats",
					"etherFcoeInterfaceStatsHist",
					"etherLossStats",
					"etherLossStatsHist",
					"etherNicIfConfig",
					"etherPIo",
					"etherPIoEndPoint",
					"etherPIoFsm",
					"etherPIoFsmStage",
					"etherPauseStats",
					"etherPauseStatsHist",
					"etherPortChanIdElem",
					"etherPortChanIdUniverse",
					"etherRxStats",
					"etherRxStatsHist",
					"etherServerIntFIo",
					"etherServerIntFIoFsm",
					"etherServerIntFIoFsmStage",
					"etherServerIntFIoFsmTask",
					"etherServerIntFIoPc",
					"etherServerIntFIoPcEp",
					"etherSwIfConfig",
					"etherSwitchIntFIo",
					"etherSwitchIntFIoPc",
					"etherSwitchIntFIoPcEp",
					"etherTxStats",
					"etherTxStatsHist",
					"eventEpCtrl",
					"eventHolder",
					"eventInst",
					"eventLog",
					"eventPolicy",
					"eventRecord",
					"extmgmtArpTargets",
					"extmgmtGatewayPing",
					"extmgmtIf",
					"extmgmtIfMonPolicy",
					"extmgmtMiiStatus",
					"extmgmtNdiscTargets",
					"extpolClient",
					"extpolClientCont",
					"extpolController",
					"extpolControllerCont",
					"extpolEp",
					"extpolEpFsm",
					"extpolEpFsmStage",
					"extpolEpFsmTask",
					"extpolProvider",
					"extpolProviderCont",
					"extpolProviderFsm",
					"extpolProviderFsmStage",
					"extpolProviderFsmTask",
					"extpolRegistry",
					"extpolRegistryFsm",
					"extpolRegistryFsmStage",
					"extpolRegistryFsmTask",
					"extpolSystemContext",
					"extvmmEp",
					"extvmmEpFsm",
					"extvmmEpFsmStage",
					"extvmmEpFsmTask",
					"extvmmFNDReference",
					"extvmmFabricNetwork",
					"extvmmFabricNetworkDefinition",
					"extvmmKeyInst",
					"extvmmKeyRing",
					"extvmmKeyStore",
					"extvmmKeyStoreFsm",
					"extvmmKeyStoreFsmStage",
					"extvmmKeyStoreFsmTask",
					"extvmmMasterExtKey",
					"extvmmMasterExtKeyFsm",
					"extvmmMasterExtKeyFsmStage",
					"extvmmMasterExtKeyFsmTask",
					"extvmmNetworkSets",
					"extvmmNetworkSetsFsm",
					"extvmmNetworkSetsFsmStage",
					"extvmmNetworkSetsFsmTask",
					"extvmmProvider",
					"extvmmProviderFsm",
					"extvmmProviderFsmStage",
					"extvmmProviderFsmTask",
					"extvmmSwitchDelTask",
					"extvmmSwitchDelTaskFsm",
					"extvmmSwitchDelTaskFsmStage",
					"extvmmSwitchDelTaskFsmTask",
					"extvmmSwitchSet",
					"extvmmUpLinkPP",
					"extvmmVMNDRef",
					"extvmmVMNetwork",
					"extvmmVMNetworkDefinition",
					"extvmmVMNetworkSets",
					"fabricBHVlan",
					"fabricCdpLinkPolicy",
					"fabricChangedObjectRef",
					"fabricChassisEp",
					"fabricComputePhEp",
					"fabricComputeSlotEp",
					"fabricComputeSlotEpFsm",
					"fabricComputeSlotEpFsmStage",
					"fabricComputeSlotEpFsmTask",
					"fabricDceSrv",
					"fabricDceSwSrv",
					"fabricDceSwSrvEp",
					"fabricDceSwSrvPc",
					"fabricDceSwSrvPcEp",
					"fabricEp",
					"fabricEpMgr",
					"fabricEpMgrFsm",
					"fabricEpMgrFsmStage",
					"fabricEpMgrFsmTask",
					"fabricEthEstc",
					"fabricEthEstcCloud",
					"fabricEthEstcEp",
					"fabricEthEstcPc",
					"fabricEthEstcPcEp",
					"fabricEthFlowMonLan",
					"fabricEthLan",
					"fabricEthLanEp",
					"fabricEthLanFlowMonitoring",
					"fabricEthLanPc",
					"fabricEthLanPcEp",
					"fabricEthLinkProfile",
					"fabricEthMon",
					"fabricEthMonDestEp",
					"fabricEthMonFiltEp",
					"fabricEthMonFiltRef",
					"fabricEthMonLan",
					"fabricEthMonSrcEp",
					"fabricEthMonSrcRef",
					"fabricEthTargetEp",
					"fabricEthVlanPc",
					"fabricEthVlanPortEp",
					"fabricFcEstc",
					"fabricFcEstcCloud",
					"fabricFcEstcEp",
					"fabricFcMon",
					"fabricFcMonDestEp",
					"fabricFcMonFiltEp",
					"fabricFcMonFiltRef",
					"fabricFcMonSan",
					"fabricFcMonSrcEp",
					"fabricFcMonSrcRef",
					"fabricFcSan",
					"fabricFcSanEp",
					"fabricFcSanPc",
					"fabricFcSanPcEp",
					"fabricFcVsanPc",
					"fabricFcVsanPortEp",
					"fabricFcoeEstcEp",
					"fabricFcoeSanEp",
					"fabricFcoeSanPc",
					"fabricFcoeSanPcEp",
					"fabricFcoeVsanPc",
					"fabricFcoeVsanPortEp",
					"fabricFlowMonDefinition",
					"fabricFlowMonExporterProfile",
					"fabricIf",
					"fabricLacpPolicy",
					"fabricLanAccessMgr",
					"fabricLanCloud",
					"fabricLanCloudFsm",
					"fabricLanCloudFsmStage",
					"fabricLanCloudFsmTask",
					"fabricLanMonCloud",
					"fabricLanPinGroup",
					"fabricLanPinTarget",
					"fabricLastAckedSlot",
					"fabricLocale",
					"fabricMulticastPolicy",
					"fabricNetGroup",
					"fabricNetflowCollector",
					"fabricNetflowIPv4Addr",
					"fabricNetflowMonExporter",
					"fabricNetflowMonExporterRef",
					"fabricNetflowMonSession",
					"fabricNetflowMonSrcEp",
					"fabricNetflowMonSrcRef",
					"fabricNetflowMonitor",
					"fabricNetflowMonitorRef",
					"fabricNetflowTimeoutPolicy",
					"fabricOrgVlanPolicy",
					"fabricPath",
					"fabricPathConn",
					"fabricPathEp",
					"fabricPoolableVlan",
					"fabricPooledVlan",
					"fabricSanCloud",
					"fabricSanCloudFsm",
					"fabricSanCloudFsmStage",
					"fabricSanCloudFsmTask",
					"fabricSanMonCloud",
					"fabricSanPinGroup",
					"fabricSanPinTarget",
					"fabricSwChPhEp",
					"fabricUdldLinkPolicy",
					"fabricUdldPolicy",
					"fabricVCon",
					"fabricVConProfile",
					"fabricVlan",
					"fabricVlanEp",
					"fabricVlanGroupReq",
					"fabricVlanPermit",
					"fabricVlanReq",
					"fabricVnetEpSyncEp",
					"fabricVnetEpSyncEpFsm",
					"fabricVnetEpSyncEpFsmStage",
					"fabricVnetEpSyncEpFsmTask",
					"fabricVsan",
					"fabricVsanEp",
					"fabricVsanMembership",
					"fabricZoneIdUniverse",
					"faultAffectedClass",
					"faultHolder",
					"faultInst",
					"faultLocalTypedHolder",
					"faultPolicy",
					"faultSuppressPolicy",
					"faultSuppressPolicyItem",
					"faultSuppressTask",
					"fcErrStats",
					"fcErrStatsHist",
					"fcNicIfConfig",
					"fcPIo",
					"fcPIoFsm",
					"fcPIoFsmStage",
					"fcStats",
					"fcStatsHist",
					"fcSwIfConfig",
					"fcpoolAddr",
					"fcpoolBlock",
					"fcpoolBootTarget",
					"fcpoolFormat",
					"fcpoolInitiator",
					"fcpoolInitiatorEp",
					"fcpoolInitiators",
					"fcpoolPoolable",
					"fcpoolUniverse",
					"firmwareAck",
					"firmwareAutoSyncPolicy",
					"firmwareBlade",
					"firmwareBootDefinition",
					"firmwareBootUnit",
					"firmwareBundleInfo",
					"firmwareBundleInfoDigest",
					"firmwareBundleType",
					"firmwareBundleTypeCapProvider",
					"firmwareCatalogPack",
					"firmwareCatalogue",
					"firmwareCompSource",
					"firmwareCompTarget",
					"firmwareComputeHostPack",
					"firmwareComputeMgmtPack",
					"firmwareDependency",
					"firmwareDistImage",
					"firmwareDistributable",
					"firmwareDistributableFsm",
					"firmwareDistributableFsmStage",
					"firmwareDistributableFsmTask",
					"firmwareDownloader",
					"firmwareDownloaderFsm",
					"firmwareDownloaderFsmStage",
					"firmwareDownloaderFsmTask",
					"firmwareHost",
					"firmwareHostPackModImpact",
					"firmwareImage",
					"firmwareImageFsm",
					"firmwareImageFsmStage",
					"firmwareImageFsmTask",
					"firmwareImageLock",
					"firmwareInfra",
					"firmwareInfraPack",
					"firmwareInstallImpact",
					"firmwareInstallable",
					"firmwarePackItem",
					"firmwareRack",
					"firmwareRunning",
					"firmwareSpec",
					"firmwareStatus",
					"firmwareSystem",
					"firmwareSystemCompCheckResult",
					"firmwareSystemFsm",
					"firmwareSystemFsmStage",
					"firmwareSystemFsmTask",
					"firmwareType",
					"firmwareUcscInfo",
					"firmwareUpdatable",
					"firmwareUpgradeConstraint",
					"firmwareUpgradeDetail",
					"firmwareUpgradeInfo",
					"flowctrlDefinition",
					"flowctrlItem",
					"fsmStatus",
					"gmetaClass",
					"gmetaEp",
					"gmetaHolder",
					"gmetaHolderFsm",
					"gmetaHolderFsmStage",
					"gmetaHolderFsmTask",
					"gmetaPolicyMapElement",
					"gmetaPolicyMapHolder",
					"gmetaProp",
					"graphicsCard",
					"graphicsController",
					"hostimgPolicy",
					"hostimgTarget",
					"identIdentCtx",
					"identIdentRequest",
					"identIdentRequestFsm",
					"identIdentRequestFsmStage",
					"identIdentRequestFsmTask",
					"identMetaSystem",
					"identMetaSystemFsm",
					"identMetaSystemFsmStage",
					"identMetaSystemFsmTask",
					"identMetaVerse",
					"identRequestEp",
					"identSysInfo",
					"imgprovPolicy",
					"imgprovTarget",
					"imgsecKey",
					"imgsecPolicy",
					"initiatorFcInitiatorEp",
					"initiatorGroupEp",
					"initiatorIScsiInitiatorEp",
					"initiatorLunEp",
					"initiatorMemberEp",
					"initiatorRequestorEp",
					"initiatorRequestorGrpEp",
					"initiatorStoreEp",
					"initiatorUnitEp",
					"ipDnsSuffix",
					"ipIPv4Dns",
					"ipIPv4WinsServer",
					"ipIpV4StaticAddr",
					"ipIpV4StaticTargetAddr",
					"ipServiceIf",
					"ippoolAddr",
					"ippoolBlock",
					"ippoolIpV6Addr",
					"ippoolIpV6Block",
					"ippoolIpV6Pooled",
					"ippoolPool",
					"ippoolPoolable",
					"ippoolPooled",
					"ippoolUniverse",
					"iqnpoolAddr",
					"iqnpoolBlock",
					"iqnpoolFormat",
					"iqnpoolPool",
					"iqnpoolPoolable",
					"iqnpoolPooled",
					"iqnpoolTransportBlock",
					"iqnpoolUniverse",
					"iscsiAuthProfile",
					"licenseContents",
					"licenseDownloader",
					"licenseDownloaderFsm",
					"licenseDownloaderFsmStage",
					"licenseDownloaderFsmTask",
					"licenseEp",
					"licenseFeature",
					"licenseFeatureCapProvider",
					"licenseFeatureLine",
					"licenseFile",
					"licenseFileFsm",
					"licenseFileFsmStage",
					"licenseFileFsmTask",
					"licenseInstance",
					"licenseInstanceFsm",
					"licenseInstanceFsmStage",
					"licenseInstanceFsmTask",
					"licenseProp",
					"licenseServerHostId",
					"licenseSource",
					"licenseSourceFile",
					"lldpAcquired",
					"lsAgentPolicy",
					"lsBinding",
					"lsFcLocale",
					"lsFcZone",
					"lsFcZoneGroup",
					"lsIssues",
					"lsPower",
					"lsRequirement",
					"lsServer",
					"lsServerAssocCtx",
					"lsServerExtension",
					"lsServerFsm",
					"lsServerFsmStage",
					"lsServerFsmTask",
					"lsTier",
					"lsUuidHistory",
					"lsVConAssign",
					"lsVersionBeh",
					"lsZoneInitiatorMember",
					"lsZoneTargetMember",
					"lsbootBootSecurity",
					"lsbootDef",
					"lsbootDefaultLocalImage",
					"lsbootIScsi",
					"lsbootIScsiImagePath",
					"lsbootLan",
					"lsbootLanImagePath",
					"lsbootLocalHddImage",
					"lsbootLocalStorage",
					"lsbootPolicy",
					"lsbootSan",
					"lsbootSanCatSanImage",
					"lsbootSanCatSanImagePath",
					"lsbootSanImage",
					"lsbootSanImagePath",
					"lsbootStorage",
					"lsbootUsbExternalImage",
					"lsbootUsbFlashStorageImage",
					"lsbootUsbInternalImage",
					"lsbootVirtualMedia",
					"lsmaintAck",
					"lsmaintMaintPolicy",
					"macpoolAddr",
					"macpoolBlock",
					"macpoolFormat",
					"macpoolPool",
					"macpoolPoolable",
					"macpoolPooled",
					"macpoolUniverse",
					"managedObject",
					"memoryArray",
					"memoryArrayEnvStats",
					"memoryArrayEnvStatsHist",
					"memoryBufferUnit",
					"memoryBufferUnitEnvStats",
					"memoryBufferUnitEnvStatsHist",
					"memoryErrorStats",
					"memoryQual",
					"memoryRuntime",
					"memoryRuntimeHist",
					"memoryUnit",
					"memoryUnitEnvStats",
					"memoryUnitEnvStatsHist",
					"mgmtAccessPolicy",
					"mgmtAccessPolicyItem",
					"mgmtAccessPort",
					"mgmtBackup",
					"mgmtBackupExportExtPolicy",
					"mgmtBackupFsm",
					"mgmtBackupFsmStage",
					"mgmtBackupFsmTask",
					"mgmtBackupPolicy",
					"mgmtBackupPolicyConfig",
					"mgmtBackupPolicyFsm",
					"mgmtBackupPolicyFsmStage",
					"mgmtCfgExportPolicy",
					"mgmtCfgExportPolicyFsm",
					"mgmtCfgExportPolicyFsmStage",
					"mgmtConnection",
					"mgmtController",
					"mgmtControllerFsm",
					"mgmtControllerFsmStage",
					"mgmtControllerFsmTask",
					"mgmtEntity",
					"mgmtExportPolicyFsm",
					"mgmtExportPolicyFsmStage",
					"mgmtExportPolicyFsmTask",
					"mgmtIPv6IfAddr",
					"mgmtIPv6IfAddrFsm",
					"mgmtIPv6IfAddrFsmStage",
					"mgmtIPv6IfAddrFsmTask",
					"mgmtIPv6IfConfig",
					"mgmtIf",
					"mgmtIfFsm",
					"mgmtIfFsmStage",
					"mgmtIfFsmTask",
					"mgmtImporter",
					"mgmtImporterFsm",
					"mgmtImporterFsmStage",
					"mgmtImporterFsmTask",
					"mgmtInbandProfile",
					"mgmtIntAuthPolicy",
					"mgmtInterface",
					"mgmtPmonEntry",
					"mgmtProfDerivedInterface",
					"mgmtVnet",
					"networkElement",
					"networkIfStats",
					"networkOperLevel",
					"nfsEp",
					"nfsMountDef",
					"nfsMountDefFsm",
					"nfsMountDefFsmStage",
					"nfsMountDefFsmTask",
					"nfsMountInst",
					"nfsMountInstFsm",
					"nfsMountInstFsmStage",
					"nfsMountInstFsmTask",
					"nwctrlDefinition",
					"observe",
					"observeObserved",
					"observeObservedCont",
					"observeObservedFsm",
					"observeObservedFsmStage",
					"observeObservedFsmTask",
					"orgOrg",
					"orgSourceMask",
					"osAgent",
					"osInstance",
					"pciEquipSlot",
					"pciUnit",
					"pkiCertReq",
					"pkiEp",
					"pkiEpFsm",
					"pkiEpFsmStage",
					"pkiEpFsmTask",
					"pkiKeyRing",
					"pkiTP",
					"policyCentraleSync",
					"policyCommunication",
					"policyConfigBackup",
					"policyControlEp",
					"policyControlEpFsm",
					"policyControlEpFsmStage",
					"policyControlEpFsmTask",
					"policyControlledInstance",
					"policyControlledType",
					"policyControlledTypeFsm",
					"policyControlledTypeFsmStage",
					"policyControlledTypeFsmTask",
					"policyDateTime",
					"policyDigest",
					"policyDiscovery",
					"policyDns",
					"policyElement",
					"policyFault",
					"policyInfraFirmware",
					"policyLocalMap",
					"policyMEp",
					"policyMonitoring",
					"policyPolicyEp",
					"policyPolicyRequestor",
					"policyPolicyScope",
					"policyPolicyScopeCont",
					"policyPolicyScopeContext",
					"policyPolicyScopeFsm",
					"policyPolicyScopeFsmStage",
					"policyPolicyScopeFsmTask",
					"policyPowerMgmt",
					"policyPsu",
					"policyRefReq",
					"policySecurity",
					"portDomainEp",
					"portGroup",
					"portPIoFsm",
					"portPIoFsmStage",
					"portPIoFsmTask",
					"portTrustMode",
					"powerBudget",
					"powerChassisMember",
					"powerEp",
					"powerGroup",
					"powerGroupAdditionPolicy",
					"powerGroupQual",
					"powerGroupStats",
					"powerGroupStatsHist",
					"powerMgmtPolicy",
					"powerPlacement",
					"powerPolicy",
					"powerPrioWght",
					"powerRackUnitMember",
					"procDoer",
					"procManager",
					"procPrt",
					"procPrtCounts",
					"procStimulusCounts",
					"procSvc",
					"procTxCounts",
					"processorCore",
					"processorEnvStats",
					"processorEnvStatsHist",
					"processorErrorStats",
					"processorQual",
					"processorRuntime",
					"processorRuntimeHist",
					"processorThread",
					"processorUnit",
					"processorUnitAssocCtx",
					"qosclassDefinition",
					"qosclassDefinitionFsm",
					"qosclassDefinitionFsmStage",
					"qosclassDefinitionFsmTask",
					"qosclassEthBE",
					"qosclassEthClassified",
					"qosclassFc",
					"queryresultDependency",
					"queryresultUsage",
					"solConfig",
					"solIf",
					"solPolicy",
					"statsCollectionPolicy",
					"statsCollectionPolicyFsm",
					"statsCollectionPolicyFsmStage",
					"statsCollectionPolicyFsmTask",
					"statsHolder",
					"statsThr32Definition",
					"statsThr32Value",
					"statsThr64Definition",
					"statsThr64Value",
					"statsThrFloatDefinition",
					"statsThrFloatValue",
					"statsThresholdClass",
					"statsThresholdPolicy",
					"storageAuthKey",
					"storageConnectionDef",
					"storageConnectionPolicy",
					"storageController",
					"storageDomainEp",
					"storageDrive",
					"storageEnclosure",
					"storageEpUser",
					"storageEtherIf",
					"storageFcIf",
					"storageFcTargetEp",
					"storageFcTargetIf",
					"storageFlexFlashCard",
					"storageFlexFlashController",
					"storageFlexFlashDrive",
					"storageFlexFlashVirtualDrive",
					"storageIScsiTargetIf",
					"storageIniGroup",
					"storageInitiator",
					"storageItem",
					"storageLocalDisk",
					"storageLocalDiskConfigDef",
					"storageLocalDiskConfigPolicy",
					"storageLocalDiskPartition",
					"storageLocalDiskSlotEp",
					"storageLocalLun",
					"storageLunDisk",
					"storageMezzFlashLife",
					"storageNodeEp",
					"storageOperation",
					"storageQual",
					"storageRaidBattery",
					"storageSystem",
					"storageSystemFsm",
					"storageSystemFsmStage",
					"storageSystemFsmTask",
					"storageTransportableFlashModule",
					"storageVirtualDrive",
					"storageVsanRef",
					"swAccessDomain",
					"swAccessDomainFsm",
					"swAccessDomainFsmStage",
					"swAccessDomainFsmTask",
					"swAccessEp",
					"swCardEnvStats",
					"swCardEnvStatsHist",
					"swCmclan",
					"swEnvStats",
					"swEnvStatsHist",
					"swEthEstcEp",
					"swEthEstcPc",
					"swEthLanBorder",
					"swEthLanBorderFsm",
					"swEthLanBorderFsmStage",
					"swEthLanBorderFsmTask",
					"swEthLanEp",
					"swEthLanFlowMon",
					"swEthLanFlowMonFsm",
					"swEthLanFlowMonFsmStage",
					"swEthLanFlowMonFsmTask",
					"swEthLanMon",
					"swEthLanPc",
					"swEthMon",
					"swEthMonDestEp",
					"swEthMonFsm",
					"swEthMonFsmStage",
					"swEthMonFsmTask",
					"swEthMonSrcEp",
					"swEthTargetEp",
					"swFabricZoneNs",
					"swFabricZoneNsOverride",
					"swFcEstcEp",
					"swFcMon",
					"swFcMonDestEp",
					"swFcMonFsm",
					"swFcMonFsmStage",
					"swFcMonFsmTask",
					"swFcMonSrcEp",
					"swFcSanBorder",
					"swFcSanBorderFsm",
					"swFcSanBorderFsmStage",
					"swFcSanBorderFsmTask",
					"swFcSanEp",
					"swFcSanMon",
					"swFcSanPc",
					"swFcServerZoneGroup",
					"swFcZone",
					"swFcZoneSet",
					"swFcoeEstcEp",
					"swFcoeSanEp",
					"swFcoeSanPc",
					"swIpRoute",
					"swNFExporterRef",
					"swNetflowExporter",
					"swNetflowMonSession",
					"swNetflowMonitor",
					"swNetflowMonitorRef",
					"swNetflowRecordDef",
					"swPhys",
					"swPhysEtherEp",
					"swPhysFcEp",
					"swPhysFsm",
					"swPhysFsmStage",
					"swPhysFsmTask",
					"swSystemStats",
					"swSystemStatsHist",
					"swUlan",
					"swUtilityDomain",
					"swUtilityDomainFsm",
					"swUtilityDomainFsmStage",
					"swUtilityDomainFsmTask",
					"swVirtL3Intf",
					"swVlan",
					"swVlanGroup",
					"swVlanPortNs",
					"swVlanPortNsOverride",
					"swVlanRef",
					"swVsan",
					"swZoneInitiatorMember",
					"swZoneTargetMember",
					"swatAction",
					"swatCondition",
					"swatInjection",
					"swatResultstats",
					"swatTarget",
					"swatTrigger",
					"syntheticDirectory",
					"syntheticFile",
					"syntheticFileSystem",
					"syntheticFsObj",
					"syntheticFsObjFsm",
					"syntheticFsObjFsmStage",
					"syntheticFsObjFsmTask",
					"syntheticTime",
					"sysdebugAutoCoreFileExportTarget",
					"sysdebugAutoCoreFileExportTargetFsm",
					"sysdebugAutoCoreFileExportTargetFsmStage",
					"sysdebugAutoCoreFileExportTargetFsmTask",
					"sysdebugBackupBehavior",
					"sysdebugCore",
					"sysdebugCoreFileRepository",
					"sysdebugCoreFsm",
					"sysdebugCoreFsmStage",
					"sysdebugCoreFsmTask",
					"sysdebugEp",
					"sysdebugLogControlDestinationFile",
					"sysdebugLogControlDestinationSyslog",
					"sysdebugLogControlDomain",
					"sysdebugLogControlEp",
					"sysdebugLogControlEpFsm",
					"sysdebugLogControlEpFsmStage",
					"sysdebugLogControlEpFsmTask",
					"sysdebugLogControlModule",
					"sysdebugLogExportPolicy",
					"sysdebugLogExportPolicyFsm",
					"sysdebugLogExportPolicyFsmStage",
					"sysdebugLogExportPolicyFsmTask",
					"sysdebugLogExportStatus",
					"sysdebugMEpLog",
					"sysdebugMEpLogPolicy",
					"sysdebugManualCoreFileExportTarget",
					"sysdebugManualCoreFileExportTargetFsm",
					"sysdebugManualCoreFileExportTargetFsmStage",
					"sysdebugManualCoreFileExportTargetFsmTask",
					"sysdebugTechSupFileRepository",
					"sysdebugTechSupport",
					"sysdebugTechSupportCmdOpt",
					"sysdebugTechSupportFsm",
					"sysdebugTechSupportFsmStage",
					"sysdebugTechSupportFsmTask",
					"sysfileDigest",
					"sysfileMutation",
					"sysfileMutationFsm",
					"sysfileMutationFsmStage",
					"sysfileMutationFsmTask",
					"topMetaInf",
					"topRoot",
					"topSysDefaults",
					"topSystem",
					"trigAbsWindow",
					"trigClientToken",
					"trigLocalAbsWindow",
					"trigLocalSched",
					"trigMeta",
					"trigRecurrWindow",
					"trigSched",
					"trigTest",
					"trigTriggered",
					"uuidpoolAddr",
					"uuidpoolBlock",
					"uuidpoolFormat",
					"uuidpoolPool",
					"uuidpoolPoolable",
					"uuidpoolPooled",
					"uuidpoolUniverse",
					"versionApplication",
					"versionEp",
					"vmComputeEp",
					"vmDC",
					"vmDCOrg",
					"vmEp",
					"vmHba",
					"vmHv",
					"vmInstance",
					"vmLifeCyclePolicy",
					"vmLifeCyclePolicyFsm",
					"vmLifeCyclePolicyFsmStage",
					"vmLifeCyclePolicyFsmTask",
					"vmNic",
					"vmOrg",
					"vmSwitch",
					"vmVif",
					"vmVlan",
					"vmVnicProfCl",
					"vmVnicProfInst",
					"vmVsan",
					"vnicBootIpPolicy",
					"vnicBootTarget",
					"vnicConnDef",
					"vnicDefBeh",
					"vnicDynamicCon",
					"vnicDynamicConPolicy",
					"vnicDynamicConPolicyRef",
					"vnicDynamicIdUniverse",
					"vnicDynamicProvider",
					"vnicDynamicProviderEp",
					"vnicEthLif",
					"vnicEther",
					"vnicEtherIf",
					"vnicFc",
					"vnicFcGroupDef",
					"vnicFcGroupTempl",
					"vnicFcIf",
					"vnicFcLif",
					"vnicFcNode",
					"vnicFcOEIf",
					"vnicIPv4Dhcp",
					"vnicIPv4Dns",
					"vnicIPv4If",
					"vnicIPv4IscsiAddr",
					"vnicIPv4PooledIscsiAddr",
					"vnicIPv4StaticRoute",
					"vnicIScsi",
					"vnicIScsiAutoTargetIf",
					"vnicIScsiBootParams",
					"vnicIScsiBootVnic",
					"vnicIScsiLCP",
					"vnicIScsiNode",
					"vnicIScsiStaticTargetIf",
					"vnicInternalProfile",
					"vnicIpV4History",
					"vnicIpV4MgmtPooledAddr",
					"vnicIpV4PooledAddr",
					"vnicIpV4ProfDerivedAddr",
					"vnicIpV4StaticAddr",
					"vnicIpV6History",
					"vnicIpV6MgmtPooledAddr",
					"vnicIpV6StaticAddr",
					"vnicIpc",
					"vnicIpcIf",
					"vnicIqnHistory",
					"vnicLanConnPolicy",
					"vnicLanConnTempl",
					"vnicLifVlan",
					"vnicLifVsan",
					"vnicLun",
					"vnicMacHistory",
					"vnicOProfileAlias",
					"vnicProfile",
					"vnicProfileAlias",
					"vnicProfileRef",
					"vnicProfileSet",
					"vnicProfileSetFsm",
					"vnicProfileSetFsmStage",
					"vnicProfileSetFsmTask",
					"vnicRackServerDiscoveryProfile",
					"vnicSanConnPolicy",
					"vnicSanConnTempl",
					"vnicScsi",
					"vnicScsiIf",
					"vnicUsnicConPolicy",
					"vnicUsnicConPolicyRef",
					"vnicVhbaBehPolicy",
					"vnicVlan",
					"vnicVmqConPolicy",
					"vnicVmqConPolicyRef",
					"vnicVnicBehPolicy",
					"vnicWwnnHistory",
					"vnicWwpnHistory",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class Dn(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Dn")
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the Dn object."""
		if w is None:
			x=Element("dn")
		else:
			if (elementName == None):
				x = SubElement(w,"dn")
			else:
				x = SubElement(w,elementName)
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the Dn object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the Dn object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the Dn object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class DnSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "DnSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the DnSet object."""
		if w is None:
			x=Element("dnSet")
		else:
			if (elementName == None):
				x = SubElement(w,"dnSet")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the DnSet object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the DnSet object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the DnSet object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"dn",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class EqFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "EqFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the EqFilter object."""
		if w is None:
			x=Element("eq")
		else:
			if (elementName == None):
				x = SubElement(w,"eq")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the EqFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the EqFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the EqFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class FilterFilter(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "FilterFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the FilterFilter object."""
		if w is None:
			x=Element("filter")
		else:
			if (elementName == None):
				x = SubElement(w,"filter")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the FilterFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the FilterFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the FilterFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class GeFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "GeFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the GeFilter object."""
		if w is None:
			x=Element("ge")
		else:
			if (elementName == None):
				x = SubElement(w,"ge")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the GeFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the GeFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the GeFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class GtFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "GtFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the GtFilter object."""
		if w is None:
			x=Element("gt")
		else:
			if (elementName == None):
				x = SubElement(w,"gt")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the GtFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the GtFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the GtFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class Id(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Id")
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the Id object."""
		if w is None:
			x=Element("id")
		else:
			if (elementName == None):
				x = SubElement(w,"id")
			else:
				x = SubElement(w,elementName)
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the Id object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the Id object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the Id object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class IdSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "IdSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the IdSet object."""
		if w is None:
			x=Element("idSet")
		else:
			if (elementName == None):
				x = SubElement(w,"idSet")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the IdSet object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the IdSet object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the IdSet object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"id",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class LeFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "LeFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the LeFilter object."""
		if w is None:
			x=Element("le")
		else:
			if (elementName == None):
				x = SubElement(w,"le")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the LeFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the LeFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the LeFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class LtFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "LtFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the LtFilter object."""
		if w is None:
			x=Element("lt")
		else:
			if (elementName == None):
				x = SubElement(w,"lt")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the LtFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the LtFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the LtFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class NeFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "NeFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the NeFilter object."""
		if w is None:
			x=Element("ne")
		else:
			if (elementName == None):
				x = SubElement(w,"ne")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the NeFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the NeFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the NeFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class NotFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "NotFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the NotFilter object."""
		if w is None:
			x=Element("not")
		else:
			if (elementName == None):
				x = SubElement(w,"not")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the NotFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the NotFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the NotFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class OrFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "OrFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the OrFilter object."""
		if w is None:
			x=Element("or")
		else:
			if (elementName == None):
				x = SubElement(w,"or")
			else:
				x = SubElement(w,elementName)
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the OrFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the OrFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the OrFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class Pair(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Pair")
		self.Key = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the Pair object."""
		if w is None:
			x=Element("pair")
		else:
			if (elementName == None):
				x = SubElement(w,"pair")
			else:
				x = SubElement(w,elementName)
		x.set("key", getattr(self,"Key"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the Pair object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the Pair object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the Pair object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
					"aaaAuthRealm",
					"aaaAuthRealmFsm",
					"aaaAuthRealmFsmStage",
					"aaaCimcSession",
					"aaaConsoleAuth",
					"aaaDefaultAuth",
					"aaaDomain",
					"aaaDomainAuth",
					"aaaEpAuthProfile",
					"aaaEpFsm",
					"aaaEpFsmStage",
					"aaaEpFsmTask",
					"aaaEpLogin",
					"aaaEpUser",
					"aaaExtMgmtCutThruTkn",
					"aaaLdapEp",
					"aaaLdapEpFsm",
					"aaaLdapEpFsmStage",
					"aaaLdapGroup",
					"aaaLdapGroupRule",
					"aaaLdapProvider",
					"aaaLocale",
					"aaaLog",
					"aaaModLR",
					"aaaOrg",
					"aaaPreLoginBanner",
					"aaaProviderGroup",
					"aaaProviderRef",
					"aaaPwdProfile",
					"aaaRadiusEp",
					"aaaRadiusEpFsm",
					"aaaRadiusEpFsmStage",
					"aaaRadiusProvider",
					"aaaRealmFsm",
					"aaaRealmFsmStage",
					"aaaRealmFsmTask",
					"aaaRemoteUser",
					"aaaRole",
					"aaaSession",
					"aaaSessionInfo",
					"aaaSessionInfoTable",
					"aaaSessionLR",
					"aaaShellLogin",
					"aaaSshAuth",
					"aaaTacacsPlusEp",
					"aaaTacacsPlusEpFsm",
					"aaaTacacsPlusEpFsmStage",
					"aaaTacacsPlusProvider",
					"aaaUser",
					"aaaUserData",
					"aaaUserEp",
					"aaaUserEpFsm",
					"aaaUserEpFsmStage",
					"aaaUserEpFsmTask",
					"aaaUserLocale",
					"aaaUserRole",
					"aaaWebLogin",
					"adaptorCapQual",
					"adaptorCapSpec",
					"adaptorDiagCap",
					"adaptorEthArfsProfile",
					"adaptorEthCompQueueProfile",
					"adaptorEthFailoverProfile",
					"adaptorEthInterruptProfile",
					"adaptorEthOffloadProfile",
					"adaptorEthPortBySizeLargeStats",
					"adaptorEthPortBySizeLargeStatsHist",
					"adaptorEthPortBySizeSmallStats",
					"adaptorEthPortBySizeSmallStatsHist",
					"adaptorEthPortErrStats",
					"adaptorEthPortErrStatsHist",
					"adaptorEthPortMcastStats",
					"adaptorEthPortMcastStatsHist",
					"adaptorEthPortOutsizedStats",
					"adaptorEthPortOutsizedStatsHist",
					"adaptorEthPortStats",
					"adaptorEthPortStatsHist",
					"adaptorEthRecvQueueProfile",
					"adaptorEthWorkQueueProfile",
					"adaptorEtherIfStats",
					"adaptorEtherIfStatsHist",
					"adaptorExtEthIf",
					"adaptorExtEthIfFsm",
					"adaptorExtEthIfFsmStage",
					"adaptorExtEthIfFsmTask",
					"adaptorExtEthIfPc",
					"adaptorExtEthIfPcEp",
					"adaptorExtIpV6RssHashProfile",
					"adaptorFamilyTypeDef",
					"adaptorFcCdbWorkQueueProfile",
					"adaptorFcErrorRecoveryProfile",
					"adaptorFcIfEventStats",
					"adaptorFcIfEventStatsHist",
					"adaptorFcIfFC4Stats",
					"adaptorFcIfFC4StatsHist",
					"adaptorFcIfFrameStats",
					"adaptorFcIfFrameStatsHist",
					"adaptorFcInterruptProfile",
					"adaptorFcOEIf",
					"adaptorFcPortFLogiProfile",
					"adaptorFcPortPLogiProfile",
					"adaptorFcPortProfile",
					"adaptorFcPortStats",
					"adaptorFcPortStatsHist",
					"adaptorFcRecvQueueProfile",
					"adaptorFcWorkQueueProfile",
					"adaptorFruCapProvider",
					"adaptorFruCapRef",
					"adaptorFwCapProvider",
					"adaptorHostEthIf",
					"adaptorHostEthIfFsm",
					"adaptorHostEthIfFsmStage",
					"adaptorHostEthIfFsmTask",
					"adaptorHostEthIfProfile",
					"adaptorHostFcIf",
					"adaptorHostFcIfFsm",
					"adaptorHostFcIfFsmStage",
					"adaptorHostFcIfFsmTask",
					"adaptorHostFcIfProfile",
					"adaptorHostIscsiIf",
					"adaptorHostIscsiIfProfile",
					"adaptorHostMgmtCap",
					"adaptorHostServiceEthIf",
					"adaptorHostethHwAddrCap",
					"adaptorHostfcHwAddrCap",
					"adaptorIScsiCap",
					"adaptorIpV4RssHashProfile",
					"adaptorIpV6RssHashProfile",
					"adaptorIscsiAuth",
					"adaptorIscsiProt",
					"adaptorIscsiTargetIf",
					"adaptorLanCap",
					"adaptorLldpCap",
					"adaptorMenloBaseErrorStats",
					"adaptorMenloBaseErrorStatsHist",
					"adaptorMenloDcePortStats",
					"adaptorMenloDcePortStatsHist",
					"adaptorMenloEthErrorStats",
					"adaptorMenloEthErrorStatsHist",
					"adaptorMenloEthStats",
					"adaptorMenloEthStatsHist",
					"adaptorMenloFcErrorStats",
					"adaptorMenloFcErrorStatsHist",
					"adaptorMenloFcStats",
					"adaptorMenloFcStatsHist",
					"adaptorMenloHostPortStats",
					"adaptorMenloHostPortStatsHist",
					"adaptorMenloMcpuErrorStats",
					"adaptorMenloMcpuErrorStatsHist",
					"adaptorMenloMcpuStats",
					"adaptorMenloMcpuStatsHist",
					"adaptorMenloNetEgStats",
					"adaptorMenloNetEgStatsHist",
					"adaptorMenloNetInStats",
					"adaptorMenloNetInStatsHist",
					"adaptorMenloQErrorStats",
					"adaptorMenloQErrorStatsHist",
					"adaptorMenloQStats",
					"adaptorMenloQStatsHist",
					"adaptorNwMgmtCap",
					"adaptorProtocolProfile",
					"adaptorQual",
					"adaptorRssProfile",
					"adaptorSanCap",
					"adaptorUnit",
					"adaptorUnitAssocCtx",
					"adaptorUnitExtn",
					"adaptorUplinkHwAddrCap",
					"adaptorUsnicConnDef",
					"adaptorVlan",
					"adaptorVnicStats",
					"adaptorVnicStatsHist",
					"adaptorVsan",
					"apeControllerChassis",
					"apeControllerEeprom",
					"apeControllerManager",
					"apeDcosAgManager",
					"apeFru",
					"apeHostAgent",
					"apeLANBoot",
					"apeLocalDiskBoot",
					"apeManager",
					"apeMc",
					"apeMcTable",
					"apeMenlo",
					"apeMenloVnic",
					"apeMenloVnicStats",
					"apeNicAgManager",
					"apePalo",
					"apePaloVnic",
					"apePaloVnicStats",
					"apeParam",
					"apeReading",
					"apeSANBoot",
					"apeSdr",
					"apeSwitchFirmwareInv",
					"apeVirtualMediaBoot",
					"biosBOT",
					"biosBootDev",
					"biosBootDevGrp",
					"biosFeatureRef",
					"biosParameterRef",
					"biosRef",
					"biosSettingRef",
					"biosSettings",
					"biosUnit",
					"biosVIdentityParams",
					"biosVProfile",
					"biosVfACPI10Support",
					"biosVfAllUSBDevices",
					"biosVfAssertNMIOnPERR",
					"biosVfAssertNMIOnSERR",
					"biosVfBootOptionRetry",
					"biosVfCPUPerformance",
					"biosVfConsoleRedirection",
					"biosVfCoreMultiProcessing",
					"biosVfDRAMClockThrottling",
					"biosVfDirectCacheAccess",
					"biosVfDramRefreshRate",
					"biosVfEnhancedIntelSpeedStepTech",
					"biosVfExecuteDisableBit",
					"biosVfFRB2Timer",
					"biosVfFrequencyFloorOverride",
					"biosVfFrontPanelLockout",
					"biosVfIntelEntrySASRAIDModule",
					"biosVfIntelHyperThreadingTech",
					"biosVfIntelTurboBoostTech",
					"biosVfIntelVTForDirectedIO",
					"biosVfIntelVirtualizationTechnology",
					"biosVfInterleaveConfiguration",
					"biosVfLOMPortsConfiguration",
					"biosVfLocalX2Apic",
					"biosVfLvDIMMSupport",
					"biosVfMaxVariableMTRRSetting",
					"biosVfMaximumMemoryBelow4GB",
					"biosVfMemoryMappedIOAbove4GB",
					"biosVfMirroringMode",
					"biosVfNUMAOptimized",
					"biosVfOSBootWatchdogTimer",
					"biosVfOSBootWatchdogTimerPolicy",
					"biosVfOSBootWatchdogTimerTimeout",
					"biosVfOnboardSATAController",
					"biosVfOnboardStorage",
					"biosVfOptionROMEnable",
					"biosVfOptionROMLoad",
					"biosVfPCISlotLinkSpeed",
					"biosVfPCISlotOptionROMEnable",
					"biosVfPOSTErrorPause",
					"biosVfPSTATECoordination",
					"biosVfPackageCStateLimit",
					"biosVfProcessorC1E",
					"biosVfProcessorC3Report",
					"biosVfProcessorC6Report",
					"biosVfProcessorC7Report",
					"biosVfProcessorCState",
					"biosVfProcessorEnergyConfiguration",
					"biosVfProcessorPrefetchConfig",
					"biosVfQPILinkFrequencySelect",
					"biosVfQuietBoot",
					"biosVfResumeOnACPowerLoss",
					"biosVfScrubPolicies",
					"biosVfSelectMemoryRASConfiguration",
					"biosVfSerialPortAEnable",
					"biosVfSparingMode",
					"biosVfSriovConfig",
					"biosVfUCSMBootModeControl",
					"biosVfUCSMBootOrderRuleControl",
					"biosVfUEFIOSUseLegacyVideo",
					"biosVfUSBBootConfig",
					"biosVfUSBFrontPanelAccessLock",
					"biosVfUSBPortConfiguration",
					"biosVfUSBSystemIdlePowerOptimizingSetting",
					"biosVfVGAPriority",
					"bmcSELCounter",
					"callhomeDest",
					"callhomeEp",
					"callhomeEpFsm",
					"callhomeEpFsmStage",
					"callhomeEpFsmTask",
					"callhomePeriodicSystemInventory",
					"callhomePolicy",
					"callhomeProfile",
					"callhomeSmtp",
					"callhomeSource",
					"callhomeTestAlert",
					"capabilityCatalogue",
					"capabilityCatalogueFsm",
					"capabilityCatalogueFsmStage",
					"capabilityCatalogueFsmTask",
					"capabilityEp",
					"capabilityFeatureLimits",
					"capabilityMgmtExtension",
					"capabilityMgmtExtensionFsm",
					"capabilityMgmtExtensionFsmStage",
					"capabilityMgmtExtensionFsmTask",
					"capabilityNetworkLimits",
					"capabilityStorageLimits",
					"capabilitySystemLimits",
					"capabilityUpdate",
					"capabilityUpdater",
					"capabilityUpdaterFsm",
					"capabilityUpdaterFsmStage",
					"capabilityUpdaterFsmTask",
					"changeChangedObjectRef",
					"cimcvmediaActualMountEntry",
					"cimcvmediaActualMountList",
					"cimcvmediaConfigMountEntry",
					"cimcvmediaExtMgmtRuleEntry",
					"cimcvmediaMountConfigDef",
					"cimcvmediaMountConfigPolicy",
					"clitestTypeTest",
					"clitestTypeTest2",
					"clitestTypeTestChild",
					"commCimcWebService",
					"commCimxml",
					"commDateTime",
					"commDns",
					"commDnsProvider",
					"commEvtChannel",
					"commHttp",
					"commHttps",
					"commNtpProvider",
					"commShellSvcLimits",
					"commSmashCLP",
					"commSnmp",
					"commSnmpTrap",
					"commSnmpUser",
					"commSsh",
					"commSvcEp",
					"commSvcEpFsm",
					"commSvcEpFsmStage",
					"commSvcEpFsmTask",
					"commSyslog",
					"commSyslogClient",
					"commSyslogConsole",
					"commSyslogFile",
					"commSyslogMonitor",
					"commSyslogSource",
					"commTelnet",
					"commWebChannel",
					"commWebSvcLimits",
					"commWsman",
					"commXmlClConnPolicy",
					"computeAutoconfigPolicy",
					"computeBlade",
					"computeBladeDiscPolicy",
					"computeBladeFsm",
					"computeBladeFsmStage",
					"computeBladeFsmTask",
					"computeBladeInheritPolicy",
					"computeBoard",
					"computeBoardConnector",
					"computeBoardController",
					"computeChassisConnPolicy",
					"computeChassisDiscPolicy",
					"computeChassisQual",
					"computeDefaults",
					"computeExtBoard",
					"computeFwSyncAck",
					"computeHealthLedSensorAlarm",
					"computeIOHub",
					"computeIOHubEnvStats",
					"computeIOHubEnvStatsHist",
					"computeKvmMgmtPolicy",
					"computeMbPowerStats",
					"computeMbPowerStatsHist",
					"computeMbTempStats",
					"computeMbTempStatsHist",
					"computeMemoryConfigPolicy",
					"computeMemoryConfiguration",
					"computeMemoryUnitConstraintDef",
					"computePCIeFatalCompletionStats",
					"computePCIeFatalProtocolStats",
					"computePCIeFatalReceiveStats",
					"computePCIeFatalStats",
					"computePciCap",
					"computePciSlotScanDef",
					"computePhysicalAssocCtx",
					"computePhysicalFsm",
					"computePhysicalFsmStage",
					"computePhysicalFsmTask",
					"computePhysicalQual",
					"computePlatform",
					"computePnuOSImage",
					"computePool",
					"computePoolPolicyRef",
					"computePoolable",
					"computePooledRackUnit",
					"computePooledSlot",
					"computePoolingPolicy",
					"computePsuControl",
					"computePsuPolicy",
					"computeQual",
					"computeRackQual",
					"computeRackUnit",
					"computeRackUnitFsm",
					"computeRackUnitFsmStage",
					"computeRackUnitFsmTask",
					"computeRackUnitMbTempStats",
					"computeRackUnitMbTempStatsHist",
					"computeRtcBattery",
					"computeScrubPolicy",
					"computeServerDiscPolicy",
					"computeServerDiscPolicyFsm",
					"computeServerDiscPolicyFsmStage",
					"computeServerDiscPolicyFsmTask",
					"computeServerMgmtPolicy",
					"computeSlotQual",
					"configImpact",
					"configManagedEpImpactResponse",
					"configSorter",
					"dcxFcoeVifEp",
					"dcxNs",
					"dcxUniverse",
					"dcxVIf",
					"dcxVc",
					"dcxVifEp",
					"dhcpAcquired",
					"dhcpInst",
					"dhcpLease",
					"diagBladeTest",
					"diagNetworkTest",
					"diagRslt",
					"diagRunPolicy",
					"diagSrvCapProvider",
					"diagSrvCtrl",
					"domainEnvironmentFeature",
					"domainEnvironmentFeatureCont",
					"domainEnvironmentParam",
					"domainNetworkFeature",
					"domainNetworkFeatureCont",
					"domainNetworkParam",
					"domainServerFeature",
					"domainServerFeatureCont",
					"domainServerParam",
					"domainStorageFeature",
					"domainStorageFeatureCont",
					"domainStorageParam",
					"dpsecMac",
					"epqosDefinition",
					"epqosDefinitionDelTask",
					"epqosDefinitionDelTaskFsm",
					"epqosDefinitionDelTaskFsmStage",
					"epqosDefinitionDelTaskFsmTask",
					"epqosDefinitionFsm",
					"epqosDefinitionFsmStage",
					"epqosDefinitionFsmTask",
					"epqosEgress",
					"equipmentAdaptorConnDef",
					"equipmentAdaptorDef",
					"equipmentAdvancedBootOrder",
					"equipmentBaseBoardCapProvider",
					"equipmentBeaconCapProvider",
					"equipmentBeaconLed",
					"equipmentBeaconLedFsm",
					"equipmentBeaconLedFsmStage",
					"equipmentBeaconLedFsmTask",
					"equipmentBiosDef",
					"equipmentBladeAGLibrary",
					"equipmentBladeAggregationCapRef",
					"equipmentBladeBiosCapProvider",
					"equipmentBladeCapProvider",
					"equipmentBladeConnDef",
					"equipmentBladeIOMConnDef",
					"equipmentBoardControllerDef",
					"equipmentCatalogCapProvider",
					"equipmentChassis",
					"equipmentChassisCapProvider",
					"equipmentChassisFsm",
					"equipmentChassisFsmStage",
					"equipmentChassisFsmTask",
					"equipmentChassisStats",
					"equipmentChassisStatsHist",
					"equipmentCimcVmedia",
					"equipmentDbgPluginCapProvider",
					"equipmentDimmEntry",
					"equipmentDimmMapping",
					"equipmentDiscoveryCap",
					"equipmentDowngradeConstraint",
					"equipmentFan",
					"equipmentFanModule",
					"equipmentFanModuleCapProvider",
					"equipmentFanModuleDef",
					"equipmentFanModuleStats",
					"equipmentFanModuleStatsHist",
					"equipmentFanStats",
					"equipmentFanStatsHist",
					"equipmentFex",
					"equipmentFexCapProvider",
					"equipmentFexEnvStats",
					"equipmentFexEnvStatsHist",
					"equipmentFexFsm",
					"equipmentFexFsmStage",
					"equipmentFexFsmTask",
					"equipmentFexPowerSummary",
					"equipmentFexPowerSummaryHist",
					"equipmentFexPsuInputStats",
					"equipmentFexPsuInputStatsHist",
					"equipmentFirmwareConstraint",
					"equipmentFlashLife",
					"equipmentGemCapProvider",
					"equipmentGemPortCap",
					"equipmentGraphicsCardCapProvider",
					"equipmentGraphicsCardCapRef",
					"equipmentHDDFaultMonDef",
					"equipmentHealthLed",
					"equipmentHostIfCapProvider",
					"equipmentIOCard",
					"equipmentIOCardCapProvider",
					"equipmentIOCardFsm",
					"equipmentIOCardFsmStage",
					"equipmentIOCardFsmTask",
					"equipmentIOCardStats",
					"equipmentIOCardStatsHist",
					"equipmentIOCardTypeDef",
					"equipmentInbandMgmtCap",
					"equipmentIndicatorLed",
					"equipmentKvmMgmtCap",
					"equipmentLocalDiskCapProvider",
					"equipmentLocalDiskControllerCapProvider",
					"equipmentLocalDiskControllerCapRef",
					"equipmentLocalDiskControllerDef",
					"equipmentLocalDiskDef",
					"equipmentLocatorLed",
					"equipmentLocatorLedFsm",
					"equipmentLocatorLedFsmStage",
					"equipmentLocatorLedFsmTask",
					"equipmentManufacturingDef",
					"equipmentMemoryUnitCapProvider",
					"equipmentMemoryUnitDiscoveryModifierDef",
					"equipmentMgmtCapProvider",
					"equipmentMgmtExtCapProvider",
					"equipmentNetworkElementFanStats",
					"equipmentNetworkElementFanStatsHist",
					"equipmentPOST",
					"equipmentPOSTCode",
					"equipmentPOSTCodeReporter",
					"equipmentPOSTCodeTemplate",
					"equipmentPciDef",
					"equipmentPhysDevicesPerBoard",
					"equipmentPhysicalDef",
					"equipmentPicture",
					"equipmentPortGroupAggregationDef",
					"equipmentPortGroupDef",
					"equipmentPortGroupSwComplexDef",
					"equipmentPortSwComplexRef",
					"equipmentProcessorUnitCapProvider",
					"equipmentProcessorUnitDef",
					"equipmentPsu",
					"equipmentPsuCapProvider",
					"equipmentPsuDef",
					"equipmentPsuInputStats",
					"equipmentPsuInputStatsHist",
					"equipmentPsuOutputStats",
					"equipmentPsuOutputStatsHist",
					"equipmentPsuStats",
					"equipmentPsuStatsHist",
					"equipmentRackFanModuleDef",
					"equipmentRackUnitCapProvider",
					"equipmentRackUnitFanStats",
					"equipmentRackUnitFanStatsHist",
					"equipmentRackUnitPsuStats",
					"equipmentRackUnitPsuStatsHist",
					"equipmentRaidDef",
					"equipmentSecureBoot",
					"equipmentServerFeatureCap",
					"equipmentServiceDef",
					"equipmentSlotArray",
					"equipmentSlotArrayRef",
					"equipmentSwitchCap",
					"equipmentSwitchCapProvider",
					"equipmentSwitchCard",
					"equipmentTpm",
					"equipmentTpmCapProvider",
					"equipmentUnifiedPortCapProvider",
					"equipmentVersionConstraint",
					"equipmentXcvr",
					"etherErrStats",
					"etherErrStatsHist",
					"etherFcoeInterfaceStats",
					"etherFcoeInterfaceStatsHist",
					"etherLossStats",
					"etherLossStatsHist",
					"etherNicIfConfig",
					"etherPIo",
					"etherPIoEndPoint",
					"etherPIoFsm",
					"etherPIoFsmStage",
					"etherPauseStats",
					"etherPauseStatsHist",
					"etherPortChanIdElem",
					"etherPortChanIdUniverse",
					"etherRxStats",
					"etherRxStatsHist",
					"etherServerIntFIo",
					"etherServerIntFIoFsm",
					"etherServerIntFIoFsmStage",
					"etherServerIntFIoFsmTask",
					"etherServerIntFIoPc",
					"etherServerIntFIoPcEp",
					"etherSwIfConfig",
					"etherSwitchIntFIo",
					"etherSwitchIntFIoPc",
					"etherSwitchIntFIoPcEp",
					"etherTxStats",
					"etherTxStatsHist",
					"eventEpCtrl",
					"eventHolder",
					"eventInst",
					"eventLog",
					"eventPolicy",
					"eventRecord",
					"extmgmtArpTargets",
					"extmgmtGatewayPing",
					"extmgmtIf",
					"extmgmtIfMonPolicy",
					"extmgmtMiiStatus",
					"extmgmtNdiscTargets",
					"extpolClient",
					"extpolClientCont",
					"extpolController",
					"extpolControllerCont",
					"extpolEp",
					"extpolEpFsm",
					"extpolEpFsmStage",
					"extpolEpFsmTask",
					"extpolProvider",
					"extpolProviderCont",
					"extpolProviderFsm",
					"extpolProviderFsmStage",
					"extpolProviderFsmTask",
					"extpolRegistry",
					"extpolRegistryFsm",
					"extpolRegistryFsmStage",
					"extpolRegistryFsmTask",
					"extpolSystemContext",
					"extvmmEp",
					"extvmmEpFsm",
					"extvmmEpFsmStage",
					"extvmmEpFsmTask",
					"extvmmFNDReference",
					"extvmmFabricNetwork",
					"extvmmFabricNetworkDefinition",
					"extvmmKeyInst",
					"extvmmKeyRing",
					"extvmmKeyStore",
					"extvmmKeyStoreFsm",
					"extvmmKeyStoreFsmStage",
					"extvmmKeyStoreFsmTask",
					"extvmmMasterExtKey",
					"extvmmMasterExtKeyFsm",
					"extvmmMasterExtKeyFsmStage",
					"extvmmMasterExtKeyFsmTask",
					"extvmmNetworkSets",
					"extvmmNetworkSetsFsm",
					"extvmmNetworkSetsFsmStage",
					"extvmmNetworkSetsFsmTask",
					"extvmmProvider",
					"extvmmProviderFsm",
					"extvmmProviderFsmStage",
					"extvmmProviderFsmTask",
					"extvmmSwitchDelTask",
					"extvmmSwitchDelTaskFsm",
					"extvmmSwitchDelTaskFsmStage",
					"extvmmSwitchDelTaskFsmTask",
					"extvmmSwitchSet",
					"extvmmUpLinkPP",
					"extvmmVMNDRef",
					"extvmmVMNetwork",
					"extvmmVMNetworkDefinition",
					"extvmmVMNetworkSets",
					"fabricBHVlan",
					"fabricCdpLinkPolicy",
					"fabricChangedObjectRef",
					"fabricChassisEp",
					"fabricComputePhEp",
					"fabricComputeSlotEp",
					"fabricComputeSlotEpFsm",
					"fabricComputeSlotEpFsmStage",
					"fabricComputeSlotEpFsmTask",
					"fabricDceSrv",
					"fabricDceSwSrv",
					"fabricDceSwSrvEp",
					"fabricDceSwSrvPc",
					"fabricDceSwSrvPcEp",
					"fabricEp",
					"fabricEpMgr",
					"fabricEpMgrFsm",
					"fabricEpMgrFsmStage",
					"fabricEpMgrFsmTask",
					"fabricEthEstc",
					"fabricEthEstcCloud",
					"fabricEthEstcEp",
					"fabricEthEstcPc",
					"fabricEthEstcPcEp",
					"fabricEthFlowMonLan",
					"fabricEthLan",
					"fabricEthLanEp",
					"fabricEthLanFlowMonitoring",
					"fabricEthLanPc",
					"fabricEthLanPcEp",
					"fabricEthLinkProfile",
					"fabricEthMon",
					"fabricEthMonDestEp",
					"fabricEthMonFiltEp",
					"fabricEthMonFiltRef",
					"fabricEthMonLan",
					"fabricEthMonSrcEp",
					"fabricEthMonSrcRef",
					"fabricEthTargetEp",
					"fabricEthVlanPc",
					"fabricEthVlanPortEp",
					"fabricFcEstc",
					"fabricFcEstcCloud",
					"fabricFcEstcEp",
					"fabricFcMon",
					"fabricFcMonDestEp",
					"fabricFcMonFiltEp",
					"fabricFcMonFiltRef",
					"fabricFcMonSan",
					"fabricFcMonSrcEp",
					"fabricFcMonSrcRef",
					"fabricFcSan",
					"fabricFcSanEp",
					"fabricFcSanPc",
					"fabricFcSanPcEp",
					"fabricFcVsanPc",
					"fabricFcVsanPortEp",
					"fabricFcoeEstcEp",
					"fabricFcoeSanEp",
					"fabricFcoeSanPc",
					"fabricFcoeSanPcEp",
					"fabricFcoeVsanPc",
					"fabricFcoeVsanPortEp",
					"fabricFlowMonDefinition",
					"fabricFlowMonExporterProfile",
					"fabricIf",
					"fabricLacpPolicy",
					"fabricLanAccessMgr",
					"fabricLanCloud",
					"fabricLanCloudFsm",
					"fabricLanCloudFsmStage",
					"fabricLanCloudFsmTask",
					"fabricLanMonCloud",
					"fabricLanPinGroup",
					"fabricLanPinTarget",
					"fabricLastAckedSlot",
					"fabricLocale",
					"fabricMulticastPolicy",
					"fabricNetGroup",
					"fabricNetflowCollector",
					"fabricNetflowIPv4Addr",
					"fabricNetflowMonExporter",
					"fabricNetflowMonExporterRef",
					"fabricNetflowMonSession",
					"fabricNetflowMonSrcEp",
					"fabricNetflowMonSrcRef",
					"fabricNetflowMonitor",
					"fabricNetflowMonitorRef",
					"fabricNetflowTimeoutPolicy",
					"fabricOrgVlanPolicy",
					"fabricPath",
					"fabricPathConn",
					"fabricPathEp",
					"fabricPoolableVlan",
					"fabricPooledVlan",
					"fabricSanCloud",
					"fabricSanCloudFsm",
					"fabricSanCloudFsmStage",
					"fabricSanCloudFsmTask",
					"fabricSanMonCloud",
					"fabricSanPinGroup",
					"fabricSanPinTarget",
					"fabricSwChPhEp",
					"fabricUdldLinkPolicy",
					"fabricUdldPolicy",
					"fabricVCon",
					"fabricVConProfile",
					"fabricVlan",
					"fabricVlanEp",
					"fabricVlanGroupReq",
					"fabricVlanPermit",
					"fabricVlanReq",
					"fabricVnetEpSyncEp",
					"fabricVnetEpSyncEpFsm",
					"fabricVnetEpSyncEpFsmStage",
					"fabricVnetEpSyncEpFsmTask",
					"fabricVsan",
					"fabricVsanEp",
					"fabricVsanMembership",
					"fabricZoneIdUniverse",
					"faultAffectedClass",
					"faultHolder",
					"faultInst",
					"faultLocalTypedHolder",
					"faultPolicy",
					"faultSuppressPolicy",
					"faultSuppressPolicyItem",
					"faultSuppressTask",
					"fcErrStats",
					"fcErrStatsHist",
					"fcNicIfConfig",
					"fcPIo",
					"fcPIoFsm",
					"fcPIoFsmStage",
					"fcStats",
					"fcStatsHist",
					"fcSwIfConfig",
					"fcpoolAddr",
					"fcpoolBlock",
					"fcpoolBootTarget",
					"fcpoolFormat",
					"fcpoolInitiator",
					"fcpoolInitiatorEp",
					"fcpoolInitiators",
					"fcpoolPoolable",
					"fcpoolUniverse",
					"firmwareAck",
					"firmwareAutoSyncPolicy",
					"firmwareBlade",
					"firmwareBootDefinition",
					"firmwareBootUnit",
					"firmwareBundleInfo",
					"firmwareBundleInfoDigest",
					"firmwareBundleType",
					"firmwareBundleTypeCapProvider",
					"firmwareCatalogPack",
					"firmwareCatalogue",
					"firmwareCompSource",
					"firmwareCompTarget",
					"firmwareComputeHostPack",
					"firmwareComputeMgmtPack",
					"firmwareDependency",
					"firmwareDistImage",
					"firmwareDistributable",
					"firmwareDistributableFsm",
					"firmwareDistributableFsmStage",
					"firmwareDistributableFsmTask",
					"firmwareDownloader",
					"firmwareDownloaderFsm",
					"firmwareDownloaderFsmStage",
					"firmwareDownloaderFsmTask",
					"firmwareHost",
					"firmwareHostPackModImpact",
					"firmwareImage",
					"firmwareImageFsm",
					"firmwareImageFsmStage",
					"firmwareImageFsmTask",
					"firmwareImageLock",
					"firmwareInfra",
					"firmwareInfraPack",
					"firmwareInstallImpact",
					"firmwareInstallable",
					"firmwarePackItem",
					"firmwareRack",
					"firmwareRunning",
					"firmwareSpec",
					"firmwareStatus",
					"firmwareSystem",
					"firmwareSystemCompCheckResult",
					"firmwareSystemFsm",
					"firmwareSystemFsmStage",
					"firmwareSystemFsmTask",
					"firmwareType",
					"firmwareUcscInfo",
					"firmwareUpdatable",
					"firmwareUpgradeConstraint",
					"firmwareUpgradeDetail",
					"firmwareUpgradeInfo",
					"flowctrlDefinition",
					"flowctrlItem",
					"fsmStatus",
					"gmetaClass",
					"gmetaEp",
					"gmetaHolder",
					"gmetaHolderFsm",
					"gmetaHolderFsmStage",
					"gmetaHolderFsmTask",
					"gmetaPolicyMapElement",
					"gmetaPolicyMapHolder",
					"gmetaProp",
					"graphicsCard",
					"graphicsController",
					"hostimgPolicy",
					"hostimgTarget",
					"identIdentCtx",
					"identIdentRequest",
					"identIdentRequestFsm",
					"identIdentRequestFsmStage",
					"identIdentRequestFsmTask",
					"identMetaSystem",
					"identMetaSystemFsm",
					"identMetaSystemFsmStage",
					"identMetaSystemFsmTask",
					"identMetaVerse",
					"identRequestEp",
					"identSysInfo",
					"imgprovPolicy",
					"imgprovTarget",
					"imgsecKey",
					"imgsecPolicy",
					"initiatorFcInitiatorEp",
					"initiatorGroupEp",
					"initiatorIScsiInitiatorEp",
					"initiatorLunEp",
					"initiatorMemberEp",
					"initiatorRequestorEp",
					"initiatorRequestorGrpEp",
					"initiatorStoreEp",
					"initiatorUnitEp",
					"ipDnsSuffix",
					"ipIPv4Dns",
					"ipIPv4WinsServer",
					"ipIpV4StaticAddr",
					"ipIpV4StaticTargetAddr",
					"ipServiceIf",
					"ippoolAddr",
					"ippoolBlock",
					"ippoolIpV6Addr",
					"ippoolIpV6Block",
					"ippoolIpV6Pooled",
					"ippoolPool",
					"ippoolPoolable",
					"ippoolPooled",
					"ippoolUniverse",
					"iqnpoolAddr",
					"iqnpoolBlock",
					"iqnpoolFormat",
					"iqnpoolPool",
					"iqnpoolPoolable",
					"iqnpoolPooled",
					"iqnpoolTransportBlock",
					"iqnpoolUniverse",
					"iscsiAuthProfile",
					"licenseContents",
					"licenseDownloader",
					"licenseDownloaderFsm",
					"licenseDownloaderFsmStage",
					"licenseDownloaderFsmTask",
					"licenseEp",
					"licenseFeature",
					"licenseFeatureCapProvider",
					"licenseFeatureLine",
					"licenseFile",
					"licenseFileFsm",
					"licenseFileFsmStage",
					"licenseFileFsmTask",
					"licenseInstance",
					"licenseInstanceFsm",
					"licenseInstanceFsmStage",
					"licenseInstanceFsmTask",
					"licenseProp",
					"licenseServerHostId",
					"licenseSource",
					"licenseSourceFile",
					"lldpAcquired",
					"lsAgentPolicy",
					"lsBinding",
					"lsFcLocale",
					"lsFcZone",
					"lsFcZoneGroup",
					"lsIssues",
					"lsPower",
					"lsRequirement",
					"lsServer",
					"lsServerAssocCtx",
					"lsServerExtension",
					"lsServerFsm",
					"lsServerFsmStage",
					"lsServerFsmTask",
					"lsTier",
					"lsUuidHistory",
					"lsVConAssign",
					"lsVersionBeh",
					"lsZoneInitiatorMember",
					"lsZoneTargetMember",
					"lsbootBootSecurity",
					"lsbootDef",
					"lsbootDefaultLocalImage",
					"lsbootIScsi",
					"lsbootIScsiImagePath",
					"lsbootLan",
					"lsbootLanImagePath",
					"lsbootLocalHddImage",
					"lsbootLocalStorage",
					"lsbootPolicy",
					"lsbootSan",
					"lsbootSanCatSanImage",
					"lsbootSanCatSanImagePath",
					"lsbootSanImage",
					"lsbootSanImagePath",
					"lsbootStorage",
					"lsbootUsbExternalImage",
					"lsbootUsbFlashStorageImage",
					"lsbootUsbInternalImage",
					"lsbootVirtualMedia",
					"lsmaintAck",
					"lsmaintMaintPolicy",
					"macpoolAddr",
					"macpoolBlock",
					"macpoolFormat",
					"macpoolPool",
					"macpoolPoolable",
					"macpoolPooled",
					"macpoolUniverse",
					"managedObject",
					"memoryArray",
					"memoryArrayEnvStats",
					"memoryArrayEnvStatsHist",
					"memoryBufferUnit",
					"memoryBufferUnitEnvStats",
					"memoryBufferUnitEnvStatsHist",
					"memoryErrorStats",
					"memoryQual",
					"memoryRuntime",
					"memoryRuntimeHist",
					"memoryUnit",
					"memoryUnitEnvStats",
					"memoryUnitEnvStatsHist",
					"mgmtAccessPolicy",
					"mgmtAccessPolicyItem",
					"mgmtAccessPort",
					"mgmtBackup",
					"mgmtBackupExportExtPolicy",
					"mgmtBackupFsm",
					"mgmtBackupFsmStage",
					"mgmtBackupFsmTask",
					"mgmtBackupPolicy",
					"mgmtBackupPolicyConfig",
					"mgmtBackupPolicyFsm",
					"mgmtBackupPolicyFsmStage",
					"mgmtCfgExportPolicy",
					"mgmtCfgExportPolicyFsm",
					"mgmtCfgExportPolicyFsmStage",
					"mgmtConnection",
					"mgmtController",
					"mgmtControllerFsm",
					"mgmtControllerFsmStage",
					"mgmtControllerFsmTask",
					"mgmtEntity",
					"mgmtExportPolicyFsm",
					"mgmtExportPolicyFsmStage",
					"mgmtExportPolicyFsmTask",
					"mgmtIPv6IfAddr",
					"mgmtIPv6IfAddrFsm",
					"mgmtIPv6IfAddrFsmStage",
					"mgmtIPv6IfAddrFsmTask",
					"mgmtIPv6IfConfig",
					"mgmtIf",
					"mgmtIfFsm",
					"mgmtIfFsmStage",
					"mgmtIfFsmTask",
					"mgmtImporter",
					"mgmtImporterFsm",
					"mgmtImporterFsmStage",
					"mgmtImporterFsmTask",
					"mgmtInbandProfile",
					"mgmtIntAuthPolicy",
					"mgmtInterface",
					"mgmtPmonEntry",
					"mgmtProfDerivedInterface",
					"mgmtVnet",
					"networkElement",
					"networkIfStats",
					"networkOperLevel",
					"nfsEp",
					"nfsMountDef",
					"nfsMountDefFsm",
					"nfsMountDefFsmStage",
					"nfsMountDefFsmTask",
					"nfsMountInst",
					"nfsMountInstFsm",
					"nfsMountInstFsmStage",
					"nfsMountInstFsmTask",
					"nwctrlDefinition",
					"observe",
					"observeObserved",
					"observeObservedCont",
					"observeObservedFsm",
					"observeObservedFsmStage",
					"observeObservedFsmTask",
					"orgOrg",
					"orgSourceMask",
					"osAgent",
					"osInstance",
					"pciEquipSlot",
					"pciUnit",
					"pkiCertReq",
					"pkiEp",
					"pkiEpFsm",
					"pkiEpFsmStage",
					"pkiEpFsmTask",
					"pkiKeyRing",
					"pkiTP",
					"policyCentraleSync",
					"policyCommunication",
					"policyConfigBackup",
					"policyControlEp",
					"policyControlEpFsm",
					"policyControlEpFsmStage",
					"policyControlEpFsmTask",
					"policyControlledInstance",
					"policyControlledType",
					"policyControlledTypeFsm",
					"policyControlledTypeFsmStage",
					"policyControlledTypeFsmTask",
					"policyDateTime",
					"policyDigest",
					"policyDiscovery",
					"policyDns",
					"policyElement",
					"policyFault",
					"policyInfraFirmware",
					"policyLocalMap",
					"policyMEp",
					"policyMonitoring",
					"policyPolicyEp",
					"policyPolicyRequestor",
					"policyPolicyScope",
					"policyPolicyScopeCont",
					"policyPolicyScopeContext",
					"policyPolicyScopeFsm",
					"policyPolicyScopeFsmStage",
					"policyPolicyScopeFsmTask",
					"policyPowerMgmt",
					"policyPsu",
					"policyRefReq",
					"policySecurity",
					"portDomainEp",
					"portGroup",
					"portPIoFsm",
					"portPIoFsmStage",
					"portPIoFsmTask",
					"portTrustMode",
					"powerBudget",
					"powerChassisMember",
					"powerEp",
					"powerGroup",
					"powerGroupAdditionPolicy",
					"powerGroupQual",
					"powerGroupStats",
					"powerGroupStatsHist",
					"powerMgmtPolicy",
					"powerPlacement",
					"powerPolicy",
					"powerPrioWght",
					"powerRackUnitMember",
					"procDoer",
					"procManager",
					"procPrt",
					"procPrtCounts",
					"procStimulusCounts",
					"procSvc",
					"procTxCounts",
					"processorCore",
					"processorEnvStats",
					"processorEnvStatsHist",
					"processorErrorStats",
					"processorQual",
					"processorRuntime",
					"processorRuntimeHist",
					"processorThread",
					"processorUnit",
					"processorUnitAssocCtx",
					"qosclassDefinition",
					"qosclassDefinitionFsm",
					"qosclassDefinitionFsmStage",
					"qosclassDefinitionFsmTask",
					"qosclassEthBE",
					"qosclassEthClassified",
					"qosclassFc",
					"queryresultDependency",
					"queryresultUsage",
					"solConfig",
					"solIf",
					"solPolicy",
					"statsCollectionPolicy",
					"statsCollectionPolicyFsm",
					"statsCollectionPolicyFsmStage",
					"statsCollectionPolicyFsmTask",
					"statsHolder",
					"statsThr32Definition",
					"statsThr32Value",
					"statsThr64Definition",
					"statsThr64Value",
					"statsThrFloatDefinition",
					"statsThrFloatValue",
					"statsThresholdClass",
					"statsThresholdPolicy",
					"storageAuthKey",
					"storageConnectionDef",
					"storageConnectionPolicy",
					"storageController",
					"storageDomainEp",
					"storageDrive",
					"storageEnclosure",
					"storageEpUser",
					"storageEtherIf",
					"storageFcIf",
					"storageFcTargetEp",
					"storageFcTargetIf",
					"storageFlexFlashCard",
					"storageFlexFlashController",
					"storageFlexFlashDrive",
					"storageFlexFlashVirtualDrive",
					"storageIScsiTargetIf",
					"storageIniGroup",
					"storageInitiator",
					"storageItem",
					"storageLocalDisk",
					"storageLocalDiskConfigDef",
					"storageLocalDiskConfigPolicy",
					"storageLocalDiskPartition",
					"storageLocalDiskSlotEp",
					"storageLocalLun",
					"storageLunDisk",
					"storageMezzFlashLife",
					"storageNodeEp",
					"storageOperation",
					"storageQual",
					"storageRaidBattery",
					"storageSystem",
					"storageSystemFsm",
					"storageSystemFsmStage",
					"storageSystemFsmTask",
					"storageTransportableFlashModule",
					"storageVirtualDrive",
					"storageVsanRef",
					"swAccessDomain",
					"swAccessDomainFsm",
					"swAccessDomainFsmStage",
					"swAccessDomainFsmTask",
					"swAccessEp",
					"swCardEnvStats",
					"swCardEnvStatsHist",
					"swCmclan",
					"swEnvStats",
					"swEnvStatsHist",
					"swEthEstcEp",
					"swEthEstcPc",
					"swEthLanBorder",
					"swEthLanBorderFsm",
					"swEthLanBorderFsmStage",
					"swEthLanBorderFsmTask",
					"swEthLanEp",
					"swEthLanFlowMon",
					"swEthLanFlowMonFsm",
					"swEthLanFlowMonFsmStage",
					"swEthLanFlowMonFsmTask",
					"swEthLanMon",
					"swEthLanPc",
					"swEthMon",
					"swEthMonDestEp",
					"swEthMonFsm",
					"swEthMonFsmStage",
					"swEthMonFsmTask",
					"swEthMonSrcEp",
					"swEthTargetEp",
					"swFabricZoneNs",
					"swFabricZoneNsOverride",
					"swFcEstcEp",
					"swFcMon",
					"swFcMonDestEp",
					"swFcMonFsm",
					"swFcMonFsmStage",
					"swFcMonFsmTask",
					"swFcMonSrcEp",
					"swFcSanBorder",
					"swFcSanBorderFsm",
					"swFcSanBorderFsmStage",
					"swFcSanBorderFsmTask",
					"swFcSanEp",
					"swFcSanMon",
					"swFcSanPc",
					"swFcServerZoneGroup",
					"swFcZone",
					"swFcZoneSet",
					"swFcoeEstcEp",
					"swFcoeSanEp",
					"swFcoeSanPc",
					"swIpRoute",
					"swNFExporterRef",
					"swNetflowExporter",
					"swNetflowMonSession",
					"swNetflowMonitor",
					"swNetflowMonitorRef",
					"swNetflowRecordDef",
					"swPhys",
					"swPhysEtherEp",
					"swPhysFcEp",
					"swPhysFsm",
					"swPhysFsmStage",
					"swPhysFsmTask",
					"swSystemStats",
					"swSystemStatsHist",
					"swUlan",
					"swUtilityDomain",
					"swUtilityDomainFsm",
					"swUtilityDomainFsmStage",
					"swUtilityDomainFsmTask",
					"swVirtL3Intf",
					"swVlan",
					"swVlanGroup",
					"swVlanPortNs",
					"swVlanPortNsOverride",
					"swVlanRef",
					"swVsan",
					"swZoneInitiatorMember",
					"swZoneTargetMember",
					"swatAction",
					"swatCondition",
					"swatInjection",
					"swatResultstats",
					"swatTarget",
					"swatTrigger",
					"syntheticDirectory",
					"syntheticFile",
					"syntheticFileSystem",
					"syntheticFsObj",
					"syntheticFsObjFsm",
					"syntheticFsObjFsmStage",
					"syntheticFsObjFsmTask",
					"syntheticTime",
					"sysdebugAutoCoreFileExportTarget",
					"sysdebugAutoCoreFileExportTargetFsm",
					"sysdebugAutoCoreFileExportTargetFsmStage",
					"sysdebugAutoCoreFileExportTargetFsmTask",
					"sysdebugBackupBehavior",
					"sysdebugCore",
					"sysdebugCoreFileRepository",
					"sysdebugCoreFsm",
					"sysdebugCoreFsmStage",
					"sysdebugCoreFsmTask",
					"sysdebugEp",
					"sysdebugLogControlDestinationFile",
					"sysdebugLogControlDestinationSyslog",
					"sysdebugLogControlDomain",
					"sysdebugLogControlEp",
					"sysdebugLogControlEpFsm",
					"sysdebugLogControlEpFsmStage",
					"sysdebugLogControlEpFsmTask",
					"sysdebugLogControlModule",
					"sysdebugLogExportPolicy",
					"sysdebugLogExportPolicyFsm",
					"sysdebugLogExportPolicyFsmStage",
					"sysdebugLogExportPolicyFsmTask",
					"sysdebugLogExportStatus",
					"sysdebugMEpLog",
					"sysdebugMEpLogPolicy",
					"sysdebugManualCoreFileExportTarget",
					"sysdebugManualCoreFileExportTargetFsm",
					"sysdebugManualCoreFileExportTargetFsmStage",
					"sysdebugManualCoreFileExportTargetFsmTask",
					"sysdebugTechSupFileRepository",
					"sysdebugTechSupport",
					"sysdebugTechSupportCmdOpt",
					"sysdebugTechSupportFsm",
					"sysdebugTechSupportFsmStage",
					"sysdebugTechSupportFsmTask",
					"sysfileDigest",
					"sysfileMutation",
					"sysfileMutationFsm",
					"sysfileMutationFsmStage",
					"sysfileMutationFsmTask",
					"topMetaInf",
					"topRoot",
					"topSysDefaults",
					"topSystem",
					"trigAbsWindow",
					"trigClientToken",
					"trigLocalAbsWindow",
					"trigLocalSched",
					"trigMeta",
					"trigRecurrWindow",
					"trigSched",
					"trigTest",
					"trigTriggered",
					"uuidpoolAddr",
					"uuidpoolBlock",
					"uuidpoolFormat",
					"uuidpoolPool",
					"uuidpoolPoolable",
					"uuidpoolPooled",
					"uuidpoolUniverse",
					"versionApplication",
					"versionEp",
					"vmComputeEp",
					"vmDC",
					"vmDCOrg",
					"vmEp",
					"vmHba",
					"vmHv",
					"vmInstance",
					"vmLifeCyclePolicy",
					"vmLifeCyclePolicyFsm",
					"vmLifeCyclePolicyFsmStage",
					"vmLifeCyclePolicyFsmTask",
					"vmNic",
					"vmOrg",
					"vmSwitch",
					"vmVif",
					"vmVlan",
					"vmVnicProfCl",
					"vmVnicProfInst",
					"vmVsan",
					"vnicBootIpPolicy",
					"vnicBootTarget",
					"vnicConnDef",
					"vnicDefBeh",
					"vnicDynamicCon",
					"vnicDynamicConPolicy",
					"vnicDynamicConPolicyRef",
					"vnicDynamicIdUniverse",
					"vnicDynamicProvider",
					"vnicDynamicProviderEp",
					"vnicEthLif",
					"vnicEther",
					"vnicEtherIf",
					"vnicFc",
					"vnicFcGroupDef",
					"vnicFcGroupTempl",
					"vnicFcIf",
					"vnicFcLif",
					"vnicFcNode",
					"vnicFcOEIf",
					"vnicIPv4Dhcp",
					"vnicIPv4Dns",
					"vnicIPv4If",
					"vnicIPv4IscsiAddr",
					"vnicIPv4PooledIscsiAddr",
					"vnicIPv4StaticRoute",
					"vnicIScsi",
					"vnicIScsiAutoTargetIf",
					"vnicIScsiBootParams",
					"vnicIScsiBootVnic",
					"vnicIScsiLCP",
					"vnicIScsiNode",
					"vnicIScsiStaticTargetIf",
					"vnicInternalProfile",
					"vnicIpV4History",
					"vnicIpV4MgmtPooledAddr",
					"vnicIpV4PooledAddr",
					"vnicIpV4ProfDerivedAddr",
					"vnicIpV4StaticAddr",
					"vnicIpV6History",
					"vnicIpV6MgmtPooledAddr",
					"vnicIpV6StaticAddr",
					"vnicIpc",
					"vnicIpcIf",
					"vnicIqnHistory",
					"vnicLanConnPolicy",
					"vnicLanConnTempl",
					"vnicLifVlan",
					"vnicLifVsan",
					"vnicLun",
					"vnicMacHistory",
					"vnicOProfileAlias",
					"vnicProfile",
					"vnicProfileAlias",
					"vnicProfileRef",
					"vnicProfileSet",
					"vnicProfileSetFsm",
					"vnicProfileSetFsmStage",
					"vnicProfileSetFsmTask",
					"vnicRackServerDiscoveryProfile",
					"vnicSanConnPolicy",
					"vnicSanConnTempl",
					"vnicScsi",
					"vnicScsiIf",
					"vnicUsnicConPolicy",
					"vnicUsnicConPolicyRef",
					"vnicVhbaBehPolicy",
					"vnicVlan",
					"vnicVmqConPolicy",
					"vnicVmqConPolicyRef",
					"vnicVnicBehPolicy",
					"vnicWwnnHistory",
					"vnicWwpnHistory",
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

class WcardFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "WcardFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w=None, option=None, elementName=None):
		"""This method writes the xml representation of the WcardFilter object."""
		if w is None:
			x=Element("wcard")
		else:
			if (elementName == None):
				x = SubElement(w,"wcard")
			else:
				x = SubElement(w,elementName)
		x.set("class", getattr(self,"Class"));
		x.set("property", getattr(self,"Property"));
		x.set("value", getattr(self,"Value"));
		self.childWriteXml(x, option)
		return x

	def setattr(self, key, value):
		"""This method sets attribute value of the WcardFilter object."""
		self.__dict__[key] = value

	def getattr(self, key):
		"""This method gets attribute value of the WcardFilter object."""
		return self.__dict__[key]

	def LoadFromXml(self, element, handle):
		"""This method creates the object from the xml representation of the WcardFilter object."""
		self.SetHandle(handle)

		if element.attrib:
			for attr_name, attr_value in element.attrib.iteritems():
				self.setattr(UcsUtils.WordU(attr_name), str(attr_value))

		child_elements = element.getchildren()
		if child_elements:
			for child_element in child_elements:
				if not ET.iselement(child_element):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(child_element.tag)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(child_element, handle)

