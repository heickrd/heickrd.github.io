# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import rclpy.qos
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from time import sleep


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        #print("Made it init")
        #self.scan_sub = self.create_subscription(LaserScan, 'scan', self.scan_callback, qos_profile=rclpy.qos.qos_profile_sensor_data)
        #print("After scan")
      #  self.odom_sub = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)
     #   self.cmd_vel_pub = self.create_publisher(Twist, "cmd_vel", 10)
        self.goal_pub = self.create_publisher(PoseStamped, "move_base_simple/goal", 10)
        vel = Twist()
        vel.linear.x = 1.0
        vel.angular.z = 1.0
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

        print("After pub")

    

def main(args=None):
    rclpy.init(args=args)
    print("In main")
    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    print("After spin")
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
