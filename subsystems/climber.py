import commands2
import rev

from constants import CLIMBING_MOTOR_SPEED, MOTOR_TYPE


class Climber(commands2.Subsystem):
    def __init__(self, CAN_ID: int) -> None:
        super().__init__()
        self.motor = rev.CANSparkMax(CAN_ID, MOTOR_TYPE)
    
    def climb(self):
        self.motor.set(CLIMBING_MOTOR_SPEED)
