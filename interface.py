from chaffeur import *
from cleaner import *
from cooker import *
from deliverer import *
from dishwasher import *

class Interface:
    def display_main_menu(self):
        print("Welcome to the main menu!")
        print("Enter number to choose your next action:\n"
              "1. Create a Robot\n"
              "2. View All Robots\n"
              "3. Delete a Robot\n"
              "4. Exit")
    def handle_main_menu(self):
        """Handle main menu actions"""
        action = input("What would you like to do?(1-4): ")
        while action not in ["1", "2", "3", "4"]:
            action = input("Invalid input. What would you like to do?(1-4): ")
        action = int(action)

        if action == 1:
            print("Here are robot types: \n"
                  "1. Chauffeurs \n"
                  "2. Cookers \n"
                  "3. Deliverers \n"
                  "4. Dishwashers \n"
                  "5. Cleaners \n")
            robot = input("What robot would you like to create?(1-5): ")
            while robot not in ["1", "2", "3", "4", "5"]:
                robot = input("Invalid input. What robot would you like to create?(1-5): ")
            robot = int(robot)
            if robot == 1:
                pass
