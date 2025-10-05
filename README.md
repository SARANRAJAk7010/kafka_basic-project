# kafka_basic-project
Kafka basic project like ordering info.

About:   
Producer: Sends order messages to Kafka topic `orders`.   
Consumer: Reads messages from topic `orders` and prints order details.  
Docker: Runs Kafka broker using Docker Compose.  

How to run:

pip3 install confluent-kafka  //It actually makes kafka and python linked.  

docker compose up -d

Producer -> kafka -> Consumer

consumer output:-   
<img width="1328" height="576" alt="image" src="https://github.com/user-attachments/assets/5ae0d263-8553-471f-ada1-195a53620cc4" />

