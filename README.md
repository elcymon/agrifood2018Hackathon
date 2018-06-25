# Agri-food Robotics Workshop - Beetroot Hackathon #

This folder provides an initial set up for solving the beetroot challenge of the Agri-food Robotics 
workshop 2018.

The folder '/data/Train' contains 50 labeled images. Each image contains one beetroot in an unknown
position, which can be classified as either good or bad. The proportion of good vs bad beetroots is 
similar. A cvs file within the folder provides training labels for both the position and the quality 
of the beetroot.

The folder '/src' contains example python code to process the beetroot images and move the r12 robotics arm.
The file 'example_vision.py' shows how to load the training set and retrieve corresponding labels for each image.
The file 'example_robot_shell.py' simulates a shell to interface with the r12/5 butterfly robotics arm. Within
the example shell it is shown how to send commands to the arm for autonomous control.