#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea
# ip address class file

class MyIpAddress(object):

    @staticmethod
    def convertIp(ipAddress):  # 这里可没有做正确IP检查
        numToIp = lambda x: '.'.join([str(x / (256 ** i) % 256) for i in range(3, -1, -1)])
        ipToNum = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
        try:
            return numToIp(int(ipAddress))
        except:
            return ipToNum(ipAddress)
