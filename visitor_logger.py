import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sqlite3
import paho.mqtt.client as mqtt
import json
import os
from datetime import datetime

class VisitorLogger(Node):
    def __init__(self):
        super().__init__('visitor_logger')
        
        # 1. SQLite Setup
        self.db_path = os.path.expanduser('~/robot_data.db')
        self.init_db()

        # 2. MQTT Setup (For Admin Dashboard)
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect("broker.hivemq.com", 1883, 60)

        # 3. ROS 2 Subscriber
        self.subscription = self.create_subscription(
            String, 'visitor_entry', self.log_callback, 10)
        
        self.get_logger().info('SQLite & MQTT Logger Started!')

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS visitors 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           timestamp TEXT, name TEXT)''')
        conn.commit()
        conn.close()

    def log_callback(self, msg):
        visitor_name = msg.data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to SQLite
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors (timestamp, name) VALUES (?, ?)", (timestamp, visitor_name))
        conn.commit()
        conn.close()

        # Publish to IoT Admin Dashboard
        iot_payload = json.dumps({"visitor": visitor_name, "time": timestamp})
        self.mqtt_client.publish("fyp/visitor/history", iot_payload)
        
        self.get_logger().info(f'Logged & Published: {visitor_name}')
