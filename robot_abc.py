from abc import ABC, abstractmethod
from random import randint


class RobotABC(ABC):
    robots = {"Cleaner": 0,
              "Deliverer": 0,
              "Dishwasher": 0,
              "Cooker": 0,
              "Chauffeur": 0}
    robots_list = {}
    def __init__(self):
        self._battery = 100
        self._condition = 100
        self.performed_tasks = 0
        for k, v in self.__class__.robots.items():
            if self.__class__.__name__ == k:
                self.robots[k] += 1







    @abstractmethod
    def perform_task(self) -> bool:
        """
        Ensures battery and condition is sufficient to perform task
        Returns True if task is performed, False otherwise
        """
        pass

    @abstractmethod
    def status(self) -> bool:
        """Prints robot status: battery, performed tasks
         and condition and returns True"""
        pass

    @property
    def battery(self) -> int:
        return self._battery

    @battery.setter
    def battery(self, battery: int):
        if self._battery < 0:
            self._battery = 0
        elif self._battery > 100:
            self._battery = 100
        else:
            self._battery = battery

    @battery.deleter
    def battery(self):
        del self._battery

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, condition: int):
        if condition < 0:
            self._condition = 0
        elif condition > 100:
            self._condition = 100
        else:
            self._condition = condition

    @condition.deleter
    def condition(self):
        del self._condition

    def recharge(self) -> None:
        """Recharges itself at 25% battery per charge"""
        self.condition += 25
        print(f"Robot recharged to {self._battery}% battery.")

    def repair(self) -> None:
        """Repairs 30% of condition"""
        self.condition += 30
        print(f"Robot recharged to {self._condition}% condition.")

    def scrap(self) -> None:
        """Delete the robot permanetly"""
        print(f"{self.__class__.__name__} robot permanently scrapped.")
        del self.battery
        del self.condition
        self.__class__.robots[self.__class__.__name__] -= 1

    def take_damage(self) -> None:
        """Creates a slim chance where a robot will take damage.
        Condition will be affected. If condition < 0, robot will be scrapped"""
        chance = randint(1, 100)
        if chance < 5:
            print("The robot has taken damage from unknown external sources.")
            self.condition = -5
        if self.condition <= 0:
            self.scrap()

    def active_robots(self) -> None:
        """Prints all the active robots."""
        print(f"Current active robots: {self.__class__.robots}")
