import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
class RobotNewsStationNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("robot_news_station") # MODIFY NAME

        self.robot_name = "C3PO"

        self.publisher = self.create_publisher(String , "robot_news", 10) # MODIFY NAME
        self.timer_ = self.create_timer(0.5, self.publish_news) 
        self.get_logger().info("Robot News Station Has benn started")

    def publish_news(self):
        msg = String() # MODIFY NAME
        msg.data = "Hi, this is "+ str(self.robot_name) + " from Robot News Station" # MODIFY NAME
        self.publisher.publish(msg) # MODIFY NAME
 
 
def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
