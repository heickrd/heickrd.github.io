# ROS2 Install on Linux Mint:
1. Go to this address: [https://index.ros.org/doc/ros2/Installation/Eloquent/Linux-Install-Debians/](https://index.ros.org/doc/ros2/Installation/Eloquent/Linux-Install-Debians/)
2. Follow all of the steps until the command: <br>
```
 sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
```
You must check what version of ubuntu you are running first. Use the command:<br>
```
lsb_release -a
```
To find the codename of your Ubuntu. If your codename is not one of the following:
- bionic
- cosmic
- disco
- eoan
- focal
- stretch
- xenial

<br>Then use this command instead:<br>
```
sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `bionic` main" > /etc/apt/sources.list.d/ros2-latest.list'
```
3. From here you can follow the rest of the steps as normal
4. Once you are finished installing ROS2, you will need to install colcon in order to build ROS2 workspaces:
```
sudo apt install python3-colcon-common-extensions
```
You are now done with the last of the necessary installations, but here are a few more install pakcages that you may find useful.
Git: 
```
sudo apt install git-all
```
Rosdep, used for easier installation of ROS packages:
```
sudo apt-get install python-rosdep
sudo rosdep init
rosdep update
```


