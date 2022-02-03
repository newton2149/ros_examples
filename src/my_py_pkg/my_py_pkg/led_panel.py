import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
from my_robot_interfaces.msg import LedStatus

class LedPanel(Node):
    def __init__(self):
        super().__init__("led_panel")
        self.service = self.create_service(SetLed,"set_led",self.callback_battery)
        self.publisher = self.create_publisher(LedStatus,"led_states",10)
        self.get_logger().info("Service Led Panel Started")


    def callback_battery(self,request,response):
        if request.operation == "off":
            response.success = True
            msg = LedStatus()
            msg.states = request.operation
            self.publisher.publish(msg)
            self.get_logger().info("Message is been set")

        elif request.operation == "on":
            response.success = False
            msg = LedStatus()
            msg.states = request.operation
            self.publisher.publish(msg)
        return response



def main(args=None):
    rclpy.init(args=args)
    node = LedPanel()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


