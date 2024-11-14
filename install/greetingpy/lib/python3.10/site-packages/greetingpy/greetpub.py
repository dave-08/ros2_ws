import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class mygreeting(Node):
    def __init__(self):
        super().__init__('mygreet')
        self.publisher = self.create_publisher(String,'greet',10)
        time = 5.0
        self.timer = self.create_timer(time,self.publish_greet)
        self.get_logger().info("greeting published")
    
    def publish_greet(self):
        msg = String()
        msg.data = "good morning"
        self.publisher.publish(msg)
        self.get_logger().info(f"publishing: {msg.data} ")

def main(args = None):
    rclpy.init(args = args)
    node = mygreeting()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()