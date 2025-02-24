# Robot Factory Program

---

The Robot Factory Simulator is a Python program that allows users to create and manage different types
of robots. Users can perform tasks, track robot battery levels and condition, recharge
or repair robots, and scrap them when necessary. 

---

## Functions
 
---

1. **Create Different Types of Robots**: Chauffeur, Cooker, Deliverer, Dishwasher, 
Cleaner. The program will store them automatically. Numbers of robots is capped at 5.
2. **Access and use a robot**: Perform the following functions:
   - **Perform Tasks**: Each robot has a unique function that consumes battery and/or 
   affects its condition.
   - **Show Status**: Show a certain robot's status: battery, condition and tasks performed
   - **Recharge**: Recharge a robot's battery.
   - **Repair**: Repair a robot, improving condition by 30%
3. **View all robots**: View all active robots.
4. **Scrap a robot**: Permanently delete a robot if necessary.
5. **Exit**: Exit the program gracefully.

---

## Code Structure

---

This program is made up of these files:
```
|- robot_abc.py: Abstract Base Class for robots
|- chauffeur.py: Class for chauffeur (robot type)
|- cooker.py: Class for cooker
|- deliverer.py: Class for deliverer 
|- dishwasher.py: Class for dishwasher
|- interface.py: Class that handles user interaction with the program
|- main.py: The program is to be run here.
```

---

## Credits
- Joshua Niam: [JoshuaGibNiam](https://github.com/JoshuaGibNiam)

---

Monday, 24th of February 2025, 5:39 p.m.