This tutorial is going to show you how to write your own publisher to send goals to the robot in a simulation.
1. First you want to have gazebo and Navigation2 running. Follow the instructions [here](http://emanual.robotis.com/docs/en/platform/turtlebot3/ros2_simulation/#turtlebot3-simulation-using-fake-node) to learn how.

2. I first suggest you follow along here with my example [code](goal_tutorial.py).
  
  First lets focus on the main focus of the code. Starting with the __init__ method.
  ```
  super().__init__('minimal_publisher')
  ```
  This first line constructs the class as a ROS2 node with the name 'minimal_publisher'. Its important to set up your node like this so it will interact correctly with other nodes.
  
  Next, I create the publisher that will send out the goals that I want. 
  ```
  self.goal_pub = self.create_publisher(PoseStamped, "move_base_simple/goal", 10)
  ```
  The main portion of this method to focus on are the first two parameters. "move_base_simple/goal" is the topic that I want to send my message to. PoseStamped is the type of message that I am sending.
  Its important to know what type of message your topic is expecting. If you do not know what kind of message your topic wants go to the command line and type:
  ```
  ros2 topic list -t
  ```
  This will list all topics and the message type that they are expecting. 
  
  Next, I create the PoseStamped objec that I want to send. 
  ```
          goal.header.frame_id = "odom"
        goal.pose.position.x = 11.7
        goal.pose.position.y = 10.4
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0
 ```
 For this example I am requesting for the robot to go to the coordinates x=11.7, y=10.4, and z=0, in the odom frame. If you 
 are unsure of the parameters in the message type you want. Almost all ROS types can be found online. 
 
 Next, I create a loop where the goal will be published infinitely. This is unecessary but makes the timings a bit more efficient.
  ```
  self.goal_pub.publish(goal)
  sleep(10)
  ```
  In this loop, I first publish the goal that I want by using the publish method of my publisher. I then have the code sleep for ten seconds.
  I have found that when dealing with publishing many goals in sequence it is best to give time for the goal to register or else the topic will get overloaded.
  
 Lastly we have the main method.
 ```
     rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()
 ```
 Most of this is simply setting up and destroyinig the node class, but the one method that I want to focus on is the .spin method.
 This method causes the method that it is given to run infintely, or until an interrupt occurs. This is useful for when you want nodes
 to constantly be running. 
 
 And there you have it. That is how you publish to a topic.
 
