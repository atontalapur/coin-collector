 > As you complete each section you **must** remove the prompt text. Every *turnin* of this project includes points for formatting of this README so keep it clean and keep it up to date. 
 > Prompt text is any lines beginning with "\>"
 > Replace anything between \<...\> with your project specifics and remove angle brackets. For example, you need to name your project and replace the header right below this line with that title (no angle brackets).

# Catch the Coins

 > Authors: Andrew Maciborski [(GitHub)](https://github.com/dpxa), Advaith Tontalpur [(GitHub)](https://github.com/atontalapur), Arjun M [(GitHub)](https://github.com/Valientkyton), Ritul Roshan Ravindran [(GitHub)](https://github.com/Vishifishi)

Catch The Coins will consist of a greedy person and an environment full of bouncing coins. The user will control the person, and their goal is to collect as many coins as possible within the level’s time limit. There will be obstacles like walls and traps that slow the player down. There will also be special coins that are deducted from the number of coins collected.

There will be X number of levels, and the only thing that will change between runs of a level will be the random coin movement.

There will be a leaderboard for each level, and it will consist of the top X times of the user. The game will be able to be signed into through a login screen only asking for the profile name.

There will be functionality to exit a level, pause/resume a level, mute sound, and other appropriate controls for the effects added.

This project is important due to its full-stack approach to building a functional video game that parallels many key features in modern video games. Building this project would help build valuable skills in frontend, and back development and implement software design structures that we have learned so far.  While this can be challenging, it makes it that much more interesting due to the fact that none of us have experience building something of this exact nature, so it will push us to be more creative. It will also give us the opportunity to work on technologies/frameworks that we may not have used before which would also help us become a better developer.

Input: There will be a “user login” page where the user can enter their username. This will open the game and take them to a specified game level, or the level they left with.
The details entered will be cross-referenced with the database to retrieve the level information for the output. If they are a “pro” (finished all the levels), they will be prompted to choose a level they would like to play on another page. Based on this selection, a level will be launched.

Output: Based on the input parameters, and the information that was pulled from the database, a pop-up window will take the user to the level that they left the game, or the level they specify. On the GUI window, we will have the game, a high score for the user, an overall high score, current points, a timer to indicate the time they have left to complete the current level, and the number of tries they have taken. After the game, all of the information received will be displayed, and the leaderboard will also be displayed. After they finish the game, the new data will be entered into the database.

Languages
Python -Used for creating the game itself
SQL - Used for querying and storing user data in the database.

Tools
Python Arcade - The Python library used to code the core game mechanics.
Pytest - Python module for writing unit tests.

Technologies
Git - Used as a version control system for the project.
Pip - Used for installing and managing the project dependencies.
SQLite - A mobile version of MySQL which is used to store the user information.

We are still exploring options to host the game online.

## User Interface Specification
### Navigation Diagram
![Navigation Diagram](assets/nav_diag.png)

The navigation diagram illustrates the flow of a user interface for a login and game system. Here’s the breakdown:

1. **Login/Logout**: The central point where users can log in or log out. If user information is not found, a pop-up window appears.

2. **User Found**: If the user is verified, they are directed to their profile.

3. **New Player Registration**: If the user is new, they go through a registration process to create a profile.

4. **Profile Actions**: After login, users can:
   - Select a level to begin the game.
   - Exit and save their progress.

5. **Game Flow**: 
   - *Start Game*: Once a level is selected, the game begins.
   - *Rules*: Users can view the game rules before starting.

6. **Game Outcomes**: After playing, users can either win or lose.
   - *Win*: Winning a game may allow selecting the next level.
   - *Lost*: If the user loses, they can choose to restart.

7. **Exit Options**: At any stage, users can exit and save their progress.

### Screen Layouts
![Screen Diagram](assets/screen_diag1.jpg)

![Screen Diagram](assets/screen_diag2.jpg)

## Class Diagram
![Class Diagram](assets/class_diag.jpg)

On login, a game object will be created. The game object will contain everything that the user will see in the game. It has a level object, which is the current level. The level has its own unique environment as well as leaderboard, which is aggregated. The environment controls the player and all of the obstacles and coins that are in that level. The game object will own everything except the leaderboard, as the leaderboard can exist on its own. On login, a username will be fetched/created and a databaseManager object will be created, and these will ensure the leaderboards will stay updated as well as the user's new high scores can be seen on the leaderboard.

Updated Class Diagram (SOLID):
1. Moves Player to be composed in Environment, instead of Game. The game class should not be controlling the core functions of the game as well as updating where the player is drawn. That is the purpose of Game.level.environment. This was fixing a mistake, not an improvement. Now everything that is drawn as part of a level is next to each other. It makes it easier to ensure that everything is updated properly. This violated the Single Responsibility Principle.

Why Whole Class Diagram Adheres to SOLID:
1. SRP - each object has a specific purpose. Coin/Obstacle/Player represents the displayed player, environment is responsible for updating their interactions, leaderboard displays that leaderboard and owns a connection to the database, as it is the only object using the database. level consists of the environment being drawn and the high score leaderboard for it. Game represents the functions that any method should have, such as pausing, muting, and showing current time and coins left.
2. OCP - A dictionary of settings for each level is used so that many of the feature the levels share is generalized outside of where the levels are built. This allows for the customization of how the coins/player act without having to write elif statement for each level. Right now, the _setup_walls() method does not follow OCD, as it used elif, but a fix is being developed.
3. LSP - Not relevant. No superclasses/subclasses developed.
4. ISP - No classes implementing interfaces.
5. DIP - No classes depending on low level modules.

 ## Changes (12/6)
 > Get rid of leaderboard class, as it is not necessary. The Database class will provide all of the scores as a list of tuples, and they just need to be parsed in the appropriate window. 
 
 ## Screenshots
 > Screenshots of the input/output after running your application **********************************************

 ## Installation/Usage
 > In order to run Catch the Coins, run git clone https://github.com/cs100/final-project-the-best-team. Make sure the folder "final-project-the-best-team" is empty in the directory you are cloning to.
 > Then, run pip install arcade to have the necessary libraries to run the game. It is best to use a virtual environment rather than installing the libraries globally, but installing them this way is the easiest.
 > Then, run python src/main.py to begin the game. Have fun!

 ## Testing
 > We used pytest to test out source code, unit test for the game and database are complete, and tests for interface navigation are underway. Estimated 60-70% method coverage.
 
