class Version(object):
    
    buildDate = '2017-05-24 09:53:43.947582'
    platform = 'PLACEHOLDERVERSION_x64_PLACEHOLDERVERSION'
    versionNr = '1.0.4'

    @classmethod
    def getString(cls):
        return 'Version: ' + cls.versionNr + ' buildDate: ' + cls.buildDate + '\nplatform: ' + cls.platform

    @classmethod
    def getVersion(cls):
        return cls.platform + '-' + cls.versionNr