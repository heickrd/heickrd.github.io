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
