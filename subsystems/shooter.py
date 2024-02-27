import commands2
import phoenix5
import wpilib
from constants import FiringSpeed

class Shooter(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        left_firing_motor = phoenix5.WPI_VictorSPX(8)
        left_firing_motor.setInverted(True)
        right_firing_motor = phoenix5.WPI_VictorSPX(5)
        self.firing_motors = wpilib.MotorControllerGroup(
            left_firing_motor, right_firing_motor
        )

        self.firing_speed = FiringSpeed.AMP

        self.solenoid = wpilib.Solenoid(1, wpilib.PneumaticsModuleType.REVPH, 0)
    
    def shoot(self):
        self.firing_motors.set(self.firing_speed.value)

    def suck(self):
        self.firing_motors.set(-self.firing_speed.value)
    
    def switch(self):
        self.firing_speed = -self.firing_speed
    
    def swivel(self):
        self.solenoid.toggle()