from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', bootstrap_servers = ['192.168.0.47:9092','192.168.0.106:9092','192.168.0.108:9092'])

def test_consumer():
    for msg in consumer:
        print(msg.value)

if __name__ == '__main__':
    test_consumer()