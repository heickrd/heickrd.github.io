# Configuring ROS 2 in a Command Shell

Everytime you start a new command shell, you must configure a new ROS 2 workspace. It's as simple as typeing the following command:
```
source /opt/ros/eloquent/setup.bash
````

Once you have done that, you should be able to use any ros2 command.

If you do not want to type that command everytime you set up a new shell, you can add sourcing to your shell startup script. Run the 
following command to do so:
```
echo "source /opt/ros/eloquent/setup.bash" >> ~/.bashrc
```

To undo this, locate your system's shell script and remove the appended command. 

**NOTE**: This tutorial assumes that you are using the Eloquent ROS 2 distro. If you are using a different distro, replace 
eloquent in the above commands with the name of your distro.
