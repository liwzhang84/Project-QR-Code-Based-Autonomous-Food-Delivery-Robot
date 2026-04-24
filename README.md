# QR Code-Based Autonomous Food Delivery Robot

## Team Members

- Liwen Zhang — lzhang84@buffalo.edu
- Kyudong Kim — kyudongk@buffalo.edu

## Project Objective

The goal of this project is to develop an autonomous food delivery robot for restaurants. The robot is designed to deliver food accurately to customers’ tables. Each table has a unique ArUco code. After receiving a predefined target ID, the robot moves to the corresponding table, stops there for 15 seconds, and then returns to the starting position.

## Contributions

By developing this system, we aim to show a simple and reliable approach for accurate table-level delivery. This project also gives us a way to test the system in simulation before applying it to a real robot, since the simulated model is intended to stay close to the physical setup.

## Current Progress

- Built the basic restaurant environment in Gazebo
- Verified that the scene can be displayed correctly
- Enabled basic car movement through another terminal interface
- Set up the main simulation framework for the delivery robot
- Started updating the car movement control code
- Began integrating the controller with the code used in class
- Defined the current workflow:
  - user enters a predefined ID
  - the robot identifies the corresponding ArUco code location
  - the robot moves to the assigned table
  - the robot stops for 15 seconds
  - the robot returns to the starting position

## Project Plan

The next step is to continue modifying the car movement control code and combine it with the code used in class so that the robot can follow the yellow line in the restaurant environment. After that, we will complete the full delivery sequence, including target ID input, ArUco target mapping, stopping at the correct table, and returning to the home position.

We will continue testing the full process in simulation before moving on to more complete system testing.

## Milestones / Schedule Checklist

- Complete this proposal document — Due March 31
- Capture the specifications of the physical robot — LZ, April 4
- Build the basic restaurant environment in Gazebo — KK, Completed
- Enable basic car movement through another terminal interface — LZ, Completed
- Modify the car movement control code — LZ, In progress
- Integrate the controller with the in-class code for yellow-line following — KK, In progress
- Implement predefined ID input and ArUco target mapping — LZ, In progress
- Make the robot stop at the assigned table for 15 seconds and return to the starting position — KK, In progress
- Create progress report and update README — In progress
- Integrate all components and perform system testing — Next step

## Measures of Success

- The restaurant environment is successfully displayed in Gazebo
- The robot responds correctly to control commands
- The robot can follow the yellow line in the simulation environment
- The robot can move to the correct table based on a predefined ID
- The robot stops at the assigned table for 15 seconds and then returns to the starting position
- A classmate can follow the README instructions and run the simulation independently without assistance

## Notes

At this stage, the environment and basic control are mostly ready. The current focus is on finishing the car movement logic, yellow-line following, target ID recognition, stopping at the table, and return-to-home behavior.
