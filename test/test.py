# /usr/bin/python evn
# coding=utf-8

"""
auth:wuqichao
mail:wqc2008@gmail.com
createtime:2014-7-19上午11:26:08
usege:

"""

import os
from  ant.yun.api import api
from pprint import pprint


def run(yun_name):
    # 查询云的Region
    strat = api(yun_name, 'get_idcs')
    idcs = strat.get_result()

    # 查询Region中服务器信息
    for idc in idcs:
        print(idc)
        t = api(yun_name, 'get_hosts', idc)
        data = t.get_result()
        # 直接打印个数
        pprint(len(data))
        # pprint(data)

    print("=" * 50)
    # 查询Region中负载信息
    for idc in idcs:
        print(idc)
        t = api(yun_name, 'get_balancers', idc)
        data = t.get_result()
        # 直接打印个数
        pprint(len(data))
        # pprint(data)


if __name__ == '__main__':

    # ,'amazon','qcloud','ucloud','qingcloud'
    yun_list = ['aliyun']
    for yun in yun_list:
        run(yun)