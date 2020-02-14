# ROS2 Install on Linux Mint:
1. Go to this address: https://index.ros.org/doc/ros2/Installation/Eloquent/Linux-Install-Debians/
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
Then use this command instead:<br>
```
sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `bionic` main" > /etc/apt/sources.list.d/ros2-latest.list'
```
3. From here you can follow the rest of the steps as normal
