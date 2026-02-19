import rclpy
from rclpy.node import Node
from std_msgs.msg import String # We will publish a simple String message

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        # Create a publisher on the topic '/robot_command' with String message type
        self.publisher_ = self.create_publisher(String, 'robot_command', 10)
        timer_period = 1.0  # seconds (publish every 1 second)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        # Simple alternating messages to simulate a command
        if self.i % 2 == 0:
            msg.data = 'MOVE_FORWARD'
        else:
            msg.data = 'STOP'

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing Command: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = CommandPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

