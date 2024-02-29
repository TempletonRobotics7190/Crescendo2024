from wpilib import Timer
import subsystems
import commands2
from constants import DRIVING_MOTOR_SPEED, SIDEWAYS_MOTOR_SPEED, TURNING_MOTOR_SPEED


class ShootAmp(commands2.Command):
    """
    Shoots the note

    :param Shooter shooter: The shooter to execute the command on
    :param FiringSpeed firing_speed: Enum of either AMP or SPEAKER firing speeds
    """

    def __init__(self, drive: subsystems.Drive):
        super().__init__()
        self.drive = drive
        self.timer = Timer()
        self.addRequirements(drive)

    def initialize(self) -> None:
        self.timer.reset()
    
    def execute(self) -> None:
        if self.timer.get() < 3:
            self.drive.move(DRIVING_MOTOR_SPEED, SIDEWAYS_MOTOR_SPEED, TURNING_MOTOR_SPEED)
    
    def end(self, interrupted: bool) -> None:
        self.timer.stop()

    def isFinished(self) -> bool:
        return self.timer.get() > 3