from robot_abc import RobotABC
import time


class Chauffeur(RobotABC):
    def perform_task(self) -> bool:
        if self.battery <= 5:
            print("Insufficient battery to perform task.")
            return False
        destination = input("Where would you like to go to?: ")
        print(f"Driving to {destination}", end="")
        for x in range(5):
            time.sleep(1.2)
            print(".", end="")
        print()
        time.sleep(1.2)
        print("You have reached your destination.")
        self.take_damage()
        self.battery -= 5
        self.condition -= 10

        if self.condition <= 0:
            self.scrap()
        self.performed_tasks += 1
        return True

    def status(self) -> bool:
        print(f"Current battery level: {self.battery}\n"
              f"Current condition: {self.condition}\n"
              f"Performed task(s): {self.performed_tasks}")
        return True
