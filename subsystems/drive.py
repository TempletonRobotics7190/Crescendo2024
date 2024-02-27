import commands2
import phoenix5
import wpilib
import wpilib.drive
import wpimath.geometry

class Drive(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        rear_left_motor = phoenix5.WPI_TalonSRX(1)
        front_left_motor = phoenix5.WPI_TalonSRX(2)
        front_right_motor = phoenix5.WPI_TalonSRX(3)
        rear_right_motor = phoenix5.WPI_TalonSRX(4)

        self.robot_drive = wpilib.drive.MecanumDrive(
            front_left_motor,
            rear_left_motor,
            rear_right_motor,
            front_right_motor,
        )
    
    def move(self, x_speed: float, y_speed: float, z_rotation: float, gyro_angle: wpimath.geometry.Rotation2d):
        """
        X: Forward/Backward
        Y: Left/Right
        Z: Clockwise/Counterclockwise
        Gyro Angle: For Field-Oriented Driving
        """
        self.robot_drive.driveCartesian(
            z_rotation,
            y_speed,
            -x_speed,
            gyro_angle,
        )