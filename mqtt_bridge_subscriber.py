import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import paho.mqtt.client as mqtt

class MQTTBridge(Node):
    def __init__(self):
        super().__init__('bridge_subscriber')
        # ROS 2 Setup
        self.subscription = self.create_subscription(String, 'robot_commands', self.listener_callback, 10)
        
        # MQTT Setup
        self.mqtt_broker = "broker.hivemq.com"
        self.mqtt_topic = "fyp/robot/status"
        self.client = mqtt.Client()
        self.client.connect(self.mqtt_broker, 1883, 60)
        self.client.on_message = self.on_mqtt_message
        self.client.subscribe("fyp/robot/control")
        self.client.loop_start()
        self.get_logger().info('MQTT Bridge Initialized and Connected to Broker')

    def listener_callback(self, msg):
        command = msg.data
        self.get_logger().info(f'ROS 2 Received: "{command}"')
        
        # This is the "Bridge" part: Sending ROS data to MQTT
        self.client.publish(self.mqtt_topic, command)
        self.get_logger().info(f'MQTT Sent to {self.mqtt_topic}: "{command}"')
    def on_mqtt_message(self, client, userdata, msg):
        mqtt_command = msg.payload.decode()
        self.get_logger().info(f'MQTT Received from Cloud: "{mqtt_command}"')
def main(args=None):
    rclpy.init(args=args)
    bridge_node = MQTTBridge()
    try:
        rclpy.spin(bridge_node)
    except KeyboardInterrupt:
        pass
    bridge_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
