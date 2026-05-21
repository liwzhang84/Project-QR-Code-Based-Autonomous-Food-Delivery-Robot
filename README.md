# QR Code Based Autonomous Restaurant Delivery Robot

## Project Description

This project presents a QR-code-based autonomous restaurant delivery robot simulation using Gazebo. The goal of this project is to create a simple restaurant environment where a small Ackermann robot can move through the center aisle and stop at a selected QR code station.

The simulated restaurant contains four tables arranged symmetrically on both sides of the aisle. QR code boards are placed near the tables and close to the robot's driving path so that they can be easily detected by the robot camera in future development. The robot also includes a food delivery tray to represent a restaurant delivery service.

At the current stage, the robot follows a predefined straight path. After the user enters a target QR code ID, the robot moves forward toward the corresponding station, stops for five seconds, and then moves backward toward the starting point.

## Motivation

Autonomous delivery robots are becoming increasingly useful in indoor environments such as restaurants, hotels, hospitals, and office buildings. In a restaurant setting, a robot can help deliver food to different tables and reduce repetitive work for staff.

This project focuses on a simplified restaurant delivery task. Instead of building a complex navigation system at the beginning, the robot is designed to move along a straight center aisle. QR code stations are used to represent different table locations. This makes the project easier to test and provides a foundation for future QR-code-based localization and task assignment.

## Simulation Environment

The Gazebo world is designed as a small restaurant. The environment includes restaurant walls, floor, tables, chairs, wall decorations, bright lights, QR code boards, and a delivery robot.

The four tables are placed symmetrically on the left and right sides of the restaurant. The middle area is kept clear as the driving path for the robot. QR code boards are placed beside the tables near the center aisle, which allows the robot to approach each station without turning.

The robot starts at one end of the aisle. It only performs forward and backward movement in the current version.

## Robot Behavior

The robot delivery task works as follows:

1. The user enters a target QR code ID.
2. The robot moves forward along the center aisle.
3. The robot stops near the selected QR code station.
4. The robot waits for five seconds to simulate food delivery or order confirmation.
5. The robot moves backward toward the starting position.
6. The robot stops after returning.

The current version uses timing-based control. Each QR code ID is assigned a predefined forward driving time. By adjusting these timing values, the robot can be tuned to stop near the corresponding QR code board.

## Main Features

- Restaurant-style Gazebo simulation world
- Four symmetric table layout
- Clear center aisle for robot movement
- QR code boards placed near table locations
- Bright lighting for better visual clarity
- Wall decorations to make the environment look like a restaurant
- Ackermann robot car model
- Food delivery tray mounted on the robot
- Forward and backward robot movement
- Timing-based stop behavior for different QR code stations

## File Organization

The project files should be placed inside the existing `gazebo_demo` folder.

The world file should be placed in the `worlds` folder.

The QR code marker models and the updated Ackermann car model should be placed in the `models` folder.

The control script should be placed directly inside the `gazebo_demo` folder.

The expected project structure is:

    gazebo_demo/
    ├── models/
    │   ├── ackermann_car/
    │   ├── restaurant_qr_marker_01/
    │   ├── restaurant_qr_marker_02/
    │   ├── restaurant_qr_marker_03/
    │   ├── restaurant_qr_marker_04/
    │   ├── restaurant_qr_marker_05/
    │   └── restaurant_qr_marker_06/
    ├── worlds/
    │   └── restaurant_qr_activity_v3.world
    └── qr_delivery_simple.py

## Setup Instructions

First, copy the restaurant world file into the `worlds` folder.

Then, copy all restaurant QR marker model folders into the `models` folder.

The original `ackermann_car` folder should be replaced by the updated `ackermann_car` folder provided in this project. The updated robot model includes the delivery tray.

After all files are added, make sure the Gazebo resource path includes both the `models` and `worlds` folders.

## Running the Simulation

This project should be run with three terminals.

### Terminal 1: Start the Gazebo Server

    cd /path/to/gazebo_demo
    export GZ_SIM_RESOURCE_PATH=$PWD/models:$PWD/worlds
    gz sim -s worlds/restaurant_qr_activity_v3.world -v 4

### Terminal 2: Start the Gazebo GUI

    cd /path/to/gazebo_demo
    export GZ_SIM_RESOURCE_PATH=$PWD/models:$PWD/worlds
    gz sim -g

### Terminal 3: Run the Robot Control Script

    cd /path/to/gazebo_demo
    python qr_delivery_simple.py

The program will ask the user to enter a target QR code ID. After the ID is entered, the robot will move to the corresponding station, stop for five seconds, and return.

## Control Method

The current control method is based on predefined travel time. Each QR code ID corresponds to a forward movement time.

If the robot stops too early, the travel time for that QR code ID should be increased.

If the robot moves too far, the travel time should be decreased.

If the robot moves too fast or becomes unstable, the speed value in the control script should be reduced.

This method is simple but useful for demonstrating the basic delivery task in the restaurant environment.

## Adjustable Parameters

The main adjustable parameters are in `qr_delivery_simple.py`.

The robot speed can be adjusted by changing the value of `SPEED`.

If the robot flips over or moves too fast, reduce the speed.

The stopping position for each QR code can be adjusted by changing the values in `ID_TO_FORWARD_TIME`.

If the robot stops too early, increase the corresponding time.

If the robot moves too far, decrease the corresponding time.

## Current Limitations

The current version does not yet use real-time QR code recognition. The robot does not automatically detect the QR code ID from the camera image. Instead, the user inputs the target ID, and the robot moves based on a predefined timing table.

The robot also does not perform path planning or turning. It only moves forward and backward along the center aisle.

Because the motion is timing-based, the stopping position may need manual tuning for different computers, simulation speeds, or model settings.

## Future Work

Future improvements may include real-time QR code or ArUco marker detection using the robot camera. Once the robot can detect QR code IDs automatically, it can stop based on visual recognition instead of predefined travel time.

Other possible improvements include odometry-based return control, smoother speed control, obstacle avoidance, PID control, and more realistic restaurant furniture and decorations.

In the future, the robot can also be extended to support multiple delivery tasks, different table locations, and more complex indoor navigation.

## Conclusion

This project demonstrates a simple QR-code-based restaurant delivery robot simulation in Gazebo. The robot moves through a restaurant aisle, stops near a selected QR code station, waits to simulate delivery, and returns to the starting point.

Although the current version uses a timing-based control method, this project provides a foundation for future camera-based QR code recognition and autonomous indoor delivery behavior.
