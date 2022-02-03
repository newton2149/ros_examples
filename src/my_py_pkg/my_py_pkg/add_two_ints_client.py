import rclpy
from rclpy.logging import get_logger
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts,SetBool
from functools import partial
 
 
class AddTwoIntsClientNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("add_two_clients")
        self.call_add_two_ints_server(6,7)

    def call_add_two_ints_server(self,a,b):
        client = self.create_client(AddTwoInts,"add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server Add two Ints ")

        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        future = client.call_async(req)
        future.add_done_callback(partial(self.callBackfun,a=a,b=b))

    def callBackfun(self,future,a,b):
        try:
            response = future.result()
            self.get_logger().info(f"{response}")
        except Exception as e:
            self.get_logger().error(e)

 
 
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()