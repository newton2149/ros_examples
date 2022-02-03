import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_sim")
        self.pose = None
        self.pose_subscriber = self.create_subscription(Pose,"turtle/pose",self.callback_turtle_pose,10)


    def callback_turtle_pose(self,msg):
        self.pose = msg
        



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
