#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea
# dict class file

class MyDict(object):

    # 合并字典
    @staticmethod
    def mergeDicts(dictX, dictY):
        dictZ = dictX.copy()
        dictZ.update(dictY)
        return dictZ
