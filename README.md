The objective is to demonstrate a simple publisher-subscriber operation in a docker container
Publisher sends mock IMU data on a channel called "IMU" every 1 second. Subscriber prints the message

Steps
1. gh repo clone AtiMotors/simple_pub_sub
2. cd simple_pub_sub
3. docker-compose up --build
