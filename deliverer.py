from robot_abc import RobotABC
import time


class Deliverer(RobotABC):
    def perform_task(self) -> bool:
        if self.battery <= 5:
            print("Insufficient battery to perform task.")
            return False

        print("Delivering delivery", end="")
        for x in range(5):
            time.sleep(1.2)
            print(".", end="")
        print()
        time.sleep(1.2)
        print("Delivery complete.")
        self.take_damage()
        self.battery -= 5
        self.condition -= 10

        if self.condition <= 0:
            self.scrap()
        return True

    def status(self) -> bool:
        print(f"Current battery level: {self.battery}"
              f"Current condition: {self.condition}"
              f"Performed task(s): {self.perform_task()}")
        return True
