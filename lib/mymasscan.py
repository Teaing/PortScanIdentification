#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

import os
from mymasscananalysis import MyMasscanAnalysis


class MyMasscan(object):
    def __init__(self, scanIpFile, scanRate=2000):
        self.masscanPath = '/usr/bin/masscan'
        self.outLogFile = '/tmp/myResult.xml'
        self.scanRate = scanRate
        self.scanIpFile = scanIpFile
        if not os.path.exists(self.masscanPath):
            raise Exception('masscan path:{0}, not found!'.format(self.masscanPath))
        if not os.path.exists(scanIpFile):
            raise Exception('scan ip file:{0}, not found!'.format(self.scanIpFile))

    def getScanCommand(self):
        masscanPar = '{0} -p1-65535 -iL {1} -oX {2} -n --wait 5 --randomize-hosts --rate={3}'.format(self.masscanPath,
                                                                                                     self.scanIpFile,
                                                                                                     self.outLogFile,
                                                                                                     self.scanRate)
        return masscanPar

    def scan(self):
        scanCommand = self.getScanCommand()
        os.system(scanCommand)
        portInfo = MyMasscanAnalysis.analysis(self.outLogFile)
        return portInfo
