import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class SmartPhoneNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("smartphone")  # MODIFY NAME
        self.subscriber = self.create_subscription(
            String, "robot_news", self.callback, 10)
        self.get_logger().info("smartphone node started")

    def callback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = SmartPhoneNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
