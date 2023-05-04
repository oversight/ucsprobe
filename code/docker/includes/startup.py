#!/usr/bin/python
import json
import sys
import os
import uuid
# data handling:
# logging              --> [named volume] --> /data/log/<probename>-<hostname>.log
# /opt/<probename>/var --> ignored as it does not contain data
# /opt/<probename>/etc --> [symlink to named volume] --> /data/config/<probename>

def updateconfiguration (file_path, **new_values):
    assert isinstance(new_values, dict)
    if os.path.exists(file_path):
        fl = open(file_path, 'rb')
        cfg = json.load(fl)
        fl.close()
    else:
        cfg = {}
    cfg.update(new_values)
    fl = open(file_path, 'wb')
    json.dump(cfg, fl, indent=4, sort_keys=True)
    fl.close()

def symlinkDirectory (sourcePath, destinationPath):
    createDirs (sourcePath)
    #createDirs (os.path.join(destinationPath.rsplit('/', 1))[0])
    if os.path.lexists(destinationPath):
        os.remove(destinationPath)
    os.symlink(sourcePath,destinationPath)

def createDirs (direcory):
    if not os.path.exists(direcory):
        os.makedirs(direcory)

# Redirect the configurion files to the named volume data
symlinkDirectory ('/data/config/OsUcsProbe','/opt/OsUcsProbe/etc')

# Create log base directory
createDirs ('/data/log')

# UUID is used to uniquely identitfy each containter
uniqueHostID = str(uuid.uuid1()).split("-")[-1]
updateconfiguration(
    '/opt/OsUcsProbe/etc/ucsProbe-config.json',
    systemId=uniqueHostID,
    agentCoreIp='agentcore',
    logFileName='OsUcsProbe-' + uniqueHostID + '.log',
    logPath=os.path.join('/','data', 'log')
)

#Start the probe
os.system("/opt/OsUcsProbe/OsUcsProbe.bin")
