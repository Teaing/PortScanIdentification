#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea
# masscan scan result analysis class file

import os
import time
from myipaddress import MyIpAddress

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class MyMasscanAnalysis(object):

    @staticmethod
    def analysis(xmlPath, projectName):
        if not os.path.exists(xmlPath):
            raise Exception('masscan scan result file not exists.')
        masscanResult = {
            'project': projectName,
            'count': 0,
            'scanResult': None,
            'startTime': 0,
            'endTime': 0
        }
        try:
            tree = ET.ElementTree(file=xmlPath)
            root = tree.getroot()
        except:
            masscanResult['endTime'] = int(time.time())
            return masscanResult
        hostList = []
        for host in root:
            for address in host:
                if address.tag == 'address':
                    tmpIp = '%s' % (
                        MyIpAddress.convertIp(address.attrib['addr']))  # Mongodb Error: can't have . in field names
                    hostList.append(tmpIp)
                    # hostList   ['167838072', '167838072', '167838072', '167838072', '167838072']
                '''
                if address.tag == 'finished':
                    endTime = address.attrib['time']  # root[-1][0].attrib['time'] 可以替代这里
                '''
        hostList = list(set(hostList))  # 去重
        resultDict = {}.fromkeys(hostList, None)  # 创建结果字典
        masscanResult['count'] = len(resultDict)  # 所有主机数量
        masscanResult['startTime'] = root.attrib['start']  # 开始时间
        masscanResult['endTime'] = root[-1][0].attrib['time']  # 结束时间,Masscan version 1.0.3 支持
        '''
        for line in result_dict:    # 这里不重置会有BUG,后面用了try后可以去除
                result_dict[line] = []
        '''
        for host in root:
            ip_str, port_str = '', ''
            for address in host:
                if address.tag == 'address':
                    ip_str = '%s' % (MyIpAddress.convertIp(address.attrib['addr']))
                for port in address:
                    port_str = port.attrib['portid']
                    try:
                        resultDict[ip_str].append(port_str)
                    except:
                        resultDict[ip_str] = []
                        resultDict[ip_str].append(port_str)
        masscanResult['scanResult'] = resultDict
        return masscanResult
