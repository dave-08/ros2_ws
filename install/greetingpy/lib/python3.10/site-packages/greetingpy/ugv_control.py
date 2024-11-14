#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class UGVController(Node):
    def __init__(self):
        super().__init__('ugv_controller')
        
        # Create a publisher to the cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Set up a timer to alternate movement
        timer_period = 2.0  # 2 seconds interval
        self.timer = self.create_timer(timer_period, self.move_ugv)
        
        # Track movement direction
        self.moving_forward = True  # Initial direction

        self.get_logger().info('UGV Controller Node started.')

    def move_ugv(self):
        # Create a Twist message
        msg = Twist()

        # Set linear and angular velocities
        if self.moving_forward:
            msg.linear.x = 0.5  # Move forward with 0.5 m/s
            self.get_logger().info("Moving forward")
        else:
            msg.linear.x = -0.5  # Move backward with -0.5 m/s
            self.get_logger().info("Moving backward")

        # Publish the command
        self.publisher_.publish(msg)
        self.moving_forward = not self.moving_forward  # Toggle direction

def main(args=None):
    rclpy.init(args=args)
    controller = UGVController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
