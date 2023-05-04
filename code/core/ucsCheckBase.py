'''
Created on 12 dec. 2014

@author: sjuul
'''
from generic.checks.checkBase import CredentialsCheckBase
from generic.checks.checkBase import cachedHostProp
from UcsSdk.UcsHandle import UcsHandle
from UcsSdk.UcsHandle import UcsPropertyMeta
from UcsSdk.Constants import YesOrNo
from UcsSdk.UcsBase import UcsUtils
from twisted.internet import reactor
ONE_DAY = 24*60*60


class UcsCheckBase(CredentialsCheckBase):
    
    def __init__(self, *args, **kwargs):
        self._connection = None
        super(UcsCheckBase, self).__init__(*args, **kwargs)

    def updateHostConfig(self, hostConfig):
        super(UcsCheckBase, self).updateHostConfig(hostConfig, 'ucsProbe')

    @cachedHostProp(maxAge=ONE_DAY)
    def connection(self):
        handle = UcsHandle()
        handle.Login(self.ip4, self.userName, self.password, autoRefresh=YesOrNo.TRUE)
        def closeConn(*args):
            handle.Logout()
        reactor.callLater(ONE_DAY + 10, closeConn)
        return handle
    
    def moToDct(self, mo, classFormatters=None):
        dct = {
            prop: mo.getattr(prop) 
            for prop in UcsUtils.GetUcsPropertyMetaAttributeList(mo.propMoMeta.name) 
            if UcsUtils.GetUcsPropertyMeta(mo.propMoMeta.name,prop).access != UcsPropertyMeta.Internal
        }
        dct['name'] = mo.Dn
        if classFormatters:
            for ky in set(dct) & set(classFormatters):
                formatter = classFormatters[ky]
                if isinstance(formatter, tuple):
                    newKy, formatter = formatter
                else:
                    newKy = ky
                
                try:
                    dct[newKy] = formatter(dct[ky])
                except Exception:
                    self.log.failure('Formatting failed {ky} {formatter} {vl}', ky=ky, vl=dct.get(ky), formatter=formatter)
                    raise
        return dct