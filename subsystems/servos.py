import commands2
import wpilib


class Servos(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.left_servo = wpilib.Servo(0)
        self.right_servo = wpilib.Servo(1)
        self.down()
    
    def up(self):
        self.left_servo.set(0.25)
        self.right_servo.set(0.80)

    def down(self):
        self.left_servo.set(0.75)
        self.right_servo.set(0.30)