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
-Added tutorial for building ROS workspace

**Current TODO**: Get basic movement in robots and get Rviz to work with ROS2
