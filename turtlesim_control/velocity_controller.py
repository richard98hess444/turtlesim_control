import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class VelocityController(Node):

    def __init__(self):
        super().__init__('velocity_controller')
        
        self.curr_x = 0
        self.curr_y = 0
        self.curr_t = 0
        
        self.init_pubs_and_subs()

    def init_pubs_and_subs(self):
        self.sub_pose = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            1)
        self.sub_pose
        
    def pose_callback(self, pose: Pose) -> None:
        self.curr_x = pose.x
        self.get_logger().info(f'Pose x: {self.curr_x}.')
        

def main(args=None):
    rclpy.init(args=args)
    node = VelocityController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()