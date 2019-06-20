import csv

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

host = ['192.168.0.47:9200'] #单机
#hosts = ['192.168.0.47:9200','192.168.0.106:9200','192.168.0.108:9200']#多节点

class esApi():
    def __init__(self, index_name, index_type=None,mapping = None,body = None):
        """
        :param index_name: 索引名称
        :param index_type: 索引类型
        """
        self.index_name = index_name
        self.index_type = index_type
        self.mapping = mapping
        self.body = body
        # 无用户名密码状态
        self.es = Elasticsearch(host)
        # 用户名密码状态
        # self.es = Elasticsearch(hosts, http_auth=('elastic', 'password'), port=9200)
    def create_index(self):#创建索引
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index=self.index_name)#ignore=[400, 404],ignore可以忽略异常对应的返回码，常见的有400表示索引已存在，404表示索引没找到。
            print(res)
            print('创建索引成功!')
            self.es.indices.put_mapping(index=self.index_name, doc_type=self.index_type, body=self.mapping)
            print('设置mapping成功!')
        else:
            self.es.indices.put_mapping(index=self.index_name, doc_type=self.index_type, body=self.mapping)
            print('设置mapping成功!')

    def delete_index(self):#删除索引
        if self.es.indices.exists(index=self.index_name) is True:
            res = self.es.indices.delete(index=self.index_name)#ignore=[400, 404],ignore可以忽略异常对应的返回码，常见的有400表示索引已存在，404表示索引没找到。
            print('删除索引成功!')

    def put_datas(self):#批量写入
        if self.es.indices.exists(index=self.index_name) is True:
            success, _= bulk(self.es,self.body,index=self.index_name, raise_on_error=True)
            print('批量写入成功 %d' % success)

    def deleteDataById(self):#根据id 删除一条数据
        if self.es.indices.exists(index=self.index_name) is True:
            res = self.es.delete(index=self.index_name, doc_type=self.index_type, id=self.body)
            print(res)
            print('删除成功')

    def deleteDataByBody(self):#根据查询条件删除数据
        if self.es.indices.exists(index=self.index_name) is True:
            res = self.es.delete_by_query(index=self.index_name, body=self.body)#新版没有doc_type
            print(res)
            print('根据查询条件删除数据成功')

    def getData(self):#查询数据
        if self.es.indices.exists(index=self.index_name) is True:
            res = self.es.search(index=self.index_name, body=self.body)
            print(res)
            print('查询数据成功')

    def updateDataByBody(self):#更新数据
        if self.es.indices.exists(index=self.index_name) is True:
            res = self.es.update_by_query(index=self.index_name,  body=self.body)
            print(res)
            print('更新数据成功')

def set_mapping():#定义映射
    mapping = {
        "properties": {
            "name": {
                "type": "text",
                "analyzer": "ik_smart",
                "search_analyzer": "ik_smart"
            },
            "content": {
                "type": "text",
                "analyzer": "ik_smart",
                "search_analyzer": "ik_smart"
            }
        }
    }
    return mapping

def set_date(index_name,doc_type_name):
    actions = []
    i = 1
    with open(u'./es.csv', 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            action = {
                "_index": index_name,
                "_type": doc_type_name,
                "_id": i,
                "_source": {
                    "name": row[0],
                    "content": row[1],
                }
            }
            i = i + 1
            actions.append(action)
    return actions

if __name__ == '__main__':
    index_name = 'index_demo'
    index_type = 'index_type'
    mapping = set_mapping()
    es = esApi(index_name,index_type)
    es.mapping = mapping
    #es.create_index()#创建索引

    #es.delete_index()#删除索引

    #es.body = set_date(index_name,index_type)#设置批量写入数据
    #es.put_datas()#批量写入

    #es.body = '1'#设置要删除数据的id
    #es.deleteDataById()#根据id 删除一条数据

    # es.body = {
    #       "query":{
    #             "match":{
    #                 "name":   "黄鹤楼"
    #             }
    #           }
    # }#设置要删除数据的查询条件
    #es.deleteDataByBody()#根据查询条件删除数据

    # es.body = {
    #     "query": {
    #         "type": {
    #             "value": "index_type"#指定文档类型
    #         },
    #     }
    # }
    # es.body = {
    #     "query": {
    #         "bool": {
    #             "must": [
    #                 {
    #                     "type": {
    #                         "value": "index_type"#指定文档类型
    #                     }
    #                 },
    #                 {
    #                     "match": {
    #                         "name":"七步诗"
    #                      }
    #                 }
    #             ]
    #          }
    #      }
    # }#联合查询条件设置
    # es.getData()#查询数据

    #将name=七步诗的字段值修改为'七步诗2'
    es.body = {
        "script": {
            "source": "ctx._source['name']='七步诗2'"
        },
        "query": {
            "bool": {
                "must": [
                    {
                        "type": {
                            "value": "index_type"  # 指定文档类型
                        }
                    },
                    {
                        "match": {
                            "name": "七步诗"
                        }
                    }
                ]
            }
        }
    }
    es.updateDataByBody()#更新数据