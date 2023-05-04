'''
Created on 12 dec. 2014

@author: sjuul
'''

import sys
import uuid
import time
from os.path import dirname
from os.path import join
from twisted.python import log
from twisted.python.failure import Failure
from twisted.internet.defer import Deferred
from twisted.python.log import startLogging
from generic.folderManager import FolderManager
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def testCheck(constructor, ip4, basePath=None, **kwargs):
    if not basePath:
        basePath = dirname(dirname(__file__))
    FolderManager(join(basePath, 'someFilename.txt'))
    from twisted.internet import reactor
    from generic.jsonUtils import printAndLoadJson
    startLogging(sys.stdout)
    startTs = time.time()

    def printAndStopReactor(*args, **kwargs):
        runtime = time.time() - startTs
        if args and isinstance(args[0], (Exception, Failure)):
            log.err(args[0])
        else:
            printAndLoadJson(*args, **kwargs)
        print 'Runtime', runtime
        if reactor.running:
            reactor.stop()
        else:
            reactor.run = lambda: 'Not running'

    probeConfig = {}
    probeConfig.update(kwargs)
    SOME_UUID = 'b6da8c7e6e93-005056b6769b'
    check = constructor({}, hostConfig={'parentCore': SOME_UUID, 'hostUuid': SOME_UUID, 'probeConfig': {'ucsProbe': {'ip4': ip4}}}, basePath=basePath)
    res = check.getData({}, printAndStopReactor, printAndStopReactor)
    printAndStopReactor(res)
    check.connection.Logout()
