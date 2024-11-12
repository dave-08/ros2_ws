import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class mygreetingsub(Node):
    def __init__ (self):
        super().__init__ ("mysubgreet")
        self.subscriber = self.create_subscription(String,'greet',self.callback,10)
        self.get_logger().info("subscriber started")
    
    def callback(self,msg):
        self.get_logger().info(f"greeting is : {msg.data}")
    

def main(args = None):
    rclpy.init(args=args)
    node = mygreetingsub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
