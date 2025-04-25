# DronePilot-AI

DronePilot-AI is a project developed as part of the Capstone 1 final for the drone capstone program. The goal of this project is to demonstrate basic drone control skills, including:

- Following hand signals.
- Tracking and following a person as an object.
- Responding to speech commands.

## Features

- **Hand Signal Recognition**: The drone can interpret specific hand gestures to perform corresponding actions.
- **Object Tracking**: The drone is capable of identifying and following a person as a target.
- **Speech Command Execution**: The drone responds to predefined voice commands for navigation and control.

## Requirements

- A compatible Ryze Tello drone .
- Python 3.9 or higher.
## Libraries

The following libraries are required to run the project:

- `djitellopy`: A Python library for controlling the Tello drone.
- `opencv-python`: For image processing and computer vision tasks.
- `numpy`: For numerical computations.
- `speech_recognition`: For processing and recognizing voice commands.
- `mediapipe`: For hand gesture recognition and tracking.

Make sure to install these libraries using `pip` before running the scripts.

## Usage

1. Ensure your Tello drone is powered on and connected to the internet.
2. Update the IP address in the script to match your Tello's IP.
3. Run the appropriate script that you are interested in:
    ```bash
    python script.py
    ```
4. Use hand signals, voice commands, or position yourself for object tracking to interact with the drone.

## Acknowledgments

This project was created as part of the Capstone 1 final for the drone capstone program. Special thanks to the instructor Steve Barry for his support throughout the duration of the class. 

## License

This project is licensed under the [MIT License](LICENSE).
