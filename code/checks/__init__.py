from UcsSdk import *


from dateutil.parser import parse


def parseTimeIfAny(timestr):
    if timestr == '1970-01-01T01:00:00.000':
        return None
    try:
        return parse(timestr)
    except Exception:
        pass


def tryFloat(inp):
    if inp == 'not-applicable':
        return None
    try:
        return float(inp)
    except Exception:
        pass


yesBl = lambda vl: vl == 'yes'
operableBl = lambda vl: vl == 'operable'
onBl = lambda vl: vl == 'on'
okBl = lambda vl: vl == 'ok'
equipedBl = lambda vl: vl == 'equipped'
enabledBl = lambda vl: vl == 'enabled'
onlineBl = lambda vl: vl == 'online'
isUpBl = lambda vl: vl == 'up'
presentBl = lambda vl: vl == 'present'
inServiceBl = lambda vl: vl == 'in-service'
availBl = lambda vl: vl == 'available'
connectedBl = lambda vl: vl == 'connected'
