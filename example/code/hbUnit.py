# coding=utf-8
import random
import string

import happybase
host = '192.168.0.47'
class hbUnit():
    def __init__(self):
        self.host = host

    def getConn(self):
        try:
            #conn = happybase.Connection(host=self.host) #获取连接实例
            pool = happybase.ConnectionPool(size=3, host=self.host)# 创建连接，通过参数size来设置连接池中连接的个数, table_prefix='oa'
            # 获取连接
            with pool.connection() as conn:
                conn.open
                return conn
        except Exception as e:
            print('getConn wrong: %s' % format(e))

    # 关闭连接
    def closeConn(self, conn):
        try:
            if conn != None:
                conn.close()
        except Exception as e:
            print('closeConn wrong: %s' % format(e))
    # 创建表
    def createTable(self,tableName,families):
        try:
            conn = self.getConn()
            conn.create_table(tableName, families)
        except Exception as e:
            print('createTable wrong: %s' % format(e))

    # 返回单行数据，返回tuple
    def querySingleLine(self, tableName, rowkey):
        conn = self.getConn()
        t = conn.table(tableName)
        return t.row(rowkey)

    # 返回多行数据，返回dict
    def queryMultilLines(self, tableName, list):
        conn = self.getConn()
        t = conn.table(tableName)
        return dict(t.rows(list))

    # 批量插入数据
    def batchPut(self, tableName):
        conn = self.getConn()
        t = conn.table(tableName)
        batch = t.batch(batch_size=10)
        return batch

    # exmple
    # batch_put = batchPut(table)
    #     person1 = {'info:name': 'lianglin', 'info:age': '30', 'info:addr': 'hubei'}
    #     person2 = {'info:name': 'jiandong', 'info:age': '22', 'info:addr': 'henan', 'info:school': 'henandaxue'}
    #     person3 = {'info:name': 'laowei', 'info:age': '29'}
    #     with batch_put as bat:
    #         bat.put('lianglin', person1)
    #         bat.put('jiandong', person2)
    #         bat.put('laowei', person3)

    # 插入单条数据
    def singlePut(self, tableName, rowkey, data):
        conn = self.getConn()
        t = conn.table(tableName)
        t.put(rowkey, data=data)

    # 批量删除数据
    def batchDelete(self, tableName, rowkeys):
        conn = self.getConn()
        t = conn.table(tableName)
        with t.batch() as bat:
            for rowkey in rowkeys:
                bat.delete(rowkey)

    # 删除单行数据
    def singleDelete(self, tableName, rowkey):
        conn = self.getConn()
        t = conn.table(tableName)
        t.delete(rowkey)

    # 删除多个列族的数据
    def deleteColumns(self, tableName, rowkey, columns):
        conn = self.getConn()
        t = conn.table(tableName)
        t.delete(rowkey, columns=columns)

    # 删除一个列族中的几个列的数据
    def deleteDetailColumns(self, tableName, rowkey, detailColumns):
        conn = self.getConn()
        t = conn.table(tableName)
        t.delete(rowkey, columns=detailColumns)

    # 清空表
    def truncatTable(self, tableName, name, families):
        conn = self.getConn()
        conn.disable_table(tableName)
        conn.delete_table(tableName)
        conn.create_table(tableName, name, families)

    # 删除hbase中的表
    def deletTable(self, tableName):
        conn = self.getConn()
        conn.delete_table(tableName, True)

    # 扫描一张表
    def scanTable(self, tableName, row_start, row_stop, row_prefix):
        conn = self.getConn()
        t = conn.table(tableName)
        scan = t.scan(row_start=row_start, row_stop=row_stop, row_prefix=row_prefix)
        for key, value in scan:
            print(key, value)
    # 从a-zA-Z0-9生成指定数量的随机字符：
    def getRandom(self,num):
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        return (ran_str)