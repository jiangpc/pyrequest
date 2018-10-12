#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jiangpc time:2018/10/11

import sys
sys.path.append('../db_fixture')
from db_fixture.mysql_db import DB

# 创建测试数据
datas = {
    #发布会表数据
    'sign event':[
        {'id':1,'name':'80d','`limit`':2000,'status':1,'address':'杭州','start_time':'2018-10-11 17:20:40','create_time':'2018-10-11 12:21:21'},
        {'id':2,'name':'70d','`limit`':2000,'status':1,'address':'杭州','start_time':'2018-10-11 17:20:40','create_time':'2018-10-11 12:21:21'},
        {'id':3,'name':'60d','`limit`':2000,'status':1,'address':'杭州','start_time':'2018-10-11 17:20:40','create_time':'2018-10-11 12:21:21'},
        {'id':4,'name':'50d','`limit`':2000,'status':1,'address':'杭州','start_time':'2018-10-11 17:20:40','create_time':'2018-10-11 12:21:21'},
        {'id':5,'name':'40d','`limit`':2000,'status':1,'address':'杭州','start_time':'2018-10-11 17:20:40','create_time':'2018-10-11 12:21:21'},
    ],
    # 嘉宾表数据
    'sign_guest':[
        {'id':1,'realname':'李逵','phone':17805068613,'email':'likui@email.com','sign':0,'event_id':1},
        {'id':2,'realname':'宋江','phone':17805068614,'email':'songjiang@email.com','sign':1,'event_id':1},
        {'id':3,'realname':'吴用','phone':17805068615,'email':'wuyong@email.com','sign':0,'event_id':5},
    ],
}

# 将测试数据插入表
def init_data():
    db = DB()
    for table,data in datas.items():
        db.clear(table)
        for d in  data:
            db.insert(table,d)
        db.close()


if __name__ == '__main__':
    init_data()