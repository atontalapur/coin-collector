from game import Game
import arcade

def main():
    """Main function"""
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
