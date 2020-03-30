# ROS 2 Facial Recognition Project Blog
For a current list of all tutorials, click [here](TutorialList.md)
## Week One:
- Finished syllabus for class and worked on literature review

## Week Two-Three:
- Began installing ROS 2. Had some issues setting up ROS on personal laptop as Virtual Machine was incompatible with ROS 2. Acquired a school laptop to install on instead. 
- Worked through ROS 2 tutorials. 
- **TODO**: Need to install ROS onto school laptop

## Week Four:
- Installed Facial Recognition library -Recognition Library Found here: https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/
- Added myself to the dataset and trained the software on my face.
- Tested the software at various angles, distances, lightings, etc. The software works realiably up to about 10 feet straight on and about 5 feet from an angle facing up from the ground. Though when placed at the average height of a turtlebot the reliablity went up to about 7 feet. I believe that a larger dataset will increase performance at range.
- Worked on getting output from the software for later use.
- Added more faces to the dataset and the software easily distingushes between people up close. Once again I believe that increasing the dataset will increase performance at larger distances.
- **TODO**: Integrate the software into a ROS environment
- Possible Research Concept: Finding the minimum necessary dataset size to have software running optimally.

## Week Five:
- Set up github.io page
- Installed ROS 2. For Linux Mint install instructions click [here](ROSinstall.md)
- Added tutorials for ROS 2 command line [configuration](ROSConfigure.md) and a basic ROS2 turtlesim [tutorial](ROSTurtlesimTutorial.md)
- Added tutorial for building ROS [workspace](ROSWorkspace.md)
- FIgured out how to run Rviz, tutorial [here](RvizRun.md)

**Old TODO**: Get basic movement in robots and get Rviz to work with ROS2<br>
**Current TODO**: Get movement in robots and get robot integration into RViz. Test one photo dataset with facial recognition.

## Week Six
- Installed Turtlebot 3 Gazebo, tutorial [here](GazeboInstall.md)
- Began testing with Gazebo simulation.
- Worked with mapping with Cartographer(work needed)
- Got basic movement in robot
- Began advanced robot movement. Using sensors to detect obstacles and avoid them. 

**OLD TODO**: Get movement in simulated robot. Get moving with a shortest path algorithm. <br>
**Current TODO**: Get advanced movement working. If possible, get mapping to work in order to use shortest path algorithm. 

## Week Seven
- Attempted to get mapping to work with gazebo and cartographer
  - This was very unsucessful as cartographer has not been ported over correctly and it seems that gazebo does not publich transform data. 
- Began porting over random navigation from c++ to python

**Current TODO**: Decide whether to continue on with mapping or shift focus to random navigation. As well as attempt to get facial recognition to work through the robots camera. Test movement with actual robot to see if mapping will work. 

## Week Eight and Nine
-Got consistent goal sending to work. Allowing for navigation and movement around a given map.
-Created tutorial for goal sending

**Current TODO**: Work on getting the turtlebot video stream into the facial recognition software

## Week 10
-Got facial recognition to run in a ROS workspace and created all necessary launch files.
-Began research into action clients

**Current TODO**: Get turtlebot video stream to feed into facial recognition software.

