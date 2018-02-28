#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

import time
import Queue
from lib.myarg import MyArg
from lib.myuid import MyUid
from lib.myparscheck import MyParsCheck
from lib.mymasscan import MyMasscan
from lib.mymongodb import MyMongodb
from lib.mybanner import MyBanner


def main():
    MyUid.checkPermissions()
    parsContent = MyArg.getArgparse()
    myArgparse = MyParsCheck.contentCheck(parsContent)
    myMasscan = MyMasscan(myArgparse.path)
    portInfoContent = myMasscan.scan()
    print portInfoContent

    myMongodb = MyMongodb()
    myMongodb.insertInfo(portInfoContent)
    print 'Insert Mongodb Complete.'

    if not myArgparse.banner:
        return
    scanResult = portInfoContent.get('scanResult')
    print scanResult

    myMongodb.delData()  # 清除Banner信息

    startTime = time.time()
    threadNum = 50
    queue = Queue.Queue()

    for i in range(threadNum):
        t = MyBanner(queue)
        t.setDaemon(True)
        t.start()

    for ipAddress in scanResult:
        queuePutInfo = []
        portStr = ','.join(scanResult.get(ipAddress))
        queuePutInfo.append(ipAddress)
        queuePutInfo.append(portStr)
        queue.put(queuePutInfo)
    queue.join()

    print 'Over! used {0} second.'.format(int(time.time() - startTime))


if __name__ == '__main__':
    main()
