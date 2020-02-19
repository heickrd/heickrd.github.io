# Installing Turtlebot 3 Gazebo Simulation
This installation assumes that you are using ROS eloquent. If not, replace 'eloquent' with your ROS distro name<br>
1. As per usual when working with ROS, make sure your workspace environment is [configured](ROSConfigure.md)<br>
2. Then you must install the needed ROS dependent packages.<br>

***Gazebo***
```
curl -sSL http://get.gazebosim.org | sh
sudo apt install ros-eloquent-gazebo-*
```
***Cartographer***
```
sudo apt install ros-eloquent-cartographer
sudo apt install ros-eloquent-cartographer-ros
```
***Navigation2***
```
 sudo apt install ros-eloquent-navigation2
 sudo apt install ros-eloquent-nav2-bringup
 ```
 ***vcstool***
 ```
 sudo apt install python3-vcstool
 ```
 2. Next install the Turtlebot3 Packages
 ```
 mkdir -p ~/turtlebot3_ws/src
 cd ~/turtlebot3_ws
 wget https://raw.githubusercontent.com/ROBOTIS-GIT/turtlebot3/ros2/turtlebot3.repos
 vcs import src < turtlebot3.repos
 colcon build --symlink-install
 ```
 3. Lastly, save the bash commands for setup
 ```
 echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
 echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
 source ~/.bashrc
 ```
 
