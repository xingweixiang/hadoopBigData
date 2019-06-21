import time
from kafka import KafkaProducer

servers = ['192.168.0.47']#['192.168.0.47:9092','192.168.0.106:9092','192.168.0.108:9092']
producer = KafkaProducer(bootstrap_servers = ['192.168.0.47:9092'])#,'192.168.0.106:9092','192.168.0.108:9092'
# Assign a topic
topic = 'my-topic'#主题

def test():
    print('begin')
    for i in range(100):
        producer.send(topic, value=b'value'+str(i).encode('utf-8'), key=b'key')
        print(i)
    print('done')

def producer_message():
    producer = KafkaProducer(bootstrap_servers=servers)
    for i in range(100):
        msg = "some_message_bytes " + str(i)
        producer.send('kafka-topic', bytes(msg.encode("utf-8")))
        print(msg)

if __name__ == '__main__':
    test()
