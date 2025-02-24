from chaffeur import *
from cleaner import *
from cooker import *
from deliverer import *
from dishwasher import *
from robot_abc import *

class Interface:
    def display_main_menu(self):
        print("Welcome to the main menu!")
        print("Enter number to choose your next action:\n"
              "1. Create a Robot\n"
              "2. View All Robots\n"
              "3. Access a robot \n"
              "4. Scrap a robot \n"
              "5. Exit")
    def handle_main_menu(self):
        """Handle main menu actions"""
        action = input("What would you like to do?(1-5): ")
        while action not in ["1", "2", "3", "4", "5"]:
            action = input("Invalid input. What would you like to do?(1-4): ")
        action = int(action)

        if action == 1:
            """Create a robot, check if the user has reached their limit"""
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
            count = 0
            for bot in RobotABC.robots:
                if bot != None:
                    if robot == 1:
                        RobotABC.robots[bot] = Chauffeur()
                        break
                    elif robot == 2:
                        RobotABC.robots[bot] = Cooker()
                        break
                    elif robot == 3:
                        RobotABC.robots[bot] = Deliverer()
                        break
                    elif robot == 4:
                        RobotABC.robots[bot] = Dishwasher()
                        break
                    elif robot == 5:
                        RobotABC.robots[bot] = Cleaner()
                        break
                    else:
                        count += 1
            if count == 5:
                print("Maximum amount of robots reached. Scrap one to create a new one!")
            else:
                print("Robot successfully created!")

        elif action == 2:
            """Prints all available robots"""
            for k, v in RobotABC.robots.items():
                print(f"{k}: {v.__class__.__name__ if v.__class__.__name__ != "NoneType" else 'Void'}")

        elif action == 3:
            pass

if __name__ == "__main__":
    i = Interface()
    i.display_main_menu()
    i.handle_main_menu()
    i.handle_main_menu()


