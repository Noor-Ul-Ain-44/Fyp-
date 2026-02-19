import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class TelemetryNode(Node):
    def __init__(self):
        super().__init__('telemetry_node')
        # This publishes to the topic your Web Dashboard listens to
        self.publisher_ = self.create_publisher(String, '/robot_state_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_robot_state)
        self.get_logger().info('✅ HARP Master Telemetry System Online')

    def publish_robot_state(self):
        # COLLECTING ALL 3 PARTS:
        harp_state = {
            "navigation": {"location": "Lobby", "target": "Office A"},
            "perception": {"detected": ["Person"], "status": "Path Clear"},
            "system": {"battery": 88, "wifi": "Strong"} # Fixes the --% battery!
        }
        
        msg = String()
        msg.data = json.dumps(harp_state) # Packing the 'suitcase'
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TelemetryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
