#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

from lib.mymongodb import MyMongodb
from lib.myipaddress import MyIpAddress


def main():
    myMongodb = MyMongodb()
    mongodbResult = myMongodb.getAll()
    for line in mongodbResult:
        for oneLine in line:
            if oneLine != '_id':
                ipAddress = MyIpAddress.convertIp(oneLine)
                for info in line.get(oneLine):
                    keyStr = info.keys()[0]
                    print '{0}\t{1}\t{2}'.format(ipAddress, keyStr, info.get(keyStr))


if __name__ == '__main__':
    main()
