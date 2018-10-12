#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jiangpc time:2018/10/12

import unittest
import requests
import os,sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class GetEventListTest(unittest.TestCase):
    '''查询发布会'''
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/get_event_list/"

    def tearDown(self):
        print(self.result)

    def test_get_event_list_null(self):
        '''参数eid和name为空'''
        payload = {'eid':'','name':''}
        r = requests.get(self.base_url,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')

    def test_get_event_list_eid_not_exist(self):
        '''参数eid不存在 '''
        payload ={'eid':100}
        r = requests.get(self.base_url,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'query result is empty')

    def test_get_event_list_success(self):
        '''查询成功'''
        payload = {'eid':1}
        r = requests.get(self.base_url,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')
        self.assertIn('80d',self.result['data'])

    def test_get_event_list_name_exist(self):
        '''name存在'''
        payload = {'eid':1,'name':'80d'}
        r = requests.get(self.base_url,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')

    def test_get_event_list_name_not_exist(self):
        '''name不存在'''
        payload = {'eid': 1, 'name': '100d'}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'query result is empty')

    if __name__ == '__main__':
        test_data.init_data()
        unittest.main()
