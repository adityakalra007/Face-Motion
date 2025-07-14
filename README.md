# Introduction
This project demonstrates an innovative game that utilizes real-time facial tracking to control the movement of a paddle. By detecting head rotations (left and right), the player can move the paddle horizontally on the screen to bounce a ball. The game’s primary objective is to prevent the ball from falling off the screen by keeping it within the boundaries of the paddle.


The game leverages MediaPipe to detect facial landmarks, particularly the positions of the eyes, and calculates the head rotation angle to control the paddle's movement. This adds a unique hands-free interaction to the traditional paddle-and-ball game mechanics.


By using Python and the libraries OpenCV, MediaPipe, and Pygame, the project integrates computer vision with game development to create an intuitive, interactive game controlled by head movements.

# OutPut
![Demo Screenshot](/image.png)  

# Objectives

•	Head Movement Control: 
Develop a game that enables the player to control the paddle's movement using head tilt (left and right).

•	Real-Time Interaction: 
Create a seamless real-time game where the player’s face and head movements directly impact the game behavior.

•	User-Friendly Gameplay: 
Allow the player to interact with the game using natural, physical head motions to enhance accessibility and create an immersive experience.

•	Game Features: 
Incorporate lives and scores to provide an engaging challenge with dynamic difficulty (e.g., speed changes as the player progresses).

# Tools & Technologies Used

Tool/Library	
Purpose
Python 	The programming language used for implementing game logic and integrating libraries.
OpenCV	Handles real-time video capture from the webcam and ball-paddle interaction in the game.
MediaPipe	Used to detect facial landmarks in real-time to calculate the player’s head tilt for controlling the paddle.
Pygame	Provides game development tools for rendering the game window, managing user inputs, and handling graphics.

# Project Modules
## Module Description
main.py	Contains the main game loop, logic for controlling the paddle and ball, detecting collisions, scoring, and managing lives.
face_tracker.py	Contains functions to process webcam frames, detect the face using MediaPipe, and calculate head rotation angles based on eye positions.

# Game Features
The face-controlled paddle game incorporates the following features:
1.	Face-Controlled Paddle Movement:
    The paddle’s horizontal movement is controlled by the player's head rotation. As the player moves their head left, the paddle moves left; as they move their head right, the paddle moves right.
2.	Real-Time Ball Movement:
    The ball is rendered with an initial speed and direction. The player’s goal is to keep the ball bouncing by moving the paddle to hit the ball. Missing the ball causes the player to lose a life.
3.	Lives System:
	The game starts with 3 lives. Each time the player misses the ball (when it falls off the screen), a life is lost. The game ends when all lives are lost.
4.	Score System:
	The score increases each time the ball successfully hits the paddle. The score is displayed in the top-left corner of the screen and is updated continuously.
5.	Game Over:
	Once all the lives are lost, the game transitions to a Game Over screen where the player can view their final score. The player can then restart the game or exit. 
    
# How It Works?
The game integrates two key technologies for real-time interaction:
1.	Webcam Capture:
	The webcam captures video frames in real-time using OpenCV. These frames are then passed to MediaPipe for facial detection.
2.	Facial Landmark Detection:
	MediaPipe detects the position of the eyes in the video frame. By calculating the horizontal distance between the left and right eye landmarks, we determine the angle of the head rotation (left or right).
3.	Head Movement to Paddle Control:
	The paddle’s horizontal position is updated based on the head rotation angle. A positive angle (right tilt) moves the paddle to the right, while a negative angle (left tilt) moves it left.
4.	Ball Physics:
	The ball moves autonomously across the screen, and its position is updated in each frame. The ball bounces off the paddle, walls, and screen boundaries. The game checks for ball collisions and updates the game state accordingly.
5.	Score and Life Tracking:
	Each time the ball hits the paddle, the score increases by 1. If the ball is missed, the number of lives decreases. The game ends when all lives are lost, and the final score is displayed.

# Game Flow
1.	Initialization:
	The game window opens, and the webcam captures video frames.
	MediaPipe starts detecting facial landmarks, focusing on the eye positions to calculate the head tilt.
	The paddle is displayed at the bottom of the screen, and the ball starts falling.

2.	Frame Processing:
	Every frame captured from the webcam is processed using OpenCV.
	Face landmarks are detected and processed to calculate the head rotation angle.

3.	Paddle Movement:
	The horizontal movement of the paddle is adjusted based on the head rotation angle. The movement is responsive, meaning even slight head movements will influence the paddle.
4.	Ball Movement & Collision:
	The ball’s trajectory is updated. It moves towards the bottom of the screen and bounces off the walls and paddle.
	When the ball misses the paddle, the player loses a life, and the ball resets at the top of the screen.

5.	Game Over:
	If all lives are lost, a Game Over screen is displayed showing the player’s final score.













________________________________________Results

•	The project successfully implements a face-controlled paddle movement system using real-time MediaPipe facial tracking.
•	Lives and score systems were integrated to enhance the user experience.
•	The game ends when all lives are lost, and the final score is displayed, contributing to a complete game loop.




This project successfully demonstrates the application of computer vision to create a hands-free gaming experience. By controlling the game via head movement, it opens doors for creating more accessible games for individuals with mobility impairments. Future improvements could include gesture-based controls, more complex game mechanics, and customizable player interactions.

The project also provides an example of integrating Python, OpenCV, MediaPipe, and Pygame to create interactive multimedia applications.
________________________________________

________________________________________Folder Structure

📁 face_game/
 ├── main.py           ← Game logic, game loop, collision detection, paddle control
 └── face_tracker.py   ← Facial landmark detection and head angle calculation
________________________________________

Installation & Setup

1.	Install Dependencies:
pip install opencv-python mediapipe pygame

2.	Run the Game:
python main.py
________________________________________
References:
•	MediaPipe: https://google.github.io/mediapipe/
•	OpenCV Documentation: https://opencv.org/
•	Pygame Documentation: https://www.pygame.org/docs/
