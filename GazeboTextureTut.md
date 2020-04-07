# Adding an Image File as a Texture in Gazebo

In this tutorial I am going to show you how to add an immage file as a texture using gazebo. 
For this particular tutorial I will be using the model files that come with the turtlebot3.

 First, navigate to where your gazebo models are stored. When working with the turtlebot models, the path should look something like
/home/{username}/turtlebot3_ws/src/turtlebot3/turtlebot3_simulations/turtlebot3_gazebo/models
- In this example I will be working with the premade world turtlebot3_world. If you want to know how to create your onw gazebo
world click [here](https://www.youtube.com/watch?v=7MH15kbuPdk) for a video tutorial. 

 Next, click on the world you want to use, in this case turtlebot3_world.
 
 Now open up the model.sdf file
 
 Scroll down until the bottom of the file. (The majority of this file is dedicated to creating the models for the rest of the world. 
They are unimportant for this tutorial but you might find in helpful to look through a few of them and see
how they are setup). Right before the ```</link>``` line, add in the follwing code.
```
      <collision name='test_box'>
          <pose> 2 -.5 .5 0 0 0</pose>
          <geometry>
            <box>
              <size>.25 .25 .25</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='test_box'>
          <pose> 2 -.5 .5 0 0 0</pose>
          <geometry>
            <box>
              <size>.25 .25 .25</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>  
```
These lines add in the collion and visual aspects of a box model. You can see that you can modify the size and position of the model, 
as well as modify the visual aspect apart from the collision aspect.
Now if you launch the turtlebot3_world in gazebo. You will see a grey box floating towards the top of the world. This is how you
add a model to the world. In this case it is just a box, but there are many other built-in shapes that it could be.

Now we will move onto adding a custom texture to the model. Move back to the turtlebot3_world folder and create a new folder called "materials".
In this folder create two new folders, one called scripts and one called textures. 
In the scripts folder, paste in the image you want to use as a texture. In this case, mine is called thumbnail.jpeg
Next, move to the scripts folder, create a new file called "test.material" and add the following code into it. 
```
material testMat/test
{
    recieve_shadows false
    technique
    {
        pass
        {
            texture_unit
            {
                texture thumbnail.jpeg
            }
        }
    }
}
```
In your case, the jpeg should be named whatever you named your image.

We now need to apply this material to the model we created earlier. Go back to the model.sdf file and the code that we added before.
In the visual part of your model, change the code to look like this.
```
        <visual name='face_box'>
          <pose> 2 -.5 .5 0 0 0</pose>
          <geometry>
            <box>
              <size>.25 .25 .25</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://turtlebot3_world/materials/scripts</uri>
              <uri>model://turtlebot3_world/materials/textures</uri>
              <name>testMat/test</name>
            </script>
          </material>
        </visual>  
```
This points the models visuals to the material script that we created before. Now if you launch this world in gazebo, you should
see that the cube we created before noew has your image on it.

And that is how you create a model in gazebo and add a custom texture to it. 


