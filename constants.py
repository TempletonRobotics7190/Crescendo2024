from __future__ import annotations

from enum import Enum

import rev

MOTOR_TYPE = rev.CANSparkLowLevel.MotorType.kBrushed
USE_PNEUMATICS = True
CONFIG_TAB_NAME = "Shuffleboard"

DRIVING_MOTOR_SPEED = 0.25
CLIMBING_MOTOR_SPEED = 0.5
INTAKE_MOTOR_SPEED = -0.25

POV_UP = 0
POV_RIGHT = 90
POV_DOWN = 180
POV_LEFT = 270


class FiringSpeed(Enum):
    AMP = 0.35
    SPEAKER = 0.75

    def __neg__(self) -> FiringSpeed:
        if self == FiringSpeed.AMP:
            return FiringSpeed.SPEAKER
        else:
            return FiringSpeed.AMP
