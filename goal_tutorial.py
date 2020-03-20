import rclpy
import rclpy.qos
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from time import sleep


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        self.goal_pub = self.create_publisher(PoseStamped, "move_base_simple/goal", 10)
        goal = PoseStamped()
        goal.header.frame_id = "odom"
        goal.pose.position.x = 11.7
        goal.pose.position.y = 10.4
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0
        i = goal.pose.position.x
        while True:
            print(i)
            print("\n")
            print(goal)
            self.goal_pub.publish(goal)
            sleep(10)
            i = i -1
            goal.pose.position.x = i

    

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
