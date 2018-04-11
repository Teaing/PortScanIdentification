#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

import argparse


class MyArg(object):

    @staticmethod
    def getArgparse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-path', '--path', type=str, help='filePath default:/tools/ip.txt')
        parser.add_argument('-url', '--url', type=str, help='url address')
        parser.add_argument('-project', '--project', type=str, help='project name e.g:360.cn')
        parser.add_argument('-banner', '--banner', help='get port banner info.', action='store_true')
        myArgs = parser.parse_args()
        if myArgs.url and myArgs.path:
            parser.print_help()
            return
        return myArgs
