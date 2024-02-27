import commands2
import wpilib

import subsystems
from constants import FiringSpeed


class ShootAmp(commands2.Command):
    """
    Shoots the note

    :param Shooter shooter: The shooter to execute the command on
    :param FiringSpeed firing_speed: Enum of either AMP or SPEAKER firing speeds
    """

    def __init__(self, shooter: subsystems.Shooter, servos: subsystems.Servos):
        super().__init__()
        self.shooter = shooter
        self.shooter.set_firing_speed(FiringSpeed.AMP)
        self.servos = servos
        self.timer = wpilib.Timer()
        self.addRequirements(shooter, servos)

    def initialize(self) -> None:
        self.shooter.swivel()
        
        self.timer.restart()
    
    def execute(self) -> None:
        if self.timer.get() > 2:
            self.shooter.shoot_speed(FiringSpeed.AMP.value)
        if self.timer.get() > 3.5:
            self.servos.up()
    
    def end(self, interrupted: bool) -> None:
        self.shooter.swivel()
        self.servos.down()
        self.shooter.stop()

    def isFinished(self) -> bool:
        return self.timer.get() > 5