import wpilib
import commands2
import subsystems
from constants import FiringSpeed

class Shoot(commands2.Command):
    """
    Shoots the note

    :param Shooter shooter: The shooter to execute the command on
    :param FiringSpeed firing_speed: Enum of either AMP or SPEAKER firing speeds
    """

    def __init__(self, shooter: subsystems.Shooter, servos: subsystems.Servos, firing_speed: FiringSpeed):
        super().__init__()
        self.shooter = shooter
        self.servos = servos
        self.firing_speed = firing_speed
        self.timer = wpilib.Timer()
        self.addRequirements(shooter, servos)

    def initialize(self) -> None:
        if self.firing_speed == FiringSpeed.AMP:
            self.shooter.swivel()
        
        self.timer.restart()
    
    def execute(self) -> None:
        if self.timer.get() > 2:
            self.shooter.shoot()
        if self.timer.get() > 3:
            self.servos.up()
    
    def end(self, interrupted: bool) -> None:
        if self.firing_speed == FiringSpeed.AMP:
            self.shooter.swivel()
        self.servos.down()

    def isFinished(self) -> bool:
        return self.timer.get() > 6