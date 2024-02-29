import commands2
import rev

from constants import CLIMBING_MOTOR_SPEED, MOTOR_TYPE


class Climber(commands2.Subsystem):
    def __init__(self, CAN_ID: int, reversed: bool = False) -> None:
        super().__init__()
        self.motor = rev.CANSparkMax(CAN_ID, MOTOR_TYPE)
        self.motor.setInverted(reversed)
    
    def climb_down(self):
        self.motor.set(CLIMBING_MOTOR_SPEED)

    def climb_up(self):
        self.motor.set(-CLIMBING_MOTOR_SPEED)

    def stop(self):
        self.motor.set(0)
