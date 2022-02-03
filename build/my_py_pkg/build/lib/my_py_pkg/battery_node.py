import rclpy
from rclpy import client
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
from functools import partial



class BatteryInstance(Node):
    def __init__(self):
        super().__init__("battery_instance")

        self.call_led_server('off')
        self.call_led_server('on')
    
    def call_led_server(self,operation):
        client = self.create_client(SetLed,"set_led",)
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Server Set Led Starting up")
        
        req = SetLed.Request()
        req.operation = operation
        future = client.call_async(req)
        future.add_done_callback(partial(self.callback_func,operation=operation))

    def callback_func(self,future , operation):
        try:
            response = future.result()
            self.get_logger().info(f"{response.success}")

        except Exception as e :
            self.get_logger().error(e)           


 

def main(args=None):
    rclpy.init(args=args)
    node = BatteryInstance()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
