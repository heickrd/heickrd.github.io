## Simple Gazebo Tutorial
This will be a very simple tutorial for you to begin getting used to working with Gazebo and the simulated turtlebot.<br>

1. To begin, we will simply start by launching an empty world in gazebo. Though before you are able to launch gazebo you have to 
specify the type of turtlebot you will want to work with. Use the following command, but replace ```$(TB3_MODEL}``` with burger, waffle,
or waffle_pi.
```
export TURTLEBOT3_MODEL=${TB3_MODEL}
```
2. Next we can bring up the simulation. 
```
ros2 launch turtlebot3_gazebo empty_world.launch.py
```
You should see the robot that you chose on a blank plane. 
If you want to launch simulation with premade environments, you can use one of the follwing commands
```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
or
```
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```

***Controlling your Turtlebot***<br>
To control your turtlebot, keep your gazebo simulation running and start a new command line. Configure the enrionment for ROS and then run the following commands:
```
export TURTLEBOT3_MODEL=${TB3_MODEL}
```
once again substituting ```${TB3_MODEL}``` with the name of your robot. Then:
```
ros2 run turtlebot3_teleop teleop_keyboard
```
Now, while still on your command line, you should be able to use the w,a,s,d keys to control your robot. 

 
