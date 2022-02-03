#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.declare_parameter("number_to_publish",2)
        self.counter = self.get_parameter("number_to_publish").value     #Making parameters    
        self.publisher = self.create_publisher(Int64, "number_counter", 10)
        self.timer_ = self.create_timer(0.5, self.callback)

    def callback(self):
        msg = Int64()
        msg.data = self.counter
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing {self.counter}')
        self.counter+=1


def main(args=None):
    rclpy.init(args=args)   

    number_publisher_node = NumberPublisherNode()

    rclpy.spin(number_publisher_node)

    number_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
