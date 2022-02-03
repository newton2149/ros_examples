import rclpy
from rclpy.node import Node

class BatteryInstance(Node):
    def __init__(self):
        super().__init__("battery_instance")


def main(args=None):
    rclpy.init(args=args)
    node = BatteryInstance()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
