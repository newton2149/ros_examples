import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts
 
class AddTwoIntServerNode(Node):
    def __init__(self):
        super().__init__("add_two_int_server") 
        self.server_ = self.create_service(AddTwoInts,"add_two_ints",self.callback_add_two_ints)
        self.get_logger().info("Add service activated")
    
    def callback_add_two_ints(self,request,response):
        response.sum = request.a + request.b
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
        return response
 
 
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntServerNode()
    rclpy.spin(node)
    rclpy.shutdown()
