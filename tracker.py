import json
import uuid

from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",  #This actually connects to kafka
    "group.id": "order-tracker",  #it assigns your consumer to a consumer group named order-tracker,Can't see this anywhere. it is present inside kafka meta-data
    "auto.offset.reset": "earliest" #it tells kafka where to start reading text, earliest means latest
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])  #tells consumer that this topics to read and publish it. If only subsribe it checks and respond.
print("Consumer is running & subscribed")

try:
    while True:
        msg = consumer.poll(1.0)  #waits up to 1 sec to respond
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        value=msg.value().decode("utf-8")
        order=json.loads(value)  #converts to JSON type
        print(f"Received order : {order['quantity']} x {order['item']} from {order['user']}"
        #op: Received order: 3 * Apple from saran
except KeyboardInterrupt:  #itworks when user press manually like ctrl c in the keyboard
    print("\n Stopping consumer")

finally:
    consumer.close()