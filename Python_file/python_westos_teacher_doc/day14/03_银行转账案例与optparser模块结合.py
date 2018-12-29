#!/usr/bin/env python
#coding:utf-8


""""
Name: 03_银行转账案例与optparser模块结合.py
Date: 2018/06/03
Connect: xc_guofan@163.com
Author: lvah
Desc:


"""
from optparse import OptionParser

import pymysql


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, source_acctid, target_acctid, money):
        """转账函数"""
        try:
            # 判断账户是否存在?
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            # 001: 1000   002: 500
            # 001: 1000    002: 500
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            # 撤销数据库的执行
            self.conn.rollback()
            raise e

    def check_acct_available(self, acctid):
        """检测账户是否存在?"""
        cur = self.conn.cursor()
        try:
            # 查询账户名为acctid的详细信息
            select_sql = 'select * from account where accid=%s;' % (acctid)
            cur.execute(select_sql)
            print("execute sql:%s" % (select_sql))

            res = cur.fetchall()
            if len(res) != 1:
                raise Exception("帐号%s不存在" % (acctid))
        finally:
            cur.close()

    def has_enough_money(self, acctid, money):
        """检测账户是否有足够的钱"""
        cur = self.conn.cursor()
        try:
            select_sql = 'select money from account where accid=%s' \
                         %(acctid)
            cur.execute(select_sql)
            print('has_enough_money sql: %s' %(select_sql))
            res = cur.fetchall()
            if res:

                now_money = int(res[0][0])
                if int(now_money) < int(money):
                    raise  Exception("账户%s没有足够的钱,目前金额为 %d" %(acctid, now_money))
        finally:
            cur.close()
    def reduce_money(self, acctid, money):
        """给其他账户进行转账操作"""
        cur = conn.cursor()
        try:
            update_sqli = 'update account set money=money-%s where accid=%s' %(money, acctid)
            cur.execute(update_sqli)
            print('reduce_money sql:%s' %(update_sqli))
        except Exception as e:
            print("reduce money failed：",e)
        finally:
            cur.close()

    def add_money(self, acctid, money):

        cur = conn.cursor()
        try:
            update_sqli = 'update account set money=money+%s where accid=%s' % (money, acctid)
            cur.execute(update_sqli)
            print('add_money sql:%s' % (update_sqli))
        except Exception as e:
            print("add money failed：",e)
        finally:
            cur.close()



if __name__ == "__main__":
    conn = pymysql.connect(
        host='172.25.254.250', user='root', passwd='westos',
        db='hello', charset='utf8')

    USAGE = "command [OPTION....]"
    parser = OptionParser(USAGE)

    # 新加属性：
    # -s:  type:类型, dest: 传递的值赋值的变量名, help:帮助, default: 默认值
    parser.add_option('-s', type=int, dest='srcid', help="原账户id", default=610001)
    parser.add_option('-d', type=int, dest='destid', help='目标账户id', default=610002)
    parser.add_option('-m', type=int, dest='money', help='转账金额', default=500)

    # 解析接收的属性值
    option, args = parser.parse_args()

    source_acctid = option.srcid
    target_acctid = option.destid
    money = option.money



    trans_money = TransferMoney(conn)
    try:
        print(source_acctid, target_acctid, money)
        trans_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print("转账出现问题:", e)
    finally:
        conn.commit()
        conn.close()











