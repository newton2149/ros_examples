import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import HardwareStatus
from example_interfaces.msg import Float64
 
 
class HardwareStatusPublisher(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("hw_status_publisher") 
        self.hw_status_publisher_ = self.create_publisher(HardwareStatus,"harware_status",10)
        self._timer = self.create_timer(0.5,self.publish_status)
        self.get_logger().info("Hardware Status publisher")

    def publish_status(self):
        msg = HardwareStatus()
        msg.tempreature=45
        msg.are_motors_ready=True
        msg.debug_message="Nothing Special"
        self.hw_status_publisher_.publish(msg)
            



 
 
def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisher() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()