import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
 
 
class BatteryStatus(Node):
    def __init__(self):
        super().__init__("battery_status")
        self.create_service(SetLed,"set_led",self.callback_battery)

    def callback_battery(self,request,response):
        if request.operation == "off":
            response.success = True
        elif request.operation == "on":
            response.success = False
        return response

 
 
def main(args=None):
    rclpy.init(args=args)
    node = BatteryStatus() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()