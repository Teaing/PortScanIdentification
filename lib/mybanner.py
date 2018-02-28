#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea
# nmap banner get class file

import nmap
import threading
from myipaddress import MyIpAddress
from mymongodb import MyMongodb


class MyBanner(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            scanInfo = self.queue.get()
            if scanInfo:
                self.scan(scanInfo[0], scanInfo[1])
            self.queue.task_done()

    def scan(self, ipAddress, port):
        address = MyIpAddress.convertIp(ipAddress)
        scanResult = dict.fromkeys([ipAddress], [])
        nmapScan = nmap.PortScanner()
        nmapScan.scan(hosts=address, ports=port, arguments='-sV --open -Pn -n')
        tcpInfo = nmapScan[address].get('tcp')
        for port in tcpInfo:
            portInfo = tcpInfo.get(port)
            tmpInfo = dict.fromkeys([str(port)], '{0} {1} {2}'.format(portInfo.get('name'), portInfo.get('product'),
                                                                      portInfo.get('version')).strip())
            scanResult[ipAddress].append(tmpInfo)
        myMongodb = MyMongodb()
        myMongodb.insertInfo(scanResult, collectionStr='BannerInfo')
