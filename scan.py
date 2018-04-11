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
from lib.mydict import MyDict


def main():
    MyUid.checkPermissions()
    parsContent = MyArg.getArgparse()
    myArgparse = MyParsCheck.contentCheck(parsContent)
    myMasscan = MyMasscan(myArgparse.path, myArgparse.project)
    portInfoContent = myMasscan.scan()
    print portInfoContent

    myMongodb = MyMongodb()
    myMongodb.insertInfo(portInfoContent)
    print 'Insert Mongodb Complete.'

    if not myArgparse.banner:
        return

    scanResult = portInfoContent.get('scanResult')

    if not scanResult:
        return

    startTime = time.time()
    threadNum = 50
    inputQueue = Queue.Queue()
    outputQueue = Queue.Queue()  # 输出结果

    for i in range(threadNum):
        t = MyBanner(inputQueue, outputQueue)
        t.setDaemon(True)
        t.start()

    for ipAddress in scanResult:
        queuePutInfo = []
        portStr = ','.join(scanResult.get(ipAddress))
        queuePutInfo.append(ipAddress)
        queuePutInfo.append(portStr)
        inputQueue.put(queuePutInfo)

    inputQueue.join()

    tmpBannerDict = {}
    while not outputQueue.empty():
        tmpBannerDict = MyDict.mergeDicts(tmpBannerDict, outputQueue.get())
        outputQueue.task_done()

    bannerResult = {
        'project': myArgparse.project,
        'count': len(tmpBannerDict),
        'scanResult': tmpBannerDict,
        'endTime': int(time.time())
    }

    myMongodb.insertInfo(bannerResult, collectionStr='BannerInfo')

    print bannerResult
    print 'Over! used {0} second.'.format(int(time.time() - startTime))


if __name__ == '__main__':
    main()
