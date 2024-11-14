#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class UGVControl(Node):
    def __init__(self):
        super().__init__('ugv_control')
        self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.left_wheel_pub = self.create_publisher(Float64, 'left_wheel_velocity', 10)
        self.right_wheel_pub = self.create_publisher(Float64, 'right_wheel_velocity', 10)
        self.wheel_separation = 0.5
        self.wheel_radius = 0.1

    def cmd_vel_callback(self, msg):
        linear_velocity = msg.linear.x
        angular_velocity = msg.angular.z
        left_wheel_velocity = (linear_velocity - angular_velocity * self.wheel_separation / 2) / self.wheel_radius
        right_wheel_velocity = (linear_velocity + angular_velocity * self.wheel_separation / 2) / self.wheel_radius
        self.left_wheel_pub.publish(Float64(data=left_wheel_velocity))
        self.right_wheel_pub.publish(Float64(data=right_wheel_velocity))
        self.get_logger().info(f"Left wheel velocity: {left_wheel_velocity}, Right wheel velocity: {right_wheel_velocity}")

def main(args=None):
    rclpy.init(args=args)
    node = UGVControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
