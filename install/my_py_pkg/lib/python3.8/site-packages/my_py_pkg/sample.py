import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
import time
from example_interfaces.msg import Float64

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


class DistanceNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("ultrasonic")
        self.distance_publisher = self.create_publisher(
            Float64, "distance_status", 10)
        self._timer = self.create_timer(1, self.publish_distance)
        self.get_logger().info("Ultrasonic node established")

    def publish_distance(self):
        msg = Float64()
        msg.data = distance()
        self.distance_publisher.publish(msg)
        self.get_logger().info(f'Distance {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = DistanceNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
