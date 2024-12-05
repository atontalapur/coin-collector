import arcade
from globals.controller import Controller
from globals.database import LeaderboardDB

import globals.controller_manager as controller_manager
import globals.database_manager as database_manager
    
if __name__ == "__main__":
    database_manager.database = LeaderboardDB()
    controller_manager.controller = Controller()
    
    arcade.run()