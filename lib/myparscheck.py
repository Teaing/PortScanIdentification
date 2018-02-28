#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

import os
import requests


class MyParsCheck(object):

    @staticmethod
    def contentCheck(myArgs):
        if not myArgs:
            return
        if myArgs.url:
            if myArgs.url.startswith('http://') or myArgs.url.startswith('https://'):
                try:
                    statusCode = int(requests.head(myArgs.url).status_code)
                except:
                    statusCode = 0
                if statusCode != 200:
                    raise Exception('url {0} error.'.format(myArgs.path))
                try:
                    requestContent = requests.get(myArgs.url).text
                    with open('/tmp/myIp.txt', 'wb') as writeFile:
                        writeFile.write(requestContent)
                    myArgs.path = '/tmp/myIp.txt'
                except:
                    raise Exception('get url {0} content failure.'.format(myArgs.path))
        else:
            if not myArgs.path:
                myArgs.path = '/tools/ip.txt'
            if not os.path.exists(myArgs.path):
                raise Exception('path {0} is not exists.'.format(myArgs.path))
        return myArgs
