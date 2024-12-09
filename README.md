[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6x3sVpPb)
# CP1404 Assignment 2: Travel Tracker 2.0 by Zhao Changlin

_Edit this README, replacing this line and above with your own name/details._  
_At the end of the project, complete the project reflection below by answering the questions (replace the ... parts)._
_Note that to get high marks for this, your reflection should match the "exemplary" description from the rubric:_

> The project reflection is complete and describes development and learning well, shows careful thought, highlights insights made during code development.


## 1. How long did the entire project (assignment 2) take you?
I spent approximately 19 hours on this project. I started working on this on Wednesday, September 20th. 
I finished the coding on Sunday, September 24th. I spent 4.5 hours reading assignment descriptions, reviewing lecture videos and Kivy demos.
I spent around 14.5 hours on coding.

Note: You may like to use the WakaTime plugin, which tracks exactly how long you spend in code. See http://wakatime.com (but note that the free version only has a 7-day history)

## 2. What are you most satisfied with?
For this assignment, the most satisfying experience would be reviewing and refining my code. I constantly keep reminding myself that I should not repeat my code and follow Single Responsibility Principle when designing functions and methods.
I did make many changes and improvements during the process. This assignment deepened my understanding of how to design functions and methods effectively. Upon completion, the sense of accomplishment made me feel that my effort invested was well worth it.

## 3. What are you least satisfied with?
The gap between learning the Kivy library and applying it in the project was a challenge. I believe we could use more lectures and live demos on Kivy. I would suggest one more week's lecture on the topic of GUI. Also, it would be best if the Kivy content was covered in week 10 such that we could start Assignment 2 immediately before we started forgetting about what we learned.
I also hold different opinions on the naming within the given code, such as the sort() method given in test_placecollection.py. Because we were instructed not to change the given testing code. That left us no options but to follow the method naming given in the test file.
The sort() method, albeit defined inside the PlaceCollection class, could still cause unnecessary confusions.
## 4. What worked well in your development process?
The Place class, PlaceCollection class and the rewritten console program went really smooth. They were quite straightforward. The application of classes really made a difference.
Creating the Place and PlaceCollection classes as the first step laid solid foundations for the rest of the project.

## 5. What about your process could be improved the next time you do a project like this?
I believe there are definitely aspects to be improved. I would spend more time on planning the structure of my code in my future project. A clear blueprint of the program structure can save coding time by reducing the need for major overhauls later. I found myself struggling from time to time for a lack of clear structure when I tried to start coding for the Kivy program. Because the console program was not much different from Assignment 1, I underestimated the difficulty of the GUI program and started right away after I finished the console program.
I found myself without a clue where and how to start my GUI program, so I had to stop and start reviewing lectures and Kivy demos to become fully equipped for the program.

## 6. Describe what learning resources you used and how you used them.
I reviewed the Kivy lecture videos, all six of them, twice. I read and tested the Kivy demos countless times. Among them, I spent the most time on the board game project, the spinner demo, and the popup demo.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.
The first challenge I faced was that I was not sure if the console program was somehow connected to the GUI program. I thought they could be connected, but then I really had no clue how they could be connected. Eventually after reading the assignment description for the fourth time plus some reflecting, I came to understand that they are two separate programs.

The second challenge I met was about the implementations of methods/functions. There were functions that were exclusively used by the console program, and others exclusively used by the GUI program. Because of this, I was reluctant about where to actually implement those methods. I could either put them inside the class, or the main program. I asked senior students and some friends with coding experience about their own opinions on this style related issue. I also conducted online research about conventions about this.
Eventually I decided to put those methods which would be used by both console and GUI programs inside the class, while leaving those exclusive functions inside respective programs.

The third challenge was the Kivy program as a whole. As I mentioned above, Kivy was covered back in week 8. After two weeks, we have already started to forget about the exact contents. I had to spend a considerable time to pick them up again. Fortunately I did manage to grasp the majority of the concepts and ideas and collected hands-on experience after multiple reviews and test runs.


## 8. Briefly describe your experience using classes and if/how they improved your code.
The usage of classes was an eye-opening experience. They totally demonstrated the power of modularity and how it could turn abstract terms into simple objects that are easy to understand through encapsulating related data and behaviors into single objects and inheritance. I realized that using classes leads to more organized, reusable, and scalable code, which is easier to understand and debug. My code definitely became more succinct and organized after using classes.
I am now able to tackle problems on a higher-level logic.