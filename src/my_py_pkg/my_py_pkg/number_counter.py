#!usr/bin/env/python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64 
from example_interfaces.srv import SetBool

class NumberCounter(Node):

    def __init__(self):
        super().__init__('number_counter')
        self.subscriber = self.create_subscription(Int64, 'number_counter', self.count_callback, 10)
        self.publisher = self.create_publisher(Int64, 'number',10)
        self.service = self.create_service(SetBool,"reset_counter",self.callback_server)
        self.get_logger().info("Reset counter service activated")
        
    def callback_server(self,request,response):
        response.data = request.data
        self.get_logger().info(f"To reset counter {response.data}")
        return response

    def count_callback(self,msg):
        self.get_logger().info('I heard: "%d"' % msg.data)
        self.publisher.publish(msg)


    


def main(args=None):
    rclpy.init(args=args)
    number_counter = NumberCounter()
    rclpy.spin(number_counter)
    rclpy.shutdown()
