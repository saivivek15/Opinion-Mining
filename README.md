Start kafka

-> bin/zookeeper-server-start.sh config/zookeeper.properties
-> bin/kafka-server-start.sh config/server.properties
 
Start elastic search and kibana (Installed using Homebrew for macOS)

-> Create a Mapping for sentiment index for elastic search, execute the curl command from the curl file.


Execute:
 -python producer.py
 -spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.0 consumer.py localhost:2181 tweets
	
Inspect:
 	- https://localhost:5601
	- Create an index pattern in kibana
	- In visualize, select SUM for fields positive, negative and neutral.
	- Save visualization
	- In dashboard, create a dashboard and set auto-refresh time for 1 minute.
	

