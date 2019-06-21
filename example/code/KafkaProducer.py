import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = ['192.168.0.47:9092'])#,'192.168.0.106:9092','192.168.0.108:9092'
# Assign a topic
topic = 'my-topic'#主题

def test():
    print('begin')
    for i in range(100):
        producer.send(topic, value=b'value'+str(i).encode('utf-8'), key=b'key')
        print(i)
    print('done')

if __name__ == '__main__':
    test()
