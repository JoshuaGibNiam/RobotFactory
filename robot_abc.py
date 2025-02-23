from abc import ABC, abstractmethod
from random import randint


class RobotABC(ABC):
    robots = {"Cleaner": 0,
              "Deliverer": 0,
              "Dishwasher": 0,
              "Cooker": 0,
              "Chauffeur": 0}

    def __init__(self):
        self.battery = 100
        self.condition = 100
        self.performed_tasks = 0
        for k, v in self.__class__.robots.items():
            if self.__class__.__name__ == k:
                self.robots[k] += 1





    @abstractmethod
    def perform_task(self):
        """
        Ensures battery and condition is sufficient to perform task
        Returns True if task is performed, False otherwise
        """
        pass

    @abstractmethod
    def status(self):
        """Prints robot status: battery, performed tasks
         and condition and returns True"""
        pass

    @property
    def battery(self) -> int:
        return self.battery

    @battery.setter
    def battery(self, battery: int):
        if self.battery < 0:
            self.battery = 0
        elif self.battery > 100:
            self.battery = 100
        else:
            self.battery = battery

    @battery.deleter
    def battery(self):
        del self.battery

    @property
    def condition(self):
        return self.condition

    @condition.setter
    def condition(self, condition: int):
        if condition < 0:
            self.condition = 0
        elif condition > 100:
            self.condition = 100
        else:
            self.condition = condition

    @condition.deleter
    def condition(self):
        del self.condition

    def recharge(self):
        self.condition += 25

    def repair(self):
        self.condition += 30

    def scrap(self):
        print(f"{self.__class__.__name__} robot permanently scrapped.")
        del self.battery
        del self.condition
        self.__class__.robots[self.__class__.__name__] -= 1

    def take_damage(self):
        """Creates a slim chance where a robot will take damage.
        Condition will be affected. If condition < 0, robot will be scrapped"""
        chance = randint(1, 100)
        if chance < 5:
            print("The robot has taken damage from unknown external sources.")
            self.condition = -5
        if self.condition <= 0:
            self.scrap()

    def active_robots(self):
        print(f"Current active robots: {self.__class__.robots}")
