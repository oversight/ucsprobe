#!/usr/bin/python
"""
file is generated with probeCreator
"""
import time
from traceback import format_exc
from twisted.internet import reactor
from encodings import hex_codec  # @UnusedImport
from encodings import ascii  # @UnusedImport
from generic.folderManager import FolderManager
from generic.credentials import setOrAddCredentialArgs
from generic.credentials import askCreds
from core.root import Root
from core.ucsCheckFactory import UcsCheckFactory
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main(service=None):
    """ Main setup of the functionality."""
    try:
        root = Root()
        parser = setOrAddCredentialArgs()
        args = parser.parse_args()
        askCreds(args)
        factory = UcsCheckFactory(FolderManager().getBasePath())
        root.setCheckFactory(factory)
        root.setUpConnectionLoop()
        if service:
            root.setServiceObject(service)
            reactor.addSystemEventTrigger('before', 'shutdown', root.stopServer)
        reactor.run()
    except Exception:
        errTrace = format_exc()
        msg = '{timestamp} Failed to startup\n{errTrace}'.format(timestamp=int(time.time()), errTrace=errTrace)
        with open(FolderManager().var('log', 'serviceStartupFailure.log'), 'w') as fl:
            fl.write(msg)
        print(msg)


if __name__ == '__main__':
    main()
