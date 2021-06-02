import redis
import time
import os

# set variable if run locally
# export param_a=hello_world

# wait for request
subscriber = redis.StrictRedis(host='redis')
publisher = redis.StrictRedis(host='redis')
pub = publisher.pubsub()
sub = subscriber.pubsub()
sub.subscribe('example_server')
print('listening..')
while True:
    # receive
    while True:
        message = sub.get_message()
        if message and message['type'] != 'subscribe':
            incoming_text = message['data'].decode("utf-8")
            print('received')
            break
        time.sleep(0.1)

    # generate
    result =  incoming_text + ' ' + str(os.environ['param_a']) + ' ok'
    print('sending:', result)
    # send
    publisher.publish("example_client", result)
    print('listening..')
