import json
import uuid

from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092" #This connects to kafka
}

producer = Producer(producer_config) #makes connection localhost above

def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivery succeeded: {msg.value().decode("utf-8")}") #change log again to readable format
        #f ensures ["utf-8") take value if not f then op be like ("utf-8")
        print(f"Delivered to {msg.topic()} : partition {msg.partition()} : offset: {msg.offset()}")



order = {  #dictonery
    "order_id": str(uuid.uuid4()), #uuid means unique diff id, 4 refers version
    "user":"saran",
    "item":"Chicken Briyani",
    "quantity":2
}


#dict is written in py, which is not understanble by other so changing into json.
#But kafka needs in bytes so again encode this coz data send over the network as binary also kafka topics store messages in bytes.
value = json.dumps(order).encode("utf-8")

producer.produce("orders", value=value, #save values in topic named orders, if not it creates too
                 callback=delivery_report #func to display logs whether its delivered or not
                 )

producer.flush() # Force send everything that's still buffered, make sure reaches kafka


