import commands2
import rev

from constants import MOTOR_TYPE, CLIMBING_MOTOR_SPEED

class RightClimber(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.motor = rev.CANSparkMax(11, MOTOR_TYPE)
    
    def climb(self):
        self.motor.set(CLIMBING_MOTOR_SPEED)