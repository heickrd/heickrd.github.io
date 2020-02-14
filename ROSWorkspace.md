# Creating and Building a ROS Workspace
This tutorial will show you how to build a workspace for your ROS packages.
1. Make sure that you have you current environment sourced for ROS. To find out how, click [here](ROSConfigure.md)
2. Next create a new directory and src folder for your workspace. Example commands for that are:
```
mkdir dev_ws
mkdir dev_ws/src
cd dev_ws/src
```
3. Once you are in the src folder you can being adding your own ROS packages. For this tutorial we will use some premade packages.
Type the follwing command into your shell:
```
git clone https://github.com/ros/ros_tutorials.git -b eloquent-devel
```
4. Once the packages have been added. Return to the root of your directory, in this example ~/dev_ws, and run:
```
colcon build
```
If you are successful you should get an output that looks like this:

```
Summary: 1 package finished [5.58s]
```
If this is the case, your ROS workspace has been correctly built. 

An issue that you may run into is to get the following error:
```
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.
```
If you are getting this error, it means that you either do not have a c++ compiler installed or it is not correctly configured in 
your CMakeLists.txt.<br>
If you do not have a c++ compiler run the follwing command:
```
sudo apt install g++
```
If you have a c++ compiler and are still getting the error, you will have to add the path to your compiler to either your 
environment variables or to the CMakeList.txt directly. 






