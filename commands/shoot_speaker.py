import commands2
import wpilib

import subsystems
from constants import FiringSpeed


class ShootSpeaker(commands2.Command):
    """
    Shoots the note

    :param Shooter shooter: The shooter to execute the command on
    :param FiringSpeed firing_speed: Enum of either AMP or SPEAKER firing speeds
    """

    def __init__(self, shooter: subsystems.Shooter, servos: subsystems.Servos):
        super().__init__()
        self.shooter = shooter
        self.shooter.set_firing_speed(FiringSpeed.SPEAKER)
        self.servos = servos
        self.timer = wpilib.Timer()
        self.addRequirements(shooter, servos)

    def initialize(self) -> None:     
        self.timer.restart()
    
    def execute(self) -> None:
        self.shooter.shoot_speed(FiringSpeed.SPEAKER.value)
        if self.timer.get() > 1:
            self.servos.up()
    
    def end(self, interrupted: bool) -> None:
        self.servos.down()
        self.shooter.stop()

    def isFinished(self) -> bool:
        return self.timer.get() > 2