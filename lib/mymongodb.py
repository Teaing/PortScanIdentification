#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea
# mongodb operation class file

from pymongo import MongoClient


class MyMongodb(object):
    def __init__(self):
        dbHost = '127.0.0.1'
        dbPort = 27017
        dbName = 'MasscanItem'
        dbUser = ''
        dbPassword = ''
        try:
            self.conn = MongoClient(dbHost, dbPort)
        except Exception, e:
            print str(e)
        self.db = self.conn[dbName]
        if dbUser and dbPassword:
            self.db.authenticate(dbUser, dbPassword)

    def getLastOne(self, collectionStr='PortInfo'):
        self.collection = self.db[collectionStr]
        return self.collection.find({}, {'_id': 0}).sort('_id', -1).limit(1)

    def insertInfo(self, jsonData, collectionStr='PortInfo'):
        self.collection = self.db[collectionStr]
        return self.collection.insert(jsonData)

    def getBannerInfo(self, projectName, collectionName='BannerInfo'):
        self.collection = self.db[collectionName]
        return self.collection.find({'project': projectName}, {'_id': 0}).sort('_id', -1).limit(1)
