from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError
from kafka.admin import ConfigResource, ConfigResourceType

servers = ['192.168.0.47:9092','192.168.0.106:9092','192.168.0.108:9092']
admin = KafkaAdminClient(bootstrap_servers=servers)

# 创建topic
def create_topic():
    try:
        new_topic = NewTopic("create-topic", 8, 3)
        admin.create_topics([new_topic])
    except TopicAlreadyExistsError as e:
        print(e.message)

# 删除topic
def delete_topic():
    admin.delete_topics(["create-topic"])

# 获取消费组信息
def get_consumer_group():
    # 显示所有的消费组
    print(admin.list_consumer_groups())

    # 显示消费组的offsets
    print(admin.list_consumer_group_offsets("kafka-group-id"))

# 获取topic的配置信息
def get_topic_config():
    resource_config = ConfigResource(ConfigResourceType.TOPIC, "create-topic")
    config_entries = admin.describe_configs([resource_config])
    print(config_entries.resources)