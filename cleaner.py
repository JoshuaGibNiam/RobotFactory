from robot_abc import RobotABC
import time


class Cleaner(RobotABC):
    def perform_task(self) -> bool:
        if self.battery <= 10:
            print("Insufficient battery.")
            return False

        print("Cleaning Room", end="")
        for x in range(5):
            time.sleep(1)
            print(".", end="")
        print("\n")
        time.sleep(1)
        self.take_damage()
        print("Cleaning Completed!")
        self.battery -= 10
        self.condition -= 5

        if self.condition <= 0:
            # Scraps robot if condition is beyond repair
            self.scrap()
        self.performed_tasks += 1
        return True

    def status(self) -> bool:
        print(f"Battery Level: {self.battery}\n"
              f"Condition: {self.condition}"
              f"Performed task(s): {self.performed_tasks}")
        return True


if __name__ == "__main__":
    cleaner = Cleaner()
    cleaner.perform_task()
    cleaner.status()
    cleaner.recharge()