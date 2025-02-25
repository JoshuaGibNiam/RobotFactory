from chauffeur import *
from cleaner import *
from cooker import *
from deliverer import *
from dishwasher import *
from robot_abc import *
import os
import json
class Interface:
    def __init__(self):
      pass

    # Mapping of robot types to their classes
    ROBOT_CLASSES = {"Chauffeur": Chauffeur,
                     "Cleaner": Cleaner,
                     "Cooker": Cooker,
                     "Deliverer": Deliverer,
                     "Dishwasher": Dishwasher}

    def load(self):
        path = "robots.json"
        if os.path.exists(path):
            with open(path, "r") as file:
                RobotABC.robots = json.load(file)
                for k, v in RobotABC.robots.items():
                    if RobotABC.robots[k]:
                        RobotABC.robots[k] = Interface.ROBOT_CLASSES[v["type"]](v["battery"], v["condition"],
                                                                            v["performed_tasks"])

        else:
            with open(path, "w") as file:
                print("Initializing file...")
                json.dump({}, file)

    def save(self):
        # convert robots into savable obj first
        for k, v in RobotABC.robots.items():
            if RobotABC.robots[k]:
                RobotABC.robots[k] = {"type": v.__class__.__name__, "battery": v._battery, "condition": v._condition,
                                  "performed_tasks": v.performed_tasks}
        path = "robots.json"

        with open(path, "w") as file:
            json.dump(RobotABC.robots, file)

    def display_main_menu(self) -> None:
        print("Welcome to the main menu!")
        print("Enter number to choose your next action:\n"
              "1. Create a Robot\n"
              "2. View All Robots\n"
              "3. Access a robot \n"
              "4. Scrap a robot \n"
              "5. Exit")
    def handle_main_menu(self) -> bool:
        """Handle main menu actions, returns True to all unless user wants to exit"""
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
            count = 5
            for bot in RobotABC.robots.keys():
                if RobotABC.robots[bot] is None:
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
                    count -= 1
            if count == 0:
                print("Maximum amount of robots reached. Scrap one to create a new one!")
            else:
                print("Robot successfully created!")
            return True
        elif action == 2:
            """Prints all available robots"""
            for k, v in RobotABC.robots.items():
                print(f"{k}: {v.__class__.__name__ if v.__class__.__name__ != "NoneType" else 'Void'}")
            return True
        elif action == 3:
            for k, v in RobotABC.robots.items():
                print(f"{k}: {v.__class__.__name__ if v.__class__.__name__ != "NoneType" else 'Void'}")
            input_robot = input("Which robot would you like to access?(1-5):")
            while input_robot not in ["1", "2", "3", "4", "5"]:
                input("Invalid input. What robot would you like to access?(1-5): ")
            input_robot = RobotABC.robots["Robot " + input_robot]
            if input_robot is None:
                print("Robot does not exists!")
                return True
            action = input("What would you like to do?:\n "
                           "1. Perform Task\n"
                           "2. Show Status\n"
                           "3. Recharge \n"
                           "4. Repair \n"
                           ": ")
            while action.strip() not in ["1", "2", "3", "4"]:
                action = input("Invalid input. What would you like to do?(1-2): ")

            if action.strip() == "1":
                input_robot.perform_task()
            elif action.strip() == "2":
                input_robot.status()
            elif action.strip() == "3":
                input_robot.recharge()
            elif action.strip() == "4":
                input_robot.repair()
            return True

        elif action == 4:
            for k, v in RobotABC.robots.items():
                print(f"{k}: {v.__class__.__name__ if v.__class__.__name__ != "NoneType" else "None"}")
            input_robot = input("Which robot would you like to scrap?(1-5):")
            while input_robot not in ["1", "2", "3", "4", "5"]:
                input("Invalid input. What robot would you like to scrap?(1-5): ")
            input_robot = RobotABC.robots["Robot " + input_robot]
            input_robot.scrap()
            return True

        else:
            print("Exiting Program...")
            self.save()
            return False


if __name__ == "__main__":

    i = Interface()
    i.load()
    i.handle_main_menu()
    i.handle_main_menu()
    i.save()



