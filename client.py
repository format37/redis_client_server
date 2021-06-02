import redis
import time


def example_request(question):
    subscriber = redis.StrictRedis(host='192.168.1.23')
    publisher = redis.StrictRedis(host='192.168.1.23')
    pub = publisher.pubsub()
    sub = subscriber.pubsub()
    sub.subscribe('example_client')
    # send
    print('sending')
    publisher.publish("example_server", question)
    # receive
    print('receiving')
    while True:
        message = sub.get_message()
        if message and message['type']!='subscribe':
            return message['data'].decode("utf-8")
            break
        time.sleep(0.1)


article_text = "test"

print('requested..')
print(example_request(article_text))
print('received!')
