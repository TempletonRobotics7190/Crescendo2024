import commands2

import commands
import subsystems
from constants import DRIVING_MOTOR_SPEED, SIDEWAYS_MOTOR_SPEED, TURNING_MOTOR_SPEED


class RobotContainer:
    def __init__(self) -> None:
        # Subsystems
        self.drive = subsystems.Drive()
        self.servos = subsystems.Servos()
        self.servos.down()
        self.shooter = subsystems.Shooter()
        self.left_climber = subsystems.Climber(12)
        self.right_climber = subsystems.Climber(11, reversed=True)

        self.controller = commands2.button.CommandXboxController(0)

        self.configure_button_bindings()

        self.drive.setDefaultCommand(
            commands2.RunCommand(
                lambda: self.drive.move(
                    self.controller.getLeftY()*DRIVING_MOTOR_SPEED,
                    self.controller.getLeftX()*SIDEWAYS_MOTOR_SPEED,
                    self.controller.getRightX()*TURNING_MOTOR_SPEED,
                ), self.drive
            )
        )


    def configure_button_bindings(self) -> None:
        self.controller.a().onTrue(commands.ShootAmp(self.shooter, self.servos))
        self.controller.b().onTrue(commands.ShootSpeaker(self.shooter, self.servos))
        self.controller.y().whileTrue(commands2.cmd.runEnd(lambda: self.shooter.suck(), lambda: self.shooter.stop(), self.shooter))
        self.controller.leftBumper().whileTrue(commands2.cmd.runEnd(lambda: self.left_climber.climb_down(), lambda: self.left_climber.stop(), self.left_climber))
        self.controller.rightBumper().whileTrue(commands2.cmd.runEnd(lambda: self.right_climber.climb_down(), lambda: self.right_climber.stop(), self.right_climber))
        self.controller.leftTrigger().whileTrue(commands2.cmd.runEnd(lambda: self.left_climber.climb_up(), lambda: self.left_climber.stop(), self.left_climber))
        self.controller.rightTrigger().whileTrue(commands2.cmd.runEnd(lambda: self.right_climber.climb_up(), lambda: self.right_climber.stop(), self.right_climber))
    

    def getAutonomousCommand(self) -> commands2.Command:
        return commands.Autonomous(self.drive)
