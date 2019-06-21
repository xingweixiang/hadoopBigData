# coding=utf-8
import json
from example.code.hbUnit import hbUnit
#from modules.hbase import hb_blue


#@hb_blue.route('/getWarehouse',methods = ['GET','POST'])
def getWarehouse():
    result = None
    data_list = []
    hb = hbUnit()
    try:
        conn = hb.getConn()
        table = conn.table('oa_warehouse')
        num = 0
        for key, data in table.scan():
            print(key, data)
            dict_info = {'rowkey':str(key)}
            num = num + 1
            dict_info['num'] = num
            if b'tableInfo:secretKey' in data:
                secretKey = data[b'tableInfo:secretKey'].decode("utf-8")
            else:
                secretKey = ''
            dict_info['secretKey'] = secretKey
            if b'tableInfo:tableName' in data:
                tableName = data[b'tableInfo:tableName'].decode("utf-8")
            else:
                tableName = ''
            dict_info['tableName'] = tableName
            if b'tableInfo:tableRemark' in data:
                tableRemark = data[b'tableInfo:tableRemark'].decode("utf-8")
            else:
                tableRemark = ''
            dict_info['tableRemark'] = tableRemark
            if b'tableInfo:account' in data:
                account = data[b'tableInfo:account'].decode("utf-8")
            else:
                account = ''
            dict_info['account'] = account
            if b'tableInfo:userName' in data:
                userName = data[b'tableInfo:userName'].decode("utf-8")
            else:
                userName = ''
            dict_info['userName'] = userName
            data_list.append(dict_info)
            print(data_list)
        result = json.dumps({"code": 0, "msg": "", "data": data_list})
    except Exception as e:
        print('wrong: %s' % format(e))
    finally:
        hb.closeConn(conn)
    return result

def getTablesName():
    hb = hbUnit()
    conn = hb.getConn()
    print (conn.tables())
    hb.closeConn(conn)

def getTable(tableName):
    hb = hbUnit()
    conn = hb.getConn()
    print(conn.is_table_enabled(tableName))
    cells = conn.table(tableName).families()
    print(cells)
    hb.closeConn(conn)

# 删除hbase中的表
def deleteTable(tableName):
    hb = hbUnit()
    conn = hb.getConn()
    try:
        print(conn.is_table_enabled(tableName))
        conn.delete_table(tableName, True)
        print('delete success')
    except Exception as e:
        print('delete wrong: %s' % format(e))
    finally:
        hb.closeConn(conn)
# 创建hbase中的表
def createTable():
    print('createTable:start')
    families = {
        "tableInfo": dict()
    }
    hb = hbUnit()
    hb.createTable('oa_warehouse', families)
    print('createTable:end')
def putData():
    hb = hbUnit()
    conn = hb.getConn()
    table = conn.table('oa_warehouse')
    cell = {'tableInfo:secretKey': 'key', 'tableInfo:account': 'user', 'tableInfo:userName': '管理员'}
    table.put('keyid',cell)
    hb.closeConn(conn)
if __name__ == '__main__':
    #hb_warehouse()
    #createTable()
    #putData()
    getTablesName()
    #getTable('oa_warehouse')
    # hb = hbUnit()
    # conn = hb.getConn()
    # table = conn.table('oa_warehouse')
    # row = table.row(row='keyid', include_timestamp=True)
    # print (row)
    #getWarehouse()
    #deleteTable('oa_warehouse')

