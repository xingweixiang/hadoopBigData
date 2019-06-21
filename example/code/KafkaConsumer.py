from kafka import KafkaConsumer
from kafka import TopicPartition
'''
auto.offset.reset 
earliest 
当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，从头开始消费 
latest 
当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，消费新产生的该分区下的数据 
none 
topic各分区都存在已提交的offset时，从offset后开始消费；只要有一个分区不存在已提交的offset，则抛出异常
'''
servers = ['192.168.0.47']#['192.168.0.47:9092','192.168.0.106:9092','192.168.0.108:9092']
consumer = KafkaConsumer('my-topic',auto_offset_reset='earliest', bootstrap_servers = servers)
test_topic = 'my-topic'

def test_message():
    for msg in consumer:
        print(msg.value)
# 消费方式1，默认消费所有分区的消息
def consumer_message1():
    consumer = KafkaConsumer(test_topic,auto_offset_reset='earliest',
                             bootstrap_servers=servers)
    # consumer = KafkaConsumer('kafka-topic', bootstrap_servers=servers)
    for msg in consumer:
        print(msg.value)

# 消费方式2, 指定消费分区
def consumer_message2():
    consumer = KafkaConsumer(auto_offset_reset='earliest',bootstrap_servers=servers,
                             group_id="kafka-group-id")
    consumer.assign([TopicPartition('my-topic', 0)])
    for msg in consumer:
        print(msg)

# 消费方式3，手动commit，生产中建议使用这种方式
# def consumer_message3():
#     consumer = KafkaConsumer(auto_offset_reset='earliest',bootstrap_servers=servers,
#                              consumer_timeout_ms=1000,
#                              group_id="kafka-group-id",
#                              enable_auto_commit=False)
#     for msg in consumer:
#         print(msg)
#         consumer.commit()

# 获取topic列表以及topic的分区列表
def retrieve_topics():
    consumer = KafkaConsumer(bootstrap_servers=servers)
    print(consumer.topics())

# 获取topic的分区列表
def retrieve_partitions(topic):
    consumer = KafkaConsumer(bootstrap_servers=servers)
    print(consumer.partitions_for_topic(topic))

# 获取Consumer Group对应的分区的当前偏移量
def retrieve_partition_offset():
    consumer = KafkaConsumer(bootstrap_servers=servers,
                             group_id='kafka-group-id')
    tp = TopicPartition('kafka-topic', 0)
    consumer.assign([tp])
    print("starting offset is ", consumer.position(tp))

if __name__ == '__main__':
    consumer_message1()
    #test_message()