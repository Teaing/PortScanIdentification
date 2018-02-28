#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

import os


class MyUid(object):

    @staticmethod
    def getUserId():
        return os.geteuid()

    @staticmethod
    def checkPermissions():
        if os.geteuid() != 0:
            raise Exception('This program must be run as root. Aborting.')
