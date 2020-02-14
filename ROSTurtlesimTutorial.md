# Simple ROS 2 Turtlesim Tutorial
 A good place to start with working with and testing ROS 2 is with the turtlesim application. <br>
 
 Once you have ROS 2 installed, you must install the turtlesim package. First, source your setup files in a new terminal.
 ```
 sudo apt update
 ```
 Then install the turtlesim package
 ```
 sudo apt install ros-eloquent-turtlesim
 ```
 
 Once the installation is finished you are ready to move onto testing the turtlesim. Make sure that you have configured your ROS 2 environment
 as shown by this [tutorial](ROSConfigure.md)
 
To launch the turtlesim apllication enter the following command into your configured terminal:
```
ros2 run turtlesim turtlesim_node
```

A blue window should appear with a turtle in the center. Along with this, the name of the node and the coordinates of the turtle will be displayed
in the command line. We will get into what nodes are later.

At the moment, you have no control over the turtle. To change this, open up a new terminal and make sure that it is configured correctly
then run the following command:
```
ros2 run turtlesim turtle_teleop_key
```
Now you should be able to use the arrow keys to move the turtle around the screen.Congratualions, you have now launched and used a
ROS2 application.
 
 
 
 
