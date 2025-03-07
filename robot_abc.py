from abc import ABC, abstractmethod
from random import randint


class RobotABC(ABC):
    robots = {"Robot 1": None, "Robot 2": None, "Robot 3": None,
              "Robot 4": None, "Robot 5": None}

    def __init__(self, battery=100, condition=100, performed_tasks=0):
        self._battery = battery
        self._condition = condition
        self.performed_tasks = performed_tasks


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
        """Delete the robot permanently"""
        print(f"{self.__class__.__name__} robot permanently scrapped.")
        del self.battery
        del self.condition
        for k, v in self.robots.items():
            if v == self:
                self.robots[k] = None
                break


    def take_damage(self) -> None:
        """Creates a slim chance where a robot will take damage.
        Condition will be affected. If condition < 0, robot will be scrapped"""
        chance = randint(1, 100)
        if chance < 5:
            print("The robot has taken damage from unknown external sources.")
            self.condition = -5
        if self.condition <= 0:
            self.scrap()

