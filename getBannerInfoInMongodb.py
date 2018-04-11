#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

import sys
from lib.mymongodb import MyMongodb
from lib.myipaddress import MyIpAddress


def main():
    if len(sys.argv) <= 1:
        raise Exception('PorjectName is empty')
    projectName = sys.argv[1]
    myMongodb = MyMongodb()
    mongodbResult = myMongodb.getBannerInfo(projectName)
    for result in mongodbResult:
        line = result.get('scanResult')
        for oneLine in line:
            ipAddress = MyIpAddress.convertIp(oneLine)
            for info in line.get(oneLine):
                keyStr = info.keys()[0]
                print '{0}\t{1}\t{2}'.format(ipAddress, keyStr, info.get(keyStr))


if __name__ == '__main__':
    main()
